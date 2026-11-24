class MyDate:
    MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
              "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
    DAY_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana kiritildi!")
        self.__day = day
        self.__month = month
        self.__year = year

    def isLeapYear(self, year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return year % 4 == 0

    def getDays(self, month, year):
        # oyning kunlar sonini qaytaradi
        if month == 2 and self.isLeapYear(year):
            return 29
        return self.DAY_IN_MONTHS[month - 1]

    def isValidDate(self, day, month, year):
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > self.getDays(month, year):
            return False
        return True

    def setDate(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana kiritildi!")
        self.__day = day
        self.__month = month
        self.__year = year

    def nextDay(self):
        day = self.__day + 1
        month = self.__month
        year = self.__year
        if day > self.getDays(month, year):
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        self.setDate(day, month, year)

    def previousDay(self):
        day = self.__day - 1
        month = self.__month
        year = self.__year
        if day < 1:
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            if year < 1:
                raise ValueError("Noto'g'ri sana kiritildi!")
            day = self.getDays(month, year)
        self.setDate(day, month, year)

    def nextMonth(self):
        month = self.__month + 1
        year = self.__year
        if month > 12:
            month = 1
            year += 1
        day = self.__day
        if year <= 9999 and day > self.getDays(month, year):
            day = self.getDays(month, year)
        self.setDate(day, month, year)

    def previousMonth(self):
        month = self.__month - 1
        year = self.__year
        if month < 1:
            month = 12
            year -= 1
        day = self.__day
        if year >= 1 and day > self.getDays(month, year):
            day = self.getDays(month, year)
        self.setDate(day, month, year)

    def nextYear(self):
        year = self.__year + 1
        day = self.__day
        if year <= 9999 and day > self.getDays(self.__month, year):
            day = self.getDays(self.__month, year)
        self.setDate(day, self.__month, year)

    def previousYear(self):
        year = self.__year - 1
        day = self.__day
        if year >= 1 and day > self.getDays(self.__month, year):
            day = self.getDays(self.__month, year)
        self.setDate(day, self.__month, year)

    def __str__(self):
        return f"{self.__day:02d}-{self.MONTHS[self.__month - 1]} {self.__year} yil"


if __name__ == "__main__":
    #uyishi1
    sana = MyDate(15, 6, 2023); sana.nextDay(); print(sana)

    #uyishi2
    sana = MyDate(30, 4, 2023); sana.nextDay(); print(sana)

    #uyishi3
    sana = MyDate(31, 12, 2023); sana.nextDay(); print(sana)

    #uyishi4
    sana = MyDate(1, 5, 2023); sana.previousDay(); print(sana)

    #uyishi5
    sana = MyDate(28, 2, 2024); sana.nextDay(); print(sana)

    #uyishi6
    sana = MyDate(29, 2, 2024); sana.nextDay(); print(sana)

    #uyishi7
    sana = MyDate(28, 2, 2023); sana.nextDay(); print(sana)

    #uyishi8
    sana = MyDate(1, 1, 2023); sana.previousDay(); print(sana)

    #uyishi9
    try:
        sana = MyDate(15, 6, 10000)
    except ValueError as e:
        print(e)

    #uyishi10
    try:
        sana = MyDate(15, 13, 2023)
    except ValueError as e:
        print(e)

    #uyishi11
    try:
        sana = MyDate(32, 5, 2023)
    except ValueError as e:
        print(e)

    #uyishi12
    sana = MyDate(15, 6, 2023); sana.setDate(5, 7, 2023); print(sana)

    #uyishi13
    try:
        sana = MyDate(15, 6, 2023)
        sana.setDate(31, 4, 2023)
    except ValueError as e:
        print(e)