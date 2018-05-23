from vec3 import Vec3
from mat3 import Mat3
from vec2 import Vec2

import time

start = time.time()

value = Mat3([
    2, 2, 2,
    8, 2, 64,
    2, 2, 8
])

starting = Mat3([
    2, 2, 2,
    8, 2, 64,
    2, 2, 8
])

for i in xrange(100000):
    value = value * starting

dur = time.time() - start
print(value)
print(dur)

start = time.time()
val = pow(18, 100000)
dur = time.time() - start
print(val)
print(dur)

exit()
