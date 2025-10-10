"""
https://www.codewars.com/kata/656e4602ee72af0017e37e82

The cuckoo bird pops out of the cuckoo clock and chimes once on the quarter-hour, half hour, and three-quarter
hour. At the beginning of each hour (1-12), it chimes out the hour. Given the current time and a number n,
determine the time when the cuckoo bird has chimed n times.

Input Parameters:
initial_time - a string in the format "HH:MM", where 1 ≤ HH ≤ 12 and 0 ≤ MM ≤ 59, with leading 0’s if necessary.
n - an integer representing the target number of chimes, with 1 <= n <= 200.

Return Value: The time when the cuckoo bird has chimed n  times - a string in the same format as initial_time.

If the cuckoo bird chimes at initial_time, include those chimes in the count. If the nth chime is reached on the
hour, report the time at the start of that hour (i.e. assume the cuckoo finishes chiming before the minute is up).

Example: "03:38", 19   should return "06:00". Explanation: It chimes once at "03:45", 4 times at "04:00",
once each at "04:15", "04:30", "04:45", 5 times at "05:00", and once each at "05:15", "05:30", "05:45". At this
point it has chimed 16 times, so the 19th chime occurs when it chimes 6 times at "06:00".

Source: International Collegiate Programming Contest, North Central North American Regional, 2023.
"""


def cuckoo_clock(initial_time: str, n: int) -> str:
    chime_counter = 0
    initial_time_list = initial_time.split(":")
    hour = int(initial_time_list[0])
    minute = int(initial_time_list[1])
    hour_chime = 0
    minute_chime_list = [15, 30, 45]
    hour_dict = {i: hour for hour, i in enumerate(range(13, 25), start=1)}
    for i in range(n):
        if hour in hour_dict:
            hour = hour_dict[hour]
        if minute == hour_chime:
            chime_counter += hour
        if minute in minute_chime_list:
            chime_counter += 1
        if chime_counter >= n:
            break
        else:
            if minute < 15:
                minute = 15
            elif 15 <= minute < 30:
                minute = 30
            elif 30 <= minute < 45:
                minute = 45
            else:
                minute = 0
                hour += 1
    return f"{hour:02d}:{minute:02d}"


# if __name__ == "__main__":
#     print(cuckoo_clock("09:53", 50))


# CODEWARS TESTS -------------------------------------------------------------------------------------------------------
import unittest


class Test(unittest.TestCase):
    def test_simple_tests(self):
        print("Simple Cases")
        initial_times = ["07:22", "12:22", "01:30", "04:01", "03:38"]
        chimes = [1, 2, 2, 10, 19]
        expected_times = ["07:30", "12:45", "01:45", "05:30", "06:00"]

        for initial_time, n, expected in zip(initial_times, chimes, expected_times):
            print("initial time", initial_time, "expected time", expected, "got", cuckoo_clock(initial_time, n))
            self.assertEqual(cuckoo_clock(initial_time, n), expected)

    def test_hour_tests(self):
        print("Starting on the Hour")
        initial_times = ["10:00", "10:00", "10:00", "10:00", "10:00"]
        chimes = [1, 10, 11, 13, 20]
        expected_times = ["10:00", "10:00", "10:15", "10:45", "11:00"]

        for initial_time, n, expected in zip(initial_times, chimes, expected_times):
            print("initial time", initial_time, "expected time", expected, "got", cuckoo_clock(initial_time, n))
            self.assertEqual(cuckoo_clock(initial_time, n), expected)

    def test_twelve_tests(self):
        print("Crossing Twelve")  # From "12:MM" to "01:NN"
        initial_times = ["12:30", "12:30", "12:30", "12:30", "09:53"]
        chimes = [1, 2, 3, 4, 50]
        expected_times = ["12:30", "12:45", "01:00", "01:15", "02:30"]

        for initial_time, n, expected in zip(initial_times, chimes, expected_times):
            print("initial time", initial_time, "expected time", expected, "got", cuckoo_clock(initial_time, n))
            self.assertEqual(cuckoo_clock(initial_time, n), expected)

    def test_around_tests(self):
        print("Around the Clock")  # From "HH:MM" to "HH:NN" 12 hours later
        initial_times = ["08:17", "08:17", "08:17", "08:17", "08:17"]
        chimes = [113, 114, 115, 150, 200]
        expected_times = ["08:00", "08:15", "08:30", "11:00", "05:45"]

        for initial_time, n, expected in zip(initial_times, chimes, expected_times):
            print("initial time", initial_time, "expected time", expected, "got", cuckoo_clock(initial_time, n))
            self.assertEqual(cuckoo_clock(initial_time, n), expected)


if __name__ == "__main__":
    unittest.main()
