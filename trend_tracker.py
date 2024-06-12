import matplotlib.pyplot as plt
from scipy import stats


# returns the list with arithmetic progression [0, 1, 2 ... length-1]
def generate_linear_progression(length):
    return [i for i in range(length)]


# calculates list of linear regression line points coordinates
def calculate_line_dot(slope, intercept, x):
    return [slope * x_element + intercept for x_element in x]


def calculate_regression(x, y, plot_title, line_color):
    # linear regression calculation
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    # linear regression results printed
    print(f'{plot_title}')
    print(f'x: {x}')
    print(f'y: {y}')
    print(f'slope: {slope}, intercept: {intercept}')
    print(f'r: {r}, p: {p}, std_err: {std_err}')
    print(f'***')
    # define model to show the line found with linear regression on chart
    mymodel = calculate_line_dot(slope, intercept, x)
    # creates new plot
    plt.figure()
    # showing the plot with input time series and linear regression line
    plt.title(plot_title)
    # plots the original time series
    plt.scatter(x, y)
    # plots the line calculated with linear regression
    plt.plot(x, mymodel, color=line_color)


def process_weak_down_trend():
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 105]
    x = generate_linear_progression(len(y))
    calculate_regression(x, y, "Weak downward trend (no trend)", 'orange')


def process_strong_down_trend():
    y = [73, 65, 67, 54, 57, 59, 53, 41, 48, 44, 43, 49]
    x = generate_linear_progression(len(y))
    calculate_regression(x, y, "Strong downward trend", 'red')


def process_strong_up_trend():
    y = [16, 14, 16, 19, 17, 16, 21, 24, 23, 22, 25, 20]
    x = generate_linear_progression(len(y))
    calculate_regression(x, y, "Strong upward trend", 'green')


process_strong_up_trend()
process_strong_down_trend()
process_weak_down_trend()

plt.show()