import pytest
import subprocess
import sys

SCRIPT_PATH = "filterstring.py"
PYTHON_EXECUTABLE = sys.executable

test_cases = [
    (['Hello the World', '4'], "['Hello', 'World']\n"),
    (['Hello the World', '99'], "[]\n"),
]

error_cases = [
    (['3', 'Hello the World']),
    ([]),
]


@pytest.mark.parametrize("args, expected_output", test_cases)
def test_normal_output(args, expected_output):
    command = [PYTHON_EXECUTABLE, SCRIPT_PATH] + args

    result = subprocess.run(
        command, capture_output=True, text=True, check=False)

    # check that the process exited successfully
    assert result.returncode == 0, \
        f"Process exited with error code {result.returncode}.\
            Stderr: {result.stderr}"

    # check that the standard output matches the expected output
    assert result.stdout == expected_output, \
        f"Unexpected stdout. Actual: {result.stdout!r},\
            Expected: {expected_output!r}"


@pytest.mark.parametrize("args", error_cases)
def test_error_handling(args):
    command = [PYTHON_EXECUTABLE, SCRIPT_PATH] + args
    expected_error_message = "AssertionError: the arguments are bad"

    result = subprocess.run(
        command, capture_output=True, text=True, check=False)

    # check that the process exited with a non-zero (error) code
    assert result.returncode != 0, \
        f"Process should have failed but exited with return code 0. \
            Stdout: {result.stdout}"

    # check that the expected error message is in stderr or stdout
    full_output = result.stdout + result.stderr
    assert expected_error_message in full_output, \
        f"Missing error message. Output: {full_output}"
