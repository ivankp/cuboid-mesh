#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

vertices = [
    ( 0, 0, 0 ),
    ( 1, 0, 0 ),
    ( 0, 1, 0 ),
    ( 1, 1, 0 ),
    ( 0, 0, 1 ),
    ( 1, 0, 1 ),
    ( 0, 1, 1 ),
    ( 1, 1, 1 )
]
nv = len(vertices)

ax.scatter(*zip(*vertices), marker='o')

c = [ 0, 0, 0 ]
for v in vertices:
    c[0] += v[0]
    c[1] += v[1]
    c[2] += v[2]

c[0] /= nv
c[1] /= nv
c[2] /= nv
print(c)
print()

vertices_sorted = [ None ] * nv

for v in vertices:
    b  = c[2] < v[2]
    b <<= 1
    b += c[1] < v[1]
    b <<= 1
    b += c[0] < v[0]

    ax.text(*v, f'  {b} {b:0>3b}')

    vertices_sorted[b] = np.array(v)

for v in vertices_sorted:
    print(v)
print()

# triangles = [
#     ( 2, 1, 0 ),
#     ( 1, 2, 3 ),
#     ( 0, 1, 5 ),
#     ( 0, 5, 4 ),
#     ( 1, 3, 7 ),
#     ( 1, 7, 5 ),
#     ( 3, 2, 6 ),
#     ( 3, 6, 7 ),
#     ( 2, 0, 4 ),
#     ( 2, 4, 6 ),
#     ( 4, 5, 7 ),
#     ( 4, 7, 6 )
# ]

triangles = [ None ] * 12
b = 0
for i in range(1,7):
    b += 3 if b < 4 else -4
    triangles[i - 1] = ( i, b, 0 )
    triangles[i + 5] = ( abs(b - 7), abs(i - 7), 7 )

for t in triangles:
    print(t)
    c = sum( vertices_sorted[t[i]] for i in range(3) ) / 3
    t = ( *t, t[0] )
    ax.plot(*zip(*((vertices_sorted[i] - c)*0.95 + c for i in t)), color='#009')
print()

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(12, -105, 2)

# plt.axis('off')
plt.show()
