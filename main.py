# Integrating functions by estimating area under curve
# Defining polynomial functions
def f(x):
    y = (x ** 3) + 1
    return y
def g(x):
    y = (3 * (x ** 3)) + (2 * ( x ** 2)) - (6 * x) + 5
    return y
def h(x):
    y = (2 * (x ** 3)) - (x **2) + (3 * x) - 2
    return y
# Function for choosing one of the polynomials above
def pick_func():

    print('Which function do you want?')
    print('Function 1: x^3 - 1, Function 2: 2x^3 + 2x^2 - 5x + 3, Function 3: 3x^3 - x^2 + 2x - 1')
    try:
        choice = int(input('Enter your choice (1,2,3): '))
    except:
        print('You have entered a point or a letter. Please enter an integer.')
        choice = int(input('Enter your choice (1,2,3): '))
    if choice == 1:
        func = f
    elif choice == 2:
        func = g
    elif choice == 3:
        func = h
    return func
# User defined interval
def interval():

    lower = float(input('Please enter lower bound of interval: '))
    upper = float(input('Please enter upper bound of interval: '))
    return lower, upper
# Under estimating integral with rectangles
def left_sum(func, lower, upper):
    intervals = 10
    error = 100000
    prev_area = 0
    while abs(error) > 1e-6:
        width = (upper - lower) / intervals
        area = 0
        for i in range(intervals):
            area += width * func(lower + (width * i))
        intervals += 1
        error = area - prev_area
        prev_area = area
    return area
# Over estimating integral with rectangles
def right_sum(func, lower, upper):
    intervals = 10
    error = 100000
    prev_area = 0
    while abs(error) > 1e-6:
        width = (upper - lower) / intervals
        area = 0
        for i in range(intervals):
            area += width * func((lower + width) + (width * i))
        intervals += 1
        error = area - prev_area
        prev_area = area
    return area
# More accurate estimation using rectangles at midpoint of intervals
def mid_sum(func, lower, upper):
    intervals = 10
    error = 100000
    prev_area = 0
    while abs(error) > 1e-6:
        width = (upper - lower) / intervals
        area = 0
        for i in range(intervals):
            area += width * func(((lower + width) / 2) + (width * i))
        intervals += 1
        error = area - prev_area
        prev_area = area
    return area
# Even more accurate estimation using trapezoids for intervals
def trapezoid_sum(func, lower, upper):
    intervals = 10
    error = 100000
    prev_area = 0
    while abs(error) > 1e-6:
        width = (upper - lower) / intervals
        area = 0
        for i in range(intervals):
            area += width * func((lower + (width * i) + (lower + (width * (i + 1)))) * 0.5)
        intervals += 1
        error = area - prev_area
        prev_area = area
    return area
# Use functions to determine area
func = pick_func()
lower, upper = interval()
beginning_integral = left_sum(func, lower, upper)
end_integral = right_sum(func, lower, upper)
midpoint_integral = mid_sum(func, lower, upper)
trapezoid_integral = trapezoid_sum(func, lower, upper)
# Print output
print('Shape 1 area: %.3f'%beginning_integral)
print('Shape 2 area: %.3f'%end_integral)
print('Shape 3 area: %.3f'%midpoint_integral)
print('Shape 4 area: %.3f'%trapezoid_integral)