import os
import webbrowser
import datetime
import pytest

TEST_FILE = "TestFilePath"
REPORT_FILE = "ReportFilePath"
 
def main():
    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Build timestamped report path
    directory = os.path.dirname(REPORT_FILE)
    base_name = "DEA PrescriberTracker"
    report_file_timestamped = os.path.join(directory, f"{base_name}_{timestamp}.html")

    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)

    # Run pytest with HTML report
    args = [
        TEST_FILE,
        f"--html={report_file_timestamped}",
        "--self-contained-html",
        "-v"
    ]
    exit_code = pytest.main(args)

    # Open the report
    if os.path.exists(report_file_timestamped):
        webbrowser.open(report_file_timestamped)
        print(f"\n{'✅ All tests passed!' if exit_code == 0 else '❌ Some tests failed.'}")
        print(f"Report opened: {report_file_timestamped}")
    else:
        print("\n⚠️ Report not generated. Check test execution or pytest-html installation.")

if __name__ == "__main__":
    main() 