"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.val = start - 1
    
    def generate(self):
        """Creates a new serial number 1 greater than the previous"""
        self.val = self.val + 1
        return self.val
    
    def reset(self):
        """Resets serial number to the start value given"""
        self.val = self.start -1