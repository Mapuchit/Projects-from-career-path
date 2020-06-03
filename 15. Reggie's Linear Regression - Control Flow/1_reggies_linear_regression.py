 ## Loops project
 ## Reggie's Linear Regression

'''
Reggie is a mad scientist who has been hired by the local fast food joint to build their newest ball pit in the play area.
As such, he is working on researching the bounciness of different balls so as to optimize the pit.
He is running an experiment to bounce different sizes of bouncy balls, and then fitting lines to the data points he records.
He has heard of linear regression, but needs your help to implement a version of linear regression in Python.

Linear Regression is when you have a group of points on a graph, and you find a line that approximately resembles that group of points.
A good Linear Regression algorithm minimizes the error_, or the distance from each point to the line. A line with the least error is the line that fits the data the best.
We call this a line of _best fit.
We will use loops, lists, and arithmetic to create a function that will find a line of best fit when given a set of data.
'''

 ## Calculating Error

# The line we will end up with will have a formula that looks like: y = m * x + b.
# m is the slope of the line and b is the intercept, where the line crosses the y-axis.

# A function that returns what the y value would be for that x on that line!
def get_y(m, b, x):
  return m * x + b

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

# A function that calculates the error between a point and a line.
# It takes in m, b, and an [x, y] point called point and returns the distance between the line and the point.
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    # get the y-value that x_point would be on the line
    # and find the difference between the y from get_y and y_point
    distance = get_y(m, b, x_point) - y_point
    return abs(distance)

# The distance represents the error between the line y = m*x + b and the point given.

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))

# Reggie's datasets will be sets of points.
# He ran an experiment comparing the width of bouncy balls to how high they bounce:
# The first datapoint, (1, 2), means that his 1cm bouncy ball bounced 2 meters. The 4cm bouncy ball bounced 4 meters.
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

# To fit a line through these points we need:
# A function that takes m and b that describe a line, and points, a set of data like the example above,
# and returns the total error after calculating the errors for each data point in the dataset and adding them up.
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

# We have a function that can take in a line and Reggie's data and return how much error that line produces when we try to fit it to the data.
# Our next step is to find the m and b that minimizes this error, and thus fits the data best!

 ## Try a bunch of slopes and intercepts!

# Reggie wants to try a bunch of different slopes (m values) and a bunch of different intercepts (b values)
# and see which one produces the smallest error value for his dataset.

# create a list of possible m values to try that goes from -10 to 10 inclusive, in increments of 0.1
possible_ms = [i * 0.1 for i in range(-100, 101)]

# create a list of possible b values to try that would be the values from -20 to 20 inclusive, in steps of 0.1
possible_bs = [i * 0.1 for i in range(-200, 201)]

# We are going to find the smallest error.
# First, we will make every possible y = m * x + b line by pairing all of the possible ms with all of the possible bs.
# Then, we will see which y = m*x + b line produces the smallest total error with the set of data stored in datapoint.

# create the variables
smallest_error = float("inf") # this should start at infinity (float("inf")) so that any error we get at first will be smaller than our value of smallest_error
best_m = 0
best_b = 0

# Reggie's data
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

# iterate through the bs and ms
for m in possible_ms:
    for b in possible_bs:
        current_error = calculate_all_error(m, b, datapoints)
        if current_error < smallest_error:
            # update the variables with the values that give the smallest error
            best_m = m
            best_b = b
            smallest_error = current_error

print(best_m)
print(best_b)
print(smallest_error)

 ## What does our model predict?

# Now we have seen that for this set of observations on the bouncy balls, the line that fits the data best has an m of 0.3 and a b of 1.7:
# y = 0.3x + 1.7

# Using this m and this we can predict the bounce height of balls with different widths: 6cm, 12cm etc.
print(get_y(0.3, 1.7, 6))
print(get_y(0.3, 1.7, 12))
print(get_y(0.3, 1.7, 3))
print(get_y(0.3, 1.7, 1))
print(get_y(0.3, 1.7, 0.5))
