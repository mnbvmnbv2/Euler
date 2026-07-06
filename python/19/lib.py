import datetime


def main() -> int:
    return sum(
        datetime.date(year, month, 1).weekday() == 6
        for year in range(1901, 2001)
        for month in range(1, 13)
    )
