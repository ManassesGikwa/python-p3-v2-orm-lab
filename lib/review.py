from lib import CURSOR, CONN

from lib.employee import Employee
class Review:
    def __init__(self, year, summary, employee):
        self.id = None
        self._year = None
        self._summary = None
        self._employee_id = None

        self.year = year
        self.summary = summary
        self.employee = employee

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and value >= 2000:
            self._year = value
        else:
            raise ValueError("Year must be an integer greater than or equal to 2000")

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if isinstance(value, str) and value.strip():
            self._summary = value
        else:
            raise ValueError("Summary must be a non-empty string")

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        if isinstance(value, int):
            self._employee_id = value
        else:
            raise ValueError("Employee ID must be an integer")
