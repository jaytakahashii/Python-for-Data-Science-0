#!/bin/bash

PYTHON="python3"
SCRIPT="whatis.py"

echo "===== Running Tests for whatis.py ====="

# 1. No argument
echo -n "Test 1: No argument -> "
OUTPUT=$($PYTHON $SCRIPT)
if [ -z "$OUTPUT" ]; then
    echo "✅ Passed"
else
    echo "❌ Failed (output: '$OUTPUT')"
fi

# 2. Even number
echo -n "Test 2: Even number (14) -> "
OUTPUT=$($PYTHON $SCRIPT 14)
if [ "$OUTPUT" = "I'm Even." ]; then
    echo "✅ Passed"
else
    echo "❌ Failed (output: '$OUTPUT')"
fi

# 3. Odd number
echo -n "Test 3: Odd number (-5) -> "
OUTPUT=$($PYTHON $SCRIPT -5)
if [ "$OUTPUT" = "I'm Odd." ]; then
    echo "✅ Passed"
else
    echo "❌ Failed (output: '$OUTPUT')"
fi

# 4. Zero (special case)
echo -n "Test 4: Zero (0) -> "
OUTPUT=$($PYTHON $SCRIPT 0)
if [ "$OUTPUT" = "I'm Even." ]; then
    echo "✅ Passed"
else
    echo "❌ Failed (output: '$OUTPUT')"
fi

# 5. Non-integer argument
echo -n "Test 5: Non-integer (Hi!) -> "
OUTPUT=$($PYTHON $SCRIPT Hi!)
if [ "$OUTPUT" = "AssertionError: argument is not an integer" ]; then
    echo "✅ Passed"
else
    echo "❌ Failed (output: '$OUTPUT')"
fi

# 6. Multiple arguments
echo -n "Test 6: Two arguments (13 5) -> "
OUTPUT=$($PYTHON $SCRIPT 13 5)
if [ "$OUTPUT" = "AssertionError: more than one argument is provided" ]; then
    echo "✅ Passed"
else
    echo "❌ Failed (output: '$OUTPUT')"
fi

echo "===== Tests Completed ====="
