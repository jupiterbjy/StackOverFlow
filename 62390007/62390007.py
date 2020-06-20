import re
from datetime import datetime


class Event:
    """
    Class isn't necessary, and longer than other solutions.
    But class gives you more control when expansion / changes are needed.
    """
    def __init__(self, start, statement, end, success):
        self.start = re.search(r"[0-9]{4}.*", start).group(0)
        self.statement = re.search(r"(?<=\()[^)]*", statement).group(0)
        self.end = re.search(r"[0-9]{4}.*", end).group(0)
        self.success = success.split()[-1]

    def __repr__(self):
        """
        When str() or print() is called on this class instances -
        this will be output.
        """
        return f"Event starting at {self.start}, Took {self.deltaTime} sec."

    @property
    def deltaTime(self):
        """
        Converting string to datetime object to perform delta time calculation.
        """
        date_format = "%Y-%m-%d %H:%M:%S"
        start = datetime.strptime(self.start, date_format)
        end = datetime.strptime(self.end, date_format)
        return (end - start).total_seconds()


def generate_events(file):
    def lineYield():
        """
        Generates line inside file without need to load whole file in memory.
        As generator is one-shot, using this to simplify pause / continue of
        line iteration.
        """
        for line_ in file:
            yield line_.strip("\n")

    find_list = ["Start Time", "Statement", "End Time"]
    generator = lineYield()

    while True:
        group = []
        for target in find_list:
            for line in generator:  # our generator keeps state after this loop.
                if target in line:
                    group.append(line)
                    break

        for line in generator:
            if "Success" in line or "Failed" in line:
                group.append(line)
                break

        try:
            yield Event(*group)
        except TypeError:
            return


def find_slowest(log_file):
    formed = list(generate_events(log_file))
    sorted_output = sorted(formed, key=lambda event_: event_.deltaTime)

    print("Recorded Events:")
    for output in sorted_output:
        print(output)

    late_runner = sorted_output[-1]
    print(f"\nSlowest: <{late_runner.statement}>")
    print(f"Took   : {late_runner.deltaTime} sec")
    print(f"Status : {late_runner.success}")


with open("log.txt", 'r') as log:
    find_slowest(log)
