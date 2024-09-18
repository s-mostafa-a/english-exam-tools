import sys
import time

tasks = [
    {"task": 1, "prep_time": 30, "talk_time": 90},
    {"task": 2, "prep_time": 30, "talk_time": 60},
    {"task": 3, "prep_time": 30, "talk_time": 60},
    {"task": 4, "prep_time": 30, "talk_time": 60},
    {"task": "5-decide", "prep_time": 60, "talk_time": 0},
    {"task": 5, "prep_time": 60, "talk_time": 60},
    {"task": 6, "prep_time": 60, "talk_time": 60},
    {"task": 7, "prep_time": 60, "talk_time": 90},
    {"task": 8, "prep_time": 30, "talk_time": 60},
]


def countdown(title, seconds):
    sys.stdout.flush()
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{title} {mins:02}:{secs:02}'
        sys.stdout.write(f"\r{timer}")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1


def celpip_timer():
    for task in tasks:
        countdown(f"Task {task['task']} prepare:", task['prep_time'])
        countdown(f"Task {task['task']} talk:", task['talk_time'])
    print("All tasks completed.")


if __name__ == "__main__":
    celpip_timer()
