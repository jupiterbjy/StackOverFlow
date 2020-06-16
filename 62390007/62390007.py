import re
from datetime import datetime


class Event:
    def __init__(self, start, statement: str, end, success):
        self.start = re.search(r"[0-9]{4}.*", start).group(0)
        self.statement = statement.replace("Statement ", "").strip(";\n")
        self.end = re.search(r"[0-9]{4}.*", end).group(0)
        self.success = success

    def __repr__(self):
        return f"Event starting at {self.start}, Took {self.deltaTime} sec."

    @property
    def deltaTime(self):
        form = "%Y-%m-%d %H:%M:%S"
        start = datetime.strptime(self.start, form)
        end = datetime.strptime(self.end, form)
        return (end - start).total_seconds()


def generate_events(file):
    def lineYield():
        for line_ in file:
            yield line_.split("|  ")[-1].strip("\n")

    find_list = ["Start Time", "Statement", "End Time"]
    generator = lineYield()

    while True:
        group = []
        for target in find_list:
            for line in generator:
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
    print(f"\nSlowest: {late_runner.statement}")
    print(f"Took   : {late_runner.deltaTime} sec")
    print(f"Status : {late_runner.success}")


with open("log.txt", 'r') as log:
    find_slowest(log)
