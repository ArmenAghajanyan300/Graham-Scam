
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise


def convex_hull(points):

    points = sorted(points)
    lowest_point = points[0]


    def polar_angle(p):

        return (p[1] - lowest_point[1], p[0] - lowest_point[0])

    sorted_points = sorted(points[1:], key=polar_angle)

  
  
    stack = [lowest_point, sorted_points[0]]


    for i in range(1, len(sorted_points)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])

    return stack

# Example usage
points = [(0, 0), (1, 1), (2, 2), (2, 1), (1, 0), (3, 3)]
hull = convex_hull(points)

print("Convex Hull points:")
for point in hull:
    print(point)
