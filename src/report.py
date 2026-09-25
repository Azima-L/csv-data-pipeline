from pathlib import Path
from datetime import datetime

def generate_report(input_file, output_file, issues_count, issue_details, total_records):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_path = Path(__file__).parent.parent / "reports" / "audit_report.txt"
    report_path.parent.mkdir(exist_ok=True)

    with open(report_path, "w") as f:
        f.write("=" * 45 + "\n")
        f.write("PIPELINE AUDIT REPORT\n")
        f.write("=" * 45 + "\n")

        f.write(f"Run timestamp : {timestamp}\n")
        f.write(f"Input file    : {input_file}\n")
        f.write(f"Output file   : {output_file}\n")

        f.write("\n" + "-" * 45 + "\n")
        f.write("VALIDATION SUMMARY\n")
        f.write("-" * 45 + "\n")
        f.write(f"Total records : {total_records}\n")
        f.write(f"Issues found  : {issues_count}\n")

        if issue_details:
            f.write("\nIssue details :\n")
            for detail in issue_details:
                f.write(f"  {detail}\n")
        else:
            f.write("  No issue found.\n")

        f.write("\n" + "-" * 45 + "\n")
        f.write("TRANSFORMATIONS APPLIED\n")
        f.write("-" * 45 + "\n")
        f.write("  - Name casing normalized\n")
        f.write("  - Salary values clipped to [50000, 200000]\n")
        f.write("  - Dates parsed to datetime format\n")

        f.write("\n" + "-" * 45 + "\n")
        f.write("PIPELINE STATUS: COMPLETE\n")
        f.write("-" * 45 + "\n")

    print(f"[INFO] Audit report written to reports/{report_path.name}")