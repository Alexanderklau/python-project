# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'


def weekends_between(d1, d2):
    days_between = (d2 - d1).days
    weekends, leftover = divmod(days_between, 7)
    if leftover:
        start_day = (d2 - timedelta(leftover)).isoweekday()
        end_day = start_day + leftover
        if start_day <= 6 and end_day > 6:
            weekends += .5
        if start_day <= 7 and end_day > 7:
            weekends += .5
    return weekends
weekends_between((2014, 10, 1))
# weekends_between(date(2014, 10, 1), date(2014, 10, 10))










# if __name__ == '__main__':