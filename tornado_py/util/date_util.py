# -*- coding: UTF-8 -*-

import datetime
import time
import calendar
from dateutil.relativedelta import relativedelta


class DateUtil:
    date_format_t = "%Y-%m-%d %H:%M:%S"

    date_format_d = "%Y-%m-%d"

    @staticmethod
    def now():
        return datetime.datetime.now()

    # datetime 转化为 String %Y%m%d %H:%M:%S
    @staticmethod
    def date_to_str_t(date):
        return date.strftime(DateUtil.date_format_t)

    # datetime 转化为 String %Y%m%d
    @staticmethod
    def date_to_str_d(date):
        return date.strftime(DateUtil.date_format_d)

    @staticmethod
    def data_to_string_d(date):
        if isinstance(date, datetime.date):
            str_date = date.strftime(DateUtil.date_format_d)
        else:
            str_date = str(date)
        return str_date

    # String 转化为 datetime %Y%m%d  %H:%M:%S
    @staticmethod
    def str_to_date_s(t_str):
        return datetime.datetime.strptime(t_str, DateUtil.date_format_t)

    # String 转化为 datetime %Y%m%d
    @staticmethod
    def str_to_date_d(t_str):
        return datetime.datetime.strptime(t_str, DateUtil.date_format_d)

    # 获取两个日期间相差的天数
    @staticmethod
    def get_poor_days(t_str1, t_str2):
        delta = DateUtil.str_to_date_s(t_str1) - DateUtil.str_to_date_s(t_str2)
        return delta.days

    # 某天的n天后的日期。
    @staticmethod
    def get_date_after(t_str1, n):
        date = DateUtil.str_to_date_d(t_str1)
        delta = datetime.timedelta(days=n)
        n_days = date + delta
        return DateUtil.date_to_str_d(n_days)

    # 某天的n天后的日期。
    @staticmethod
    def get_date_after_by_date(date, n):
        delta = datetime.timedelta(days=n)
        n_days = date + delta
        return n_days

    @staticmethod
    def get_current_slot(date, index, days):
        """

        :param datetime date: current day
        :param int index: page index
        :param int days: the count of day
        :return: datetime start_day, datetime end_day
        """
        end_day = DateUtil.get_date_after_by_date(date, -index * days)
        start_day = DateUtil.get_date_after_by_date(date, -(index + 1) * days)
        # if n_day > m_day:
        #     start_day = m_day
        #     end_day = n_day
        # else:
        #     end_day = m_day
        #     start_day = n_day
        return start_day, end_day

    @staticmethod
    def get_current_slot_week(date, index, days):
        """

        :param datetime date: current day
        :param int index: page index
        :param int days: the count of day
        :return: datetime start_day, datetime end_day
        """
        end_day = DateUtil.get_date_after_by_date(date, -index * days*7)
        start_day = DateUtil.get_date_after_by_date(date, -(index + 1) * days*7)
        # if n_day > m_day:
        #     start_day = m_day
        #     end_day = n_day
        # else:
        #     end_day = m_day
        #     start_day = n_day
        end_week = DateUtil.get_current_week(end_day)
        start_week = DateUtil.get_current_week(start_day)
        if end_week[1] < 10:
            str_e_w = "0" + str(end_week[1])
        else:
            str_e_w = str(end_week[1])
        if start_week[1] < 10:
            str_s_w = "0" + str(start_week[1])
        else:
            str_s_w = str(start_week[1])
        ew = int(str(end_week[0]) + str_e_w)
        sw = int(str(start_week[0]) + str_s_w)
        return sw, ew

    # 获得时间戳
    @staticmethod
    def get_time_stamp(str_data):

        if str_data is None or str_data == "":
            stamp = int(time.time())
        else:
            stamp = int(time.mktime(time.strptime(str_data, "%Y-%m-%d %H:%M:%S")))
        return stamp

    # 时间戳转化时间
    @staticmethod
    def stamp_to_date(stamp):

        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stamp))
        return dt

    # 获取当前日期是星期几
    @staticmethod
    def date_to_week(str_date):

        return DateUtil.str_to_date_d(str_date).isoweekday()

    @staticmethod
    def get_greenwich():

        return time.gmtime()

    @staticmethod
    def get_current_utc_timestamp():
        return (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()

    @staticmethod
    def utc_to_local(utc_dt):
        now_stamp = time.time()
        local_time = datetime.datetime.fromtimestamp(now_stamp)
        utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
        offset = local_time - utc_time
        local_st = utc_dt + offset
        return local_st

    @staticmethod
    def local_to_utc(local_dt):
        time_struct = time.mktime(local_dt.timetuple())
        utc_st = datetime.datetime.utcfromtimestamp(time_struct)
        return utc_st

    @staticmethod
    def str_to_datetime(str_date, date_format = date_format_t):
        try:
            return datetime.datetime.strptime(str_date, date_format)
        except Exception as e:
            print(e.message)
            return None

    @staticmethod
    def str_to_date(str_date, date_format = date_format_d):
        try:
            return datetime.datetime.strptime(str_date, date_format)
        except Exception as e:
            print(e.message)
            return None

    @staticmethod
    def datetime_to_str(dt, date_format = date_format_t):
        return dt.strftime(date_format)

    @staticmethod
    def date_to_str(dt, date_format = date_format_d):
        return dt.strftime(date_format)

    @staticmethod
    def get_year_month(dt=datetime.datetime.now()):
        return dt.year * 100 + dt.month

    @staticmethod
    def get_year_week(dt=datetime.datetime.now()):
        cal = dt.isocalendar()
        return cal[0] * 100 + cal[1]

    @staticmethod
    def get_year_quarter(dt=datetime.datetime.now(), offset_month=0):
        new_dt = dt - relativedelta(months=offset_month)
        month = (dt.month - offset_month) % 12
        if month <= 0:
            month += 12
        quarter_offset = 0 if (month % 3) == 0 else 1
        return new_dt.year * 10 + month / 3 + quarter_offset

    @staticmethod
    def get_current_day():
        """返回当前日期时间的日期部分

        :return: date
        """
        return datetime.datetime.now().date()

    @staticmethod
    def get_current_week(now_date):
        """

        :param now_date:
        :return:
        """
        return now_date.isocalendar()

    @staticmethod
    def get_year_and_month(now_day, n=0):
        """
        get the year,month,days from today
        before or after n months
        :param date now_day:current date
        :param int n: month count
        :return:
        """
        print(now_day)
        this_year = now_day.year
        this_mon = now_day.month
        total_mon = this_mon + n
        if n >= 0:
            if total_mon <= 12:
                days = str(DateUtil.get_days_of_month(this_year, total_mon))
                total_mon = DateUtil.add_zero(total_mon)
                return str(this_year), str(total_mon), days
            else:
                quotient = total_mon/12
                modular_month = total_mon % 12
                if modular_month == 0:
                    quotient -= 1
                    modular_month = 12
                this_year += quotient
                days = str(DateUtil.get_days_of_month(this_year, modular_month))
                modular_month = DateUtil.add_zero(modular_month)
                return str(this_year), str(modular_month), days
        else:
            if (total_mon > 0) and (total_mon < 12):
                days = str(DateUtil.get_days_of_month(this_year, total_mon))
                total_mon = DateUtil.add_zero(total_mon)
                return str(this_year), str(total_mon), days
            else:
                quotient = total_mon/12
                modular_month = total_mon % 12
                if modular_month == 0:
                    quotient -= 1
                    modular_month = 12
                days = str(DateUtil.get_days_of_month(this_year, modular_month))
                modular_month = DateUtil.add_zero(modular_month)
                return str(this_year), str(modular_month), days

    @staticmethod
    def add_zero(n):
        """
        add 0 before 0-9
        :param n:
        :return: 01-09
        """
        nabs = abs(int(n))
        if nabs < 10:
            return "0"+str(nabs)
        else:
            return nabs

    @staticmethod
    def get_days_of_month(year, mon):
        """get days of month
        :param year:
        :param mon:
        :return:
        """
        return calendar.monthrange(year, mon)[1]

    @staticmethod
    def get_current_quarter(now_day):
        """
        get days of quarter
        :param now_day:
        :return:
        """
        this_year = now_day.year
        this_mon = now_day.month

        if 0 < this_mon < 4:
            quarter = 1
        elif 3 < this_mon < 7:
            quarter = 2
        elif 6 < this_mon < 10:
            quarter = 3
        else:
            quarter = 4
        return str(this_year), str(quarter)

# if __name__ == '__main__':
#     utc_now = DateUtil.local_to_utc(DateUtil.now())
#     print(utc_now)
#     print(datetime.datetime.utcnow())

