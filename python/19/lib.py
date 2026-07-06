import datetime


def main() -> int:
    c = 0
    day = datetime.date(1901, 1, 1)
    print(day)
    while day < datetime.date(2001, 1, 1):
        day += datetime.timedelta(1)
        if day.weekday() == 6 and day.isoformat().split("-")[-1] == "01":
            c += 1
    return c


if __name__ == "__main__":
    print(main())
