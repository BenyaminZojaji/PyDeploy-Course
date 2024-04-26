import time
import random


def marriage(name):
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"{name} married after {r} years.")


def main():
    for child in ["Benyamin", "Jack", "David", "Alex"]:
        marriage(child)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time:0.3f} seconds.")
    