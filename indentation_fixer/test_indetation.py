import unittest
from indetation_fixer import allow_unindented, execute_unindented_code

class TestIndentationFixer(unittest.TestCase):
    
    def test_execute_unindented_code(self):
        # Test if the unindented code executes correctly
        code = """
a = 5
b = 10
result = a + b
print(result)
"""
        try:
            execute_unindented_code(code)  # Should print 15
        except Exception as e:
            self.fail(f"execute_unindented_code raised an exception: {e}")

    def test_allow_unindented_decorator(self):
        # Define a test function with the decorator
        @allow_unindented
        def test_function():
            return """
x = 3
y = 7
print(x * y)  # Should print 21
"""
        try:
            test_function()  # Should execute without errors
        except Exception as e:
            self.fail(f"allow_unindented raised an exception: {e}")

    def test_invalid_code(self):
        # Test if invalid Python code raises an exception
        code = """
a = 5
if a == 5
print("Missing colon should raise an error")
"""
        with self.assertRaises(SyntaxError):
            execute_unindented_code(code)

if __name__ == "__main__":
    unittest.main()
