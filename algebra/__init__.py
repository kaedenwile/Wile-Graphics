from vec3 import Vec3
from mat3 import Mat3
from vec2 import Vec2

a = Vec3(3, 20, 0)
f = Vec3(0, 2, 0)

print(a)
print(f)

# print(f.length_squared() / f.dot(a))

print(f.dot(a))
print((f*2).dot(a))
print((f*3).dot(a))

exit()
