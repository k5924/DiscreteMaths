from statistics import stdev, variance
# import modules for standard deviation and variance
from matplotlib import pyplot
import numpy
from scipy import stats
import csv
import pandas
# import modules for boxplot, gaussian distribution and probability density function


def sort(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                # if the ith value is greater than the jth value
                list[j], list[i] = list[i], list[j]
                # swap there places
    mean = 0
    for i in list:
        mean += i
    mean /= len(list)
    return mean, list


# to store cost of each path
choice = int(input(
    "Do you want the solution for the undirected or directed graph\n1.\tUndirected\n2.\tDirected\n> "))
list1 = []
list2 = []
with open('cartesian file.csv', encoding='utf-8-sig') as file:
    count = 0
    for row in csv.reader(file, delimiter=','):
        for value in row:
            if count == 0:
                if value != '':
                    if value == '105':
                        count += 1
                    list1.append(int(value))
            else:
                if value != '':
                    list2.append(int(value))
if choice == 1:
    mean, list = sort(list1)
    print("For the unidrected graph\n")
else:
    mean, list = sort(list2)
    print("For the directed graph\n")

print("\nThe sorted list is {}\n".format(list))
# print the list when its sorted

if len(list) % 2 == 0:
    m1 = len(list) / 2
    m1 = int(m1)
    middle = (list[m1 - 1] + list[m1]) / 2
    # get middle of list
    first1 = int(len(list) / 4)
    first_quartile = (list[first1] + list[first1 - 1]) / 2
    # get first quartile value
    third1 = int(first1 * 3)
    third_quartile = (list[third1] + list[third1 - 1]) / 2
    # get third quartile value
    iqr = third_quartile - first_quartile
    # get iqr
else:
    mid = len(list) / 2
    middle = list[int(mid) - 1]
    # get middle of list
    first_quartile = int(len(list) / 4)
    third_quartile = int(first_quartile * 3)
    first_quartile = list[first_quartile]
    # get first quartile value
    third_quartile = list[third_quartile]
    # get third quartile value
    iqr = third_quartile - first_quartile
    # get iqr

print("The mean is {}\nThe median is {}\nThe standard deviation is {}\nThe variance is {}\n".format(
    mean, middle, stdev(list), variance(list)))
print("The 1st quartile is {}\nThe 3rd quartile is {}\nThe IQR is {}\n".format(
    first_quartile, third_quartile, iqr))
# print information about the data sets

df = pandas.DataFrame([list], index=['Cost'])
df.T.boxplot(vert=False)
pyplot.subplots_adjust(left=0.25)
pyplot.show()
# plots the box plot for the data sets

sigma = stdev(list)
# get standard deviation
x = numpy.linspace(mean - 3 * sigma, mean + 3 * sigma, 100)
pyplot.plot(x, stats.norm.pdf(x, mean, sigma))
pyplot.show()
# plot gaussian distribution
