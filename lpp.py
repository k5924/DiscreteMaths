import numpy
from matplotlib import pyplot
from matplotlib.path import Path
from matplotlib.patches import PathPatch
# modules used to represent the graphs

fig, axis = pyplot.subplots(figsize=(4.5, 4))
x1 = numpy.linspace(0, 40)

# function definitions for each edge


def edge1():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 2.),
        (3., 0.),
        (0., 0.)])
    return (20 - x1), ((6 - 2 * x1) / 3), bounds, 20
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge2():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 2.),
        (3., 0.),
        (0., 0.)])
    return (10 - x1), ((6 - 2 * x1) / 3), bounds, 10
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge3():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 1.5),
        (4., 0.),
        (0., 0.)])
    return (40 - x1), ((12 - 3 * x1) / 8), bounds, 40
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge4():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 5.),
        (2., 0.),
        (0., 0.)])
    return (15 - x1), ((10 - 5 * x1) / 2), bounds, 15
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge5():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 1.5),
        (3., 0.),
        (0., 0.)])
    return (5 - x1), ((15 - 5 * x1) / 10), bounds, 6
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge6():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 4.),
        (2., 0.),
        (0., 0.)])
    return (20 - x1), ((8 - 4 * x1) / 2), bounds, 20
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge7():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 2.),
        (3., 0.),
        (0., 0.)])
    return (5 - x1), ((6 - 2 * x1) / 3), bounds, 5
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge8():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 3.),
        (1.5, 0.),
        (0., 0.)])
    return (10 - x1), ((9 - 6 * x1) / 3), bounds, 10
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


def edge9():
    # bounds represents boundary of feasible region
    bounds = Path([
        (0., 0.),
        (0., 4.),
        (2., 0.),
        (0., 0.)])
    return (5 - x1), ((8 - 4 * x1) / 2), bounds, 5
    # returns constraint 1, constrain 2, boundary of feasible region and limit2 of axis


edge = int(input('''Enter which edge you would like to see the graph of
1.  LC(1,2)
2.  LC(1,3)
3.  LC(2,3)
4.  LC(2,4)
5.  LC(3,4)
6.  LC(3,5)
7.  LC(4,5)
8.  LC(4,6)
9.  LC(5,6)
'''))
# input to represent each edge in the graph

# if an edge is selected the returned values are assigned to their respective parameters
if edge == 1:
    p1_constraint, p2_constraint, bounds, limit = edge1()
elif edge == 2:
    p1_constraint, p2_constraint, bounds, limit = edge2()
elif edge == 3:
    p1_constraint, p2_constraint, bounds, limit = edge3()
elif edge == 4:
    p1_constraint, p2_constraint, bounds, limit = edge4()
elif edge == 5:
    p1_constraint, p2_constraint, bounds, limit = edge5()
elif edge == 6:
    p1_constraint, p2_constraint, bounds, limit = edge6()
elif edge == 7:
    p1_constraint, p2_constraint, bounds, limit = edge7()
elif edge == 8:
    p1_constraint, p2_constraint, bounds, limit = edge8()
elif edge == 9:
    p1_constraint, p2_constraint, bounds, limit = edge9()

# plot line for p1 and p2 with label as p1 constraint and p2 constraint
pyplot.plot(x1, p1_constraint, linewidth=3, label='P1 constraint')
pyplot.plot(x1, p2_constraint, linewidth=3, label='P2 constraint')

# plot line for x, y >= 0 constraints
pyplot.plot(numpy.zeros_like(x1), x1, linewidth=3, label='$S_1$ Sign restriction')
pyplot.plot(x1, numpy.zeros_like(x1), linewidth=3, label='$S_2$ Sign restriction')

# shades in feasible region on graph
feasible_region = PathPatch(bounds, label='Feasible region', alpha=0.5)
axis.add_patch(feasible_region)

# label axis of graph
pyplot.xlabel('$S_1$')
pyplot.ylabel('$S_2$')

# plot the graphs between -0.1 and the limit given as some graphs dont show x, y>=0 constraint if first limit is 0
pyplot.xlim(-0.1, limit)
pyplot.ylim(-0.1, limit)

# show graph
pyplot.legend()
pyplot.show()

'''
Code i Have used inside of jupyter notebook
from pulp import *

# Example to get solution to maximization and minimization values
# For Minimization define the problem as follows
prob = LpProblem("LC(1,2)", LpMinimize)

# For Maximization define the problem as follows
prob = LpProblem("LC(1,2)", LpMaximize)

s1 = LpVariable("s1", lowBound=0)
s2 = LpVariable("s2", lowBound=0)
prob += 6*s1 + 7*s2
prob += 1*s1 + 1*s2 <= 20
prob += 2*s1 + 3*s2 <= 6
prob
status = prob.solve()
LpStatus[status]
value(s1), value(s2), value(prob.objective)
'''
