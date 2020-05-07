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
        """Initializes a serial number generator to start value"""
        self.start = start
        self.current = start - 1 
       
    def generate(self):
        """Returns next sequential number in the generator"""
        self.current += 1
        return self.current
    
    def reset(self):
        """Resets the serial number generator to the original start value"""
        self.current = self.start - 1
        return None
    
