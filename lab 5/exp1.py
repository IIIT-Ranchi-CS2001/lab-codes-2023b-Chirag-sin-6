import math

point1 = (3, 5, 7)
point2 = (1, 1, 1)

distance =  math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

print(f"The Euclidean distance between the points is: {distance}")