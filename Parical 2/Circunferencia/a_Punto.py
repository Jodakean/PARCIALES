
class Punto:
    
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
    
    def get_X(self):
        return self.coord_x
    
    def set_X(self, x):
        self.coord_x = x
    
    def get_Y(self):
        return self.coord_y
    
    def set_Y(self, y):
        self.coord_y = y