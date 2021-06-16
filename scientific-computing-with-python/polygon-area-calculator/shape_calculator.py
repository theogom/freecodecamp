

class Rectangle:
    """
    A class representing a rectangle
    with given width and height
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width: int) -> None:
        """
        Set the Rectangle width
        """
        self.width = width

    def set_height(self, height: int) -> None:
        """
        Set the Rectangle width
        """
        self.height = height

    def get_area(self) -> int:
        """
        Get the Rectangle area
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """
        Get the Rectangle perimeter
        """
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        """
        Get the length of the Rectangle diagonals
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        """
        Draw the shape of the Rectangle using '*' characters
        Width and height of the Rectangle should be both less or equal than 50
        """
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        return '\n'.join(('*' * self.width for _ in range(self.height))) + '\n'

    def get_amount_inside(self, shape: 'Rectangle|Square') -> int:
        """
        Get the amount of `shape` that could fit in the current Rectangle
        """
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    """
    A class representing a square
    """

    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def __str__(self) -> str:
        return f'Square(side={self.width})'

    def set_side(self, side: int) -> None:
        """
        Set the side of the Square
        """
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width: int) -> None:
        """
        Set the width of the Square
        """
        self.set_side(width)

    def set_height(self, height: int) -> None:
        """
        Set the height of the Square
        """
        self.set_side(height)
