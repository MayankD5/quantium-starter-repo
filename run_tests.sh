#!/bin/bash

# Activate virtual environment (Windows Git Bash)
source venv/Scripts/activate

# Run tests
pytest

# Return exit code
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi