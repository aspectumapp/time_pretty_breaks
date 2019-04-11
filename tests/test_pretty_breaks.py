import pytest
from dateutil.parser import parse as p
from dateutil.relativedelta import relativedelta

from time_pretty_breaks import nice_dt_intervals


SECONDS_PARAMS = [
    ('2019-03-31 02:59:02', '2019-03-31 03:02', 50),
    ('2019-03-31 02:59:59', '2019-03-31 03:02', 70),
]

SECONDS_RESULTS = [
    [p('2019-03-31 02:59') + relativedelta(seconds=5 * x) for x in range(37)],
    [p('2019-03-31 02:59:59') + relativedelta(seconds=x) for x in range(122)],
]


@pytest.mark.parametrize('params, result',
                         zip(SECONDS_PARAMS, SECONDS_RESULTS))
def test_seconds(params, result):
    begin, end, bins = params
    assert nice_dt_intervals(p(begin), p(end), bins) == result


MINUTES_PARAMS = [
    ('2018-12-31 19:22', '2019-01-01 02:02', 100),
    ('2016-02-28 23:59', '2016-03-01 00:02', 50),
    ('2019-03-31 02:59', '2019-03-31 04:02', 70),
]

MINUTES_RESULTS = [
    [p('2018-12-31 19:20') + relativedelta(minutes=5 * x) for x in range(82)],
    [p('2016-02-28 23:30') + relativedelta(minutes=30 * x) for x in range(51)],
    [p('2019-03-31 02:59') + relativedelta(minutes=x) for x in range(64)],
]


@pytest.mark.parametrize('params, result',
                         zip(MINUTES_PARAMS, MINUTES_RESULTS))
def test_miutes(params, result):
    begin, end, bins = params
    assert nice_dt_intervals(p(begin), p(end), bins) == result


HOURS_PARAMS = [
    ('2019-02-28 14:22', '2019-03-01 05:02', 18),
    ('2016-02-28 13:22', '2016-03-01 04:02', 19),
    ('2019-03-30 14:22', '2019-03-31 05:02', 18),
    ('2019-10-27 14:22', '2019-10-28 05:02', 19),
]

HOURS_RESULTS = [
    [p('2019-02-28 14:00') + relativedelta(hours=x) for x in range(17)],
    [p('2016-02-28 12:00') + relativedelta(hours=2 * x) for x in range(22)],
    [p('2019-03-30 14:00') + relativedelta(hours=x) for x in range(17)],
    [p('2019-10-27 14:00') + relativedelta(hours=x) for x in range(17)],
]


@pytest.mark.parametrize('params, result', zip(HOURS_PARAMS, HOURS_RESULTS))
def test_hours(params, result):
    begin, end, bins = params
    assert nice_dt_intervals(p(begin), p(end), bins) == result


DAYS_PARAMS = [
    ('2019-02-20', '2019-03-09', 15),
    ('2016-02-20', '2016-03-09', 15),
]

DAYS_RESULTS = [
    [p('2019-02-20') + relativedelta(days=x) for x in range(18)],
    [p('2016-02-20') + relativedelta(days=x) for x in range(19)],
]


@pytest.mark.parametrize('params, result', zip(DAYS_PARAMS, DAYS_RESULTS))
def test_days(params, result):
    begin, end, bins = params
    assert nice_dt_intervals(p(begin), p(end), bins) == result


WEEKS_PARAMS = [
    ('2019-04-04', '2019-05-19', 7),
    ('2018-12-31', '2019-12-19', 49),
    ('2018-12-31', '2019-01-04', 1),
]

WEEKS_RESULTS = [
    [p('2019-04-01') + relativedelta(weeks=x) for x in range(8)],
    [p('2018-12-31') + relativedelta(weeks=x) for x in range(52)],
    [p('2018-12-31'), p('2019-01-07')],
]


@pytest.mark.parametrize('params, result', zip(WEEKS_PARAMS, WEEKS_RESULTS))
def test_weeks(params, result):
    begin, end, bins = params
    assert nice_dt_intervals(p(begin), p(end), bins) == result


MONTHS_PARAMS = [
    ('2018-12-31', '2019-12-19', 12),
    ('2018-12-31', '2019-12-19', 5),
    ('2000-01-5', '2019-12-19', 43),
]


MONTHS_RESULTS = [
    [p('2018-12-01') + relativedelta(months=x) for x in range(14)],
    [p('2018-10-01') + relativedelta(months=3 * x) for x in range(6)],
    [p('2000-01-01') + relativedelta(months=6 * x) for x in range(41)],
]


@pytest.mark.parametrize('params, result', zip(MONTHS_PARAMS, MONTHS_RESULTS))
def test_months(params, result):
    begin, end, bins = params
    assert nice_dt_intervals(p(begin), p(end), bins) == result


YEARS_PARAMS = [
    ('2000-01-5', '2019-12-19', 19),
    ('1990-03-5', '2019-12-19', 19),
    ('1990-03-5', '2019-02-19', 19),
]


YEARS_RESULTS = [
    [p('2000-01-01') + relativedelta(years=x) for x in range(21)],
    [p('1990-01-01') + relativedelta(years=2 * x) for x in range(16)],
    [p('1990-01-01') + relativedelta(years=2 * x) for x in range(16)],
]


@pytest.mark.parametrize('params, result', zip(YEARS_PARAMS, YEARS_RESULTS))
def test_years(params, result):
    begin, end, bins = params
    assert nice_dt_intervals(p(begin), p(end), bins) == result
