class Rectangle:
    
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width: int) -> None:
        self.width = width
        
    def set_height(self, height: int) -> None:
        self.height = height
        
    def get_area(self) -> int:
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self) -> str:
        result = str()
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for _ in range(self.height):
            result += f"{''.join(['*' for __ in range(self.width)])}\n"
        return result
    
    def get_amount_inside(self, shape: "Rectangle") -> int:
        w = self.width // shape.width
        h = self.height // shape.height
        return w * h

class Square(Rectangle):
    
    def __init__(self, side: int) -> None:
        super().__init__(side, side)
        
    def __str__(self) -> str:
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)
        
    def set_height(self, height: int) -> None:
        self.set_side(height)
        
    def set_width(self, width: int) -> None:
        self.set_side(width)

if __name__=="__main__":
    rect = Rectangle(5, 10)
    print(rect.get_area())
    rect.set_width(3)
    print(rect.get_perimeter())
    print(rect)

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)