import vector_cal as vc


v1 = vc.Vector2D(20,30)
v2 = vc.Vector2D(3,30)
v3 = vc.Vector3D(20,30,40)
v4 = vc.Vector3D(3,30,50)
v5 = v1 - v2
v6 = v3 + v4
v7 = list()
# v7.insert(v5, 0)
v7.append(v5)
print(v5)
print(v7)
print(v6)
