class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, (date[:4], date[5:7], date[8:]))
        days_at_end_of_month = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
        day_of_year = days_at_end_of_month[month - 1] + day

        if month > 2 and year % 4 == 0 and (year % 100 or year % 400 == 0):
            day_of_year += 1

        return day_of_year
