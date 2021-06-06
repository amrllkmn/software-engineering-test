import seed
import datetime as dt


# Converts timestamps into just dates
def from_datetime_to_date(timestamps):
    return [date.split(" ")[0] for date in timestamps]

# Gets the difference between two dates


def get_date_diff(date1, date2):
    date_1 = dt.datetime.strptime(date1, '%Y-%m-%d')
    date_2 = dt.datetime.strptime(date2, '%Y-%m-%d')
    return (date_1 - date_2).days


# Finds the longest consecutive login days
def sort_timestamps(timestamps):
    timestamps = from_datetime_to_date(timestamps)
    # Drops any duplicate days, as multiple logins in a day doesn't count
    timestamps = list(set(timestamps))

    # Sorts the timestamps by ascending order
    timestamps = sorted(timestamps)

    result = []
    start = end = ""
    streak = 0

    # Returns if there's only one timestamp
    if len(timestamps) == 1:
        return [(timestamps[0], timestamps[0], 1)]

    for i in range(len(timestamps)):
        if i == 0:
            start = timestamps[0]
            continue
        streak += 1
        date_diff = get_date_diff(timestamps[i], timestamps[i-1])

        is_streak_broken = False

        if i == (len(timestamps) - 1):  # In the case of reaching to the end of the timestamps
            end = timestamps[i]
            streak += 1
            is_streak_broken = True

        elif date_diff > 1:  # If it's too long after the previous login
            end = timestamps[i-1]
            is_streak_broken = True

        if is_streak_broken:
            result.append((start, end, streak))
            start = timestamps[i]
            end = ""
            streak = 0

    return result


def print_outputs(sorted_timestamps):
    # Print the outputs according to specifications (by length, in descending order)
    print("| START      | END        | LENGTH |")
    for timestamp in sorted(sorted_timestamps, key=lambda item: item[2], reverse=True):
        print("| {} | {} |   {}    |".format(
            timestamp[0], timestamp[1], timestamp[2]))


def main():
    timestamps = sorted(seed.result)  # Sorted the list to count the intervals
    print()
    print("Sorting timestamps by length of days of consecutive logins...")
    sorted_timestamps = sort_timestamps(timestamps)
    print()
    print("Printing outputs...")
    print_outputs(sorted_timestamps)


if __name__ == "__main__":
    main()
