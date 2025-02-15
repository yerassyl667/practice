class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def per(self):
        return 2 * (self.width + self.height)
    
class square(rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
class cube(square):
    def __init__(self, side):
        super().__init__(side)

    def volume(self):
        return self.width ** 3
        
        