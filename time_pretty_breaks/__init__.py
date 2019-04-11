import numpy as np

from dateutil.rrule import rrule
from datetime import datetime, timedelta


def nicenumber(x):
    exp = np.floor(np.log10(x))
    f = x / 10 ** exp

    if f < 1.5:
        nf = 1
    elif f < 3:
        nf = 2
    elif f < 7.5:
        nf = 5
    else:
        nf = 10

    return nf * 10 ** exp


# How many seconds in each interval
ORDERS_SECONDS = (
    timedelta(365.25).total_seconds(),  # YEARLY
    timedelta(30.5).total_seconds(),  # MONTHLY
    timedelta(7).total_seconds(),  # WEEKLY
    timedelta(1).total_seconds(),  # DAILY
    3600,  # HOURLY
    60,  # HOURLY
    1,  # SECONDLY
)

ORDERS_MULTIPLIERS = (
    (1,),  # years
    (6, 3, 1),  # months
    (2, 1),  # weeks
    (1,),  # days
    (12, 6, 4, 3, 2, 1),  # hours
    (30, 20, 15, 10, 5, 1),  # minutes
    (30, 20, 15, 10, 5, 1),  # seconds
)


def nice_dt_intervals(begin: datetime, end: datetime, bins: int):
    """
    Split datatetime range into pretty intervals (by integer number of
    years, months, weeks, days, hours, minutes, seconds) number of intervals is
    close to bins number.

    :param begin: interval begin
    :param end: interval end
    :param bins: approximate amount of bins
    """

    time_delta = (end - begin) / bins
    seconds = time_delta.total_seconds()

    res_order = 6  # seconds
    res_multiplier = 1
    interval_seconds = 1
    min_dist = np.inf

    for order, order_seconds in enumerate(ORDERS_SECONDS):
        for multiplier in ORDERS_MULTIPLIERS[order]:
            break_seconds = order_seconds * multiplier
            dist = abs(seconds - break_seconds)

            if dist < min_dist:
                interval_seconds = break_seconds
                res_order = order
                res_multiplier = multiplier
                min_dist = dist
            else:
                break

    start = begin.replace(microsecond=0,
                          second=begin.second - begin.second % res_multiplier)

    if res_order < 6:  # minute
        start = start.replace(second=0,
                              minute=start.minute -
                              start.minute % res_multiplier)

    if res_order < 5:  # hour
        start = start.replace(minute=0,
                              hour=start.hour - start.hour % res_multiplier)

    if res_order < 4:  # day
        start = start.replace(hour=0,
                              day=start.day - (start.day - 1) % res_multiplier)

    if res_order == 2:  # by week
        start = start - timedelta(days=start.weekday())

    if res_order < 2:  # month
        start = start.replace(day=1,
                              month=start.month -
                              (start.month - 1) % res_multiplier)

    if res_order < 1:  # year
        start = start.replace(month=1)
        res_multiplier = int(nicenumber(seconds / ORDERS_SECONDS[0]))
        interval_seconds = res_multiplier * ORDERS_SECONDS[0]

    # to be sure that end date will be inside range with defined step
    end = end + timedelta(seconds=interval_seconds, milliseconds=-1)

    return list(rrule(freq=res_order,
                      dtstart=start,
                      until=end,
                      interval=res_multiplier))
