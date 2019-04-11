# Time, Date, DateTime Pretty Breaks

Split time range into ~N "rounded" intervals using the following logic:

Divide range by N and select the closest step from below:

- One year
- Six months, three months, one month
- Two weeks, one week
- One day
- Hours: 12, 6, 4, 3, 2, 1
- Minutes: 30, 20, 15, 10, 5, 1
- Seconds: 30, 20, 15, 10, 5, 1

If the interval is greater than one year, then use Pretty Breaks algorithm for the step.

Each interval starts with time multiple of step. E.g., if we have 20 min step
and the range starts at 19:43, then the first interval should starts at 19:40.


## Examples

| Range start         | Range end        | N  | Result                                                                                                        | Description                             |
|---------------------|------------------|----|---------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| 2019-04-04          | 2019-05-19       | 7  | 2019-04-01, 2019-04-08, 2019-04-15, 2019-04-22, 2019-04-29, 2019-05-06, 2019-05-13, 2019-05-20                | Split by one week, starts on Monday     |
| 2019-03-31 02:59:02 | 2019-03-31 03:02 | 50 | 2019-03-31 02:59:00, 2019-03-31 02:59:05, 2019-03-31 02:59:10, ... , 2019-03-31 03:01:55, 2019-03-31 03:02:00 | Split by 5 sec, starts at multiple time |
| 2018-12-31          | 2019-12-19       | 5  | 2018-10-01, 2019-01-01, 2019-04-01, 2019-07-01, 2019-10-01, 2020-01-01                                        | Split by three months, starts at Jan. 1 |


## Usage
```python
>>> from time_pretty_breaks import nice_dt_intervals
>>> from datetime import datetime
>>> nice_dt_intervals(datetime(2018, 12, 31), datetime(2019, 12, 19), 5)
[datetime.datetime(2018, 10, 1, 0, 0), datetime.datetime(2019, 1, 1, 0, 0), datetime.datetime(2019, 4, 1, 0, 0), datetime.datetime(2019, 7, 1, 0, 0), datetime.datetime(2019, 
10, 1, 0, 0), datetime.datetime(2020, 1, 1, 0, 0)]
```
