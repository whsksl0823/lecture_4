class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    # def lt(self, other):
    #     return Vector3D(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return Vector2D(self.x < other.x, self.y < other.y)

v1 = Vector2D(10, 20)
v2 = Vector2D(30, 10)
v3 = (v1 < v2)

#특수 메소드(__lt__) 사용하면 연산이 가능
print(v3)