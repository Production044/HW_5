import sys


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return logs


def parse_log_line(line: str) -> dict:
    components = line.split(' ', maxsplit=3)
    final = {'time': components[0] + ' ' + components[1],
             'level': components[2],
             'message': components[3].strip()}

    return final


def filter_logs_by_level(logs, level):
    filtered_logs = []
    for log in logs:
        if log['level'] == level:
            filtered_logs.append(log)

    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts: dict):

    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count:<10}")


def display_logs(logs: list):
    print("Деталі логів:")
    for log in logs:
        print(f"{log['time']} - {log['message']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python HW_5.3.py logfile.log [optional: log_level]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = None

    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()

    logs = load_logs(log_file)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        display_log_counts(count_logs_by_level(logs))
        print("\nДеталі логів для рівня '{}':".format(log_level))
        display_logs(filtered_logs)
    else:
        display_log_counts(count_logs_by_level(logs))