INFINITY = 9999999
# maximum weight
graph = {'a': {'b': 18, 'c': 9}, 'b': {'a': 18, 'c': 8, 'd': 40}, 'c': {'a': 9, 'b': 8, 'd': 12, 'e': 12},
         'd': {'b': 40, 'c': 12, 'e': 12, 'f': 9}, 'e': {'c': 12, 'd': 12, 'f': 36}, 'f': {'d': 9, 'e': 36}}
# all connections on the graph
totalCost = {}
parentNodes = {}
route = []
for node in graph:
    totalCost[node] = INFINITY
totalCost['a'] = 0
# initialises total cost of each node
while graph:
    smallest = None
    for node in graph:
        if smallest is None:
            smallest = node
        elif totalCost[node] < totalCost[smallest]:
            smallest = node
        # changes smallest node to the current node in the list
    for childNode, cost in graph[smallest].items():
        if cost + totalCost[smallest] < totalCost[childNode]:
            totalCost[childNode] = cost + totalCost[smallest]
            parentNodes[childNode] = smallest
        # append nodes to parentnodes dictionary, update values in total cost dictionary
    graph.pop(smallest)
    # remove smallest node from graph in each loop
currentNode = 'f'
while currentNode != 'a':
    try:
        route.insert(0, currentNode)
        currentNode = parentNodes[currentNode]
        # try to make a route from the parentNodes dictionary to the currentNode
    except KeyError:
        print('Path not reachable')
        break
        # print message when route isnt possible
route.insert(0, 'a')
if totalCost['f'] != INFINITY:
    print(
        "The shorest route from C1-C6 represented with a-f respectively is {} has total cost {}".format(route, totalCost['f']))
    # print the shortest route and how to get there
