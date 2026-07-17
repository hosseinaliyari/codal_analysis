import jdatetime
from datetime import datetime

class DatetimeHelper:

    def now_jalali_str():
        return jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def time_now_str():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def time_now():
        return datetime.now()

    def today():
        return datetime.now().date()