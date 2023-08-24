import numpy as np

"""
Bounds class represents the bounds of a node in PRQuadtree
    - min_x: (float) minimum x coordinate of the bounds
    - min_y: (float) minimum y coordinate of the bounds
    - max_x: (float) maximum x coordinate of the bounds
    - max_y: (float) maximum y coordinate of the bounds
"""
class Bounds:
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    # Retorna el ancho de los límites
    @property
    def width(self):
        return self.max_x - self.min_x

    # Retorna la altura de los límites
    @property
    def height(self):
        return self.max_y - self.min_y
    
    # Retorna el centro de los límites
    #  - return: (np.array) centro de los límites
    @property
    def center(self):
        center_x = (self.min_x + self.max_x) / 2
        center_y = (self.min_y + self.max_y) / 2
        return np.array([center_x, center_y])

    # Retorna True si el punto está dentro de los límites
    #   - point : (np.array) punto a verificar
    #   - return:     (bool) True: si el punto está dentro de los límites
    def contains(self, point):
        if self.min_x <= point[0] and point[0] <= self.max_x:
            return True
        if self.min_y <= point[1] and point[1] <= self.max_y:
            return True
        return False

    # Retorna True si el círculo se intersecta con los límites
    #   - center: (np.array) centro del círculo
    #   - radius:    (float) radio del círculo
    #   - return:     (bool) True: si el círculo se intersecta con los límites
    def intersects_circle(self, center, radius):
        closest_x = max(self.min_x, min(center[0], self.max_x))
        closest_y = max(self.min_y, min(center[1], self.max_y))
        
        distance_x = center[0] - closest_x
        distance_y = center[1] - closest_y
        distance_squared = distance_x**2 + distance_y**2
        
        if distance_squared <= radius**2:
            return True
        return False
    
    # Retorna True si los límites contienen a otro bounds
    #   - other_bounds: (Bounds) límites a verificar
    #   - return      :   (bool) True: si los límites contienen a otro bounds
    def contains_bounds(self, other_bounds):
        if self.min_x <= other_bounds.min_x and self.min_y <= other_bounds.min_y and self.max_x >= other_bounds.max_x and self.max_y >= other_bounds.max_y:
            return True
        return False
