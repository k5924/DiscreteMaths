import pandas
from matplotlib import pyplot
import seaborn
# import pandas to read in csv and import matplotlib and seaborn for pdf and histogram
file = 'path pdf.csv'
choice = int(input("Would you like to see the PDF of the:\n1.\tUndirected graph\n2.\tDirected graph\n> "))
if choice == 1:
    title = "Undirected Graph PDF"
    column = 0
    bins = 22
else:
    title = "Directed Graph PDF"
    column = 1
    bins = 17
# user chooses the title and column in the csv file
ds = pandas.read_csv(file, usecols=[column])
# choose the data set from the column in the csv file
seaborn.distplot(ds, bins=bins, hist=True, kde=True,
                 hist_kws={'edgecolor': 'black'}, kde_kws={'linewidth': 4})
# plot the histogram and pdf with seaborn
pyplot.title(title)
pyplot.ylabel('Density')
pyplot.xlabel('Cost')
# give the figure a title and labels on the axis
pyplot.show()
# show the graph
