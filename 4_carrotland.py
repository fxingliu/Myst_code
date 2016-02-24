# def answer(vertices):
#     # your code here
#     minx = min(i[0] for i in vertices)
#     maxx = max(i[0] for i in vertices)
#     miny = min(i[1] for i in vertices)
#     maxy = max(i[1] for i in vertices)
    
#     count = 0
#     a, b, c = vertices[:]
#     for x in xrange(minx+1, maxx):
#         last = False
#         for y in xrange(miny+1, maxy):
#             if inside(a, b, c, [x, y]):
#                 count += 1
#                 last = True
#             elif last:
#                 break
#     return count
    
# # decide if p is in triangle abc
# def inside(a, b, c, p):
#     bc = (c[0]-b[0], c[1]-b[1])
#     ac = (c[0]-a[0], c[1]-a[1])
#     ab = (b[0]-a[0], b[1]-a[1])
#     pa = (a[0]-p[0], a[1]-p[1])
#     pb = (b[0]-p[0], b[1]-p[1])
#     ba = (-ab[0], -ab[1])
#     ca = (-ac[0], -ac[1])
    
#     if cross(ab, bc) * cross(pb, bc) <= 0: return False
#     if cross(ba, ac) * cross(pa, ac) <= 0: return False
#     return cross(ca, ab) * cross(pa, ab) > 0
    
# # cross product
# def cross(x, y):
#     return x[0]*y[1] - x[1]*y[0]


# assert(inside([-1, -1], [1, 0], [0, 1], [0, 0]) is True)


# the above solution is very time inefficient
# consider using Pick's Theorem
# http://stackoverflow.com/questions/1049409/how-many-integer-points-within-the-three-points-forming-a-triangle

from fractions import gcd

def answer(vertices):
    # your code here
    edge = get_edge(vertices)
    boundary_point = get_bp(edge)
    area = get_area(edge)
    return int(area + 1 - boundary_point / 2)

def get_edge(v):
	return [[v[0][0]-v[1][0], v[0][1]-v[1][1]], [v[1][0]-v[2][0], v[1][1]-v[2][1]], [v[2][0]-v[0][0], v[2][1]-v[0][1]]]

def get_bp(edge):
	sum = 0
	for e in edge:
		sum += gcd(abs(e[0]), abs(e[1]))
	return sum

def get_area(edge):
	return abs(edge[0][0]*edge[1][1]-edge[1][0]*edge[0][1]) / 2.



assert(get_edge([[-1, -1], [1, 0], [0, 1]]) == [[-2, -1], [1, -1], [1, 2]])

assert(get_bp([[-1, -1], [1, 0], [0, 1]]) == 3)

assert(get_area([[-2, -1], [1, -1], [1, 2]]) == 1.5)

assert(answer([[-1, -1], [1, 0], [0, 1]]) == 1)
assert(answer([[2, 3], [6, 9], [10, 160]]) == 289)
assert(answer([[91207, 89566], [-88690, -83026], [67100, 47194]]) == 1730960165)