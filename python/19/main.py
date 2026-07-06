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


def is_leap(year: int) -> bool:
    return year % 4 == 0


def days_in_month(year: int, month: str) -> int:
    if month == "feb" and is_leap(year):
        return 29
    return months[month]


def main() -> int:
    c = 0
    day = 0
    for year in range(1900, 2001):
        for month in months:
            # print(year, list(months.keys())[month], date, days[day])
            if days[day] == "sun" and year > 1900:
                # print(year, list(months.keys())[month], date, days[day])
                c += 1
            day += days_in_month(year, month)
            day %= 7
    return c
