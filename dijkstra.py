# source is a pair of numbers representing position of node
def dijkstra(graph, source, destination):
    # a set
    q = set()
    dist = {}
    prev = {}
    # this returns a list of all the keys
    for v in graph.keys():
        # adding to a set
        q.add(v)
        dist[v] = 1e9
        prev[v] = None

    dist[source] = 0

    while len(q) > 0:
        u = None
        shortest_distance = 1e9
        for vertex in q:
            if dist[vertex] < shortest_distance:
                u = vertex
                shortest_distance = dist[vertex]

        q.remove(u)

        if u == destination:
            path = []
            while prev[u] != None:
                path.insert(0,u)
                u = prev[u]
            return path

        # 16 - 20
        for vertex in graph[u]:
            alt = dist[u]+1
            if alt < dist[vertex]:
                dist[vertex] = alt
                prev[vertex] = u

    # print(dist)
    # print(prev)

# dist is a dictionary where the key is the node coordinates and the value is the number of steps from the source.
# prev is a dictionary where the key is the node coordinates and the value is the previous node in the path
