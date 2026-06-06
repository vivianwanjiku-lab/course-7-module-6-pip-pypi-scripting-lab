"""Top-level shim for AutoTest compatibility.

Some test runners import `generate_log` from the project root. Expose
`generate_log` here by delegating to `lib.generate_log.generate_log`.
"""
from lib.generate_log import generate_log

__all__ = ["generate_log"]
from datetime import datetime

def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for item in log_data:
            file.write(f"{item}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(data)