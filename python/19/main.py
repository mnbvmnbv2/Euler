days = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
months = {
    "jan": 31,
    "feb": 28,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sep": 30,
    "oct": 31,
    "nov": 30,
    "dec": 31,
}


def main() -> int:
    c = 0
    d = 0

    year = 1900
    month = 0
    date = 0
    day = 0
    while year < 2001:
        # print(year, list(months.keys())[month], date, days[day])
        d += 1
        date += 1
        day += 1
        day %= len(days)
        date %= list(months.values())[month]
        if date == 0:
            month += 1
        if month == 12:
            month = 0
            year += 1
            if year % 4 != 0:
                months["feb"] = 28
            else:
                months["feb"] = 29
        if days[day] == "sun" and date == 0 and year > 1900:
            # print(year, list(months.keys())[month], date, days[day])
            c += 1
    return c


if __name__ == "__main__":
    print(main())
