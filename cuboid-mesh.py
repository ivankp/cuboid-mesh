#!/usr/bin/env python

import matplotlib.pyplot as plt

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

vertices_sorted = [ None ] * nv

for v in vertices:
    b  = c[0] < v[0]
    b <<= 1
    b += c[1] < v[1]
    b <<= 1
    b += c[2] < v[2]

    ax.text(*v, f'{b} {b:0>3b}')

    vertices_sorted[b] = v

for v in vertices_sorted:
    print(v)

triangles = [
    ( 0, 1, 2 ),
    ( 2, 1, 3 ),
    ( 4, 6, 5 ),
    ( 5, 6, 7 ),
    ( 0, 2, 4 ),
    ( 4, 2, 6 ),
    ( 1, 5, 3 ),
    ( 3, 5, 7 ),
    ( 0, 4, 1 ),
    ( 1, 4, 5 ),
    ( 2, 3, 6 ),
    ( 6, 3, 7 ),
]

for t in triangles:
    ax.plot(*zip(*(vertices_sorted[i] for i in t)))

plt.axis('off')
plt.show()
