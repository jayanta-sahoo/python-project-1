## This is a test file in python
import os
def test_function():
    print("This is a test function.")
    assert os.path.exists('.venv'), "Virtual environment does not exist."
    assert os.path.isfile('.venv/test.py'), "Test file does not exist."
    print("All tests passed.")

# add new function
def new_function():
    print("This is a new function added to the test file.")
    return "New function executed successfully."