import datetime
from contextlib import ContextDecorator


class LogFile(ContextDecorator):

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self.start_time

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = datetime.datetime.now()
        self.diff = self.end_time - self.start_time
        log_file = (
            f"Start: {self.start_time} | Run: {self.diff} | An error occurred: {exc_value if exc_value else "None"}"
        )
        with open(self.filename, "w") as f:
            f.write(log_file)

        return False


@LogFile("task.txt")
def func():
    print("ok")
    
func()
