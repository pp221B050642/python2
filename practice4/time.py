class Time:
    def __init__(self, seconds):
        self.seconds = seconds
    def convert_to_minutes(self):
        self.minutes = int(self.seconds/60)
        self.seconds2 = self.seconds - self.minutes*60
        return f'{self.minutes}:{self.seconds2}'
    def convert_to_hours(self):
        self.hours = int(self.seconds/3600)
        self.minutes2 = int((self.seconds-self.hours*3600)/60)
        self.seconds3 = self.seconds - self.minutes * 60
        return f"{self.hours}:{self.minutes2}:{self.seconds3}"

n = int(input())
t1 = Time(n)

print(t1.convert_to_minutes())
print(t1.convert_to_hours())
