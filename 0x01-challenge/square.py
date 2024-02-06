#!/usr/bin/python3

class Square:
    """
    A class representing a square shape.
    
    Attributes:
    - side: The side length of the square.
    """

    def __init__(self, side=0):
        """
        Initializes a square with the given side length.
        
        Args:
        - side: The side length of the square.
        """
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("Side length must be non-negative")
        self._side = value

    @property
    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
        The area of the square.
        """
        return self.side ** 2

    @property
    def perimeter(self):
        """
        Calculates the perimeter of the square.
        
        Returns:
        The perimeter of the square.
        """
        return self.side * 4

    def __str__(self):
        """
        Returns a string representation of the square.
        
        Returns:
        A string representation of the square in the format 'side_length'.
        """
        return str(self.side)

if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print("Area:", s.area)
    print("Perimeter:", s.perimeter)
