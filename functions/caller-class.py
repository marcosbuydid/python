class Day:
    def __init__(self):
        self.days = {0: 'Sunday', 1: 'Monday',
                     2: 'Tuesday', 3: 'Wednesday',
                     4: 'Thursday', 5: 'Friday',
                     6: 'Saturday'}

    def __call__(self, dayno):
        return self.days[dayno]


day = Day()
print(day(5))
