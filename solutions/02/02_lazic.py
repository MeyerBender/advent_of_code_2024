import argparse
from textwrap import dedent

def is_safe(report):
    differences = [b - a for a, b in zip(report, report[1:])]
    return all(1 <= abs(d) <= 3 for d in differences) and (all(d > 0 for d in differences) or all(d < 0 for d in differences))

def is_safe_removal(report):
    # Check if the report is safe after removing one level
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the ith level
        if is_safe(modified_report):
            return True
    return False

#Part 1
# def count_safe(reports):
#     return sum(is_safe(list(map(int, report.split()))) for report in reports)

#Adapted for Part2
def count_safe(reports, allow_removal=False):
    safe_count = 0
    for report in reports:
        report_levels = list(map(int, report.split()))
        if is_safe(report_levels):
            safe_count += 1
        elif allow_removal and is_safe_removal(report_levels):
            safe_count += 1
    return safe_count

# To debug
# reports = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"
# reports = reports.replace("\\n", "\n").splitlines()
# allow_removal = True
# num_safe = count_safe(reports, allow_removal=allow_removal)
# print(f"The are {num_safe} safe reports in your input.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=dedent(
            """
            Analyze reports to find out how many are safe.
            Each report is a line of space separated numbers (i.e.. levels).
            
            A report is safe if:
              - The levels are either all increasing or all decreasing.
              - Any two adjacent levels differ by at least 1 and at most 3.
            
            Input can be given as a large block of text where each line is a separate report.
            Allows removing a single bad level to make a report safe.
            """
        )
    )

    parser.add_argument(
        "--reports", 
        type=str,
        help="Input your reports (one report per line) as a string using quotation marks."
    )

    parser.add_argument(
        "--allow-removal", 
        action="store_true", 
        help="Allow to remove a single bad level to make reports safe."
    )

    args = parser.parse_args()
    reports = args.reports

    reports = args.reports.replace("\\n", "\n").splitlines()
    num_safe = count_safe(reports, allow_removal=args.allow_removal)

    print(f"The are {num_safe} safe reports in your input.")
