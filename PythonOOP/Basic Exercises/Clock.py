# Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers). The class
# should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to
# 59. You should also create 3 additional instance methods:
# - set_time(hours, minutes, seconds) - updates the time with the new values
# - get_time() - returns "{hh}:{mm}:{ss}"
# - next_second() - updates the time with one second (use the class attributes for validation) and returns
# the new time (use the get_time() method)

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.max_hours = 23
        self.max_min = 59
        self.max_sec = 59

    def set_time(self, new_hour, new_min, new_sec):
        self.hours = new_hour
        self.minutes = new_min
        self.seconds = new_sec

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        if self.seconds < self.max_sec:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < self.max_min:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < self.max_hours:
                    self.hours += 1
                else:
                    self.hours = 0

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time2 = Time(10, 59, 59)
print(time2.next_second())
time3 = Time(23, 59, 59)
print(time3.next_second())
