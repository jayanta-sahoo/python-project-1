## This is a test file in python
import os
def test_function():
    print("This is a test function.")
    assert os.path.exists('.venv'), "Virtual environment does not exist."
    assert os.path.isfile('.venv/test.py'), "Test file does not exist."
    print("All tests passed.")

# new function
def new_function1():
    print("This is a new function in the test file.")
    assert os.path.exists('.venv'), "Virtual environment does not exist."
    assert os.path.isfile('.venv/test.py'), "Test file does not exist."
    print("New function test passed.")

# new function to create
def new_function2():
    print("This is another new function in the test file.")
    assert os.path.exists('.venv'), "Virtual environment does not exist."
    assert os.path.isfile('.venv/test.py'), "Test file does not exist."
    print("Another new function test passed.")

if __name__ == "__main__":
    test_function()
    new_function1()
    new_function2()
    print("All functions executed successfully.")