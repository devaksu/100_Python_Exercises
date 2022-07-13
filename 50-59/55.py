"""
Define a custom exception class which takes a string message as attribute.
"""

class CustomException(Exception):
    """
    Custom exception class.
    """

    def __init__(self, message:str, value:int=404):
        self.message = message
        self.value = value


error = CustomException("Oops something went wrong!")

print(error)
print(error.value)
