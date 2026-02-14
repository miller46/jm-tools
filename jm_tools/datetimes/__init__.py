from datetime import datetime
import time

UTC_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_date(date_string) -> datetime:
    return datetime.strptime(date_string, UTC_DATE_FORMAT)


def get_current_datetime():
    return datetime.utcnow().strftime(UTC_DATE_FORMAT)

def get_current_timestamp():
    return int(time.time())


def timestamp_to_hour_of_day(timestamp, timezone_offset):
    """
    Takes a Unix timestamp and returns the hour of the day in 12-hour format.
    """
    dt = datetime.fromtimestamp(timestamp + timezone_offset)
    return dt.strftime("%-I%p")


def timestamp_to_date_and_time(timestamp, timezone_offset):
    # Convert timestamp to datetime object
    dt = datetime.fromtimestamp(timestamp + timezone_offset)
    return dt.strftime('%m/%d/%Y %I:%M%p')


def timestamp_to_date_only(timestamp, timezone_offset):
    # Convert timestamp to datetime object
    dt = datetime.fromtimestamp(timestamp + timezone_offset)
    return dt.strftime('%m/%d/%Y')


def timestamp_to_full_time_only(timestamp, timezone_offset):
    # Convert timestamp to datetime object
    dt = datetime.fromtimestamp(timestamp + timezone_offset)
    return dt.strftime('%I:%M%p')

