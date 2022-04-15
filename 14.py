# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.
from math import sqrt
from random import random

def is_in_circle(x_square, y_square, radius) -> bool:
    return sqrt((x_square - radius) ** 2 + (y_square - radius) ** 2) <= radius


def monte_carlo(radius, num_points) -> int:
    hits = 0
    for i in range(num_points):
        x_square = random() * radius ** 2
        y_square = random() * radius ** 2
        if is_in_circle(x_square, y_square, radius):
            hits += 1
    return hits/num_points * (radius*2)**2

if __name__ == '__main__':
    print(monte_carlo(1,1000000))
