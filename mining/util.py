from datetime import timedelta, date
from typing import Iterable


def sanitize(string: str) -> str:
    return string.replace("\n", "")


def format_day_month(day_or_month: int) -> str:
    """
    Formats day or month as a 2-digit number, adding a zero prefix if needed.
    format_day_month(1) -> '01'
    format_day_month(12) -> '12'
    """
    if 1 <= day_or_month <= 9:
        return f"0{day_or_month}"
    elif 10 <= day_or_month <= 31:
        return str(day_or_month)
    else:
        raise Exception(f"{day_or_month} does not look like a day or a month")


def daterange(start_date: date, end_date: date) -> Iterable[date]:
    """
    Range of dates. End not inclusive
    From https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    """
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
