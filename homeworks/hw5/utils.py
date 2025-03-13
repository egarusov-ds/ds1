from datetime import datetime


def get_house_age(raw: str) -> float:
    parsed = datetime.strptime(raw, "%Y%m%dT%H%M%S")
    end = datetime(year=2015, month=6, day=1)
    return (end - parsed).days / 365
