import math


class Vector:
   dimension: float = 0
   direction: float = 0
   x: float = 0
   y: float = 0

   def __init__(self, dimension: float, direction: float) -> None:
      self.dimension = dimension
      self.direction = direction

      rad_direction = math.radians(direction)
      self.x = dimension * math.cos(rad_direction)
      self.y = dimension * math.sin(rad_direction)

   def __str__(self) -> str:
      return "Vector (dimension=%.2f, direction=%.2f°)" % (self.dimension, self.direction) + " (x=%.2f, y=%.2f)" % (self.x, self.y)

   def __add__(self, other):
      xR: float = self.x + other.x
      yR: float = self.y + other.y

      dimensionR: float = math.sqrt((xR * xR) + (yR * yR))
      directionR: float = math.degrees(math.atan(yR / xR))

      return Vector(dimensionR, directionR)


v1 = Vector(10, 20)
v2 = Vector(30, 90)

print(v1)
print(v2)
print(v1 + v2)