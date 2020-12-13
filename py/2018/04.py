import datetime


class AdventOfCode:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = list(sorted(f.read().splitlines()))

        self.guards = {}

        for line in self.input:
            year = int(line[1:5])
            month = int(line[6:8])
            day = int(line[9:11])
            date = datetime.date(year, month, day)
            hour = int(line[12:14])
            minute = int(line[15:17])

            msg = line[19:]

            if hour >= 20:
                date = date + datetime.timedelta(1)

            if msg.startswith('Guard #'):
                guard_id = int(msg.split()[1][1:])
                guard = self.guards.setdefault(guard_id, Guard(guard_id))
            elif msg == 'falls asleep':
                guard.fall_asleep(date, minute)
            elif msg == 'wakes up':
                guard.wake_up(date, minute)
            else:
                raise ValueError(f'Unknown message: {msg}')

    def part1(self):
        record = -1
        for g in self.guards.values():
            if g.minutes_asleep() > record:
                record = g.minutes_asleep()
                sleepy_guard = g

        sleepy_minute = sleepy_guard.sleepiest_minute()[0]

        return sleepy_guard.id * sleepy_minute

    def part2(self):
        record = -1
        for g in self.guards.values():
            if g.sleepiest_minute()[1] > record:
                record = g.sleepiest_minute()[1]
                sleepy_guard = g

        sleepy_minute = sleepy_guard.sleepiest_minute()[0]

        return sleepy_guard.id * sleepy_minute


class Guard:
    def __init__(self, guard_id):
        self.id = guard_id
        self.shifts = {}
        self.total_asleep_time = -1
        self.sleepy_minute = -1
        self.sleepy_minute_count = -1

    def fall_asleep(self, shift, minute):
        shift = self.shifts.setdefault(shift, [False]*60)
        shift[minute:] = [True]*(60-minute)

    def wake_up(self, shift, minute):
        shift = self.shifts.setdefault(shift, [False]*60)
        shift[minute:] = [False]*(60-minute)

    def minutes_asleep(self):
        if self.total_asleep_time == -1:
            self.total_asleep_time = sum([sum(s) for s in self.shifts.values()])

        return self.total_asleep_time

    def sleepiest_minute(self):
        if self.sleepy_minute == -1:
            all_minutes = [sum([s[i] for s in self.shifts.values()]) for i in range(60)]

            self.sleepy_minute_count = max(all_minutes)
            self.sleepy_minute = all_minutes.index(self.sleepy_minute_count)

        return self.sleepy_minute, self.sleepy_minute_count
