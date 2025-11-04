import subprocess
import sys

SCRIPT_NAME = "whatis.py"
PYTHON_CMD = sys.executable


def test_1_no_argument():
    result = subprocess.run([PYTHON_CMD, SCRIPT_NAME],
                            capture_output=True,
                            text=True,
                            check=False)
    assert result.stdout.strip() == "", "Test 1 Failed: Expected no output."


def test_2_even_number():
    result = subprocess.run([PYTHON_CMD, SCRIPT_NAME, "14"],
                            capture_output=True,
                            text=True,
                            check=False)
    assert result.stdout.strip(
    ) == "I'm Even.", f"Test 2 Failed: Output was '{result.stdout.strip()}'"


def test_3_odd_number():
    result = subprocess.run([PYTHON_CMD, SCRIPT_NAME, "-5"],
                            capture_output=True,
                            text=True,
                            check=False)
    assert result.stdout.strip(
    ) == "I'm Odd.", f"Test 3 Failed: Output was '{result.stdout.strip()}'"


def test_4_zero():
    result = subprocess.run([PYTHON_CMD, SCRIPT_NAME, "0"],
                            capture_output=True,
                            text=True,
                            check=False)
    assert result.stdout.strip(
    ) == "I'm Even.", f"Test 4 Failed: Output was '{result.stdout.strip()}'"


def test_5_non_integer():
    result = subprocess.run([PYTHON_CMD, SCRIPT_NAME, "Hi!"],
                            capture_output=True,
                            text=True,
                            check=False)
    expected_output = "AssertionError: argument is not an integer"
    assert result.stdout.strip(
    ) == expected_output, \
        f"Test 5 Failed: Output was '{result.stdout.strip()}'"


def test_6_multiple_arguments():
    result = subprocess.run([PYTHON_CMD, SCRIPT_NAME, "13", "5"],
                            capture_output=True,
                            text=True,
                            check=False)
    expected_output = "AssertionError: more than one argument is provided"
    assert result.stdout.strip(
    ) == expected_output, \
        f"Test 6 Failed: Output was '{result.stdout.strip()}'"
