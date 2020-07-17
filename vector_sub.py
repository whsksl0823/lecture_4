class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def sub(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

v1 = Vector3D(10, 20, 30)
v2 = Vector3D(30, 40, 50)
v3 = v1.sub(v2)
v4 = v1 - v2
#특수 메소드 없이 연산
print(v3)

#특수 메소드(__sub__) 사용하면 연산이 가능
print(v4)