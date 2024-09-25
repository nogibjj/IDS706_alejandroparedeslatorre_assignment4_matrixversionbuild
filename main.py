import os
import sys
import re


def os_and_sys_version():
    python_version = re.search(r"\d+\.\d+", sys.version).group()
    os_name = os.getenv("RUNNER_OS")
    return python_version, os_name


if __name__ == "__main__":
    python_version_str, os_name_str = os_and_sys_version()
    print(f"Python version: {python_version_str}")
    print(f"OS name: {os_name_str}")