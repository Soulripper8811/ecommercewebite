graph1={
    'A':set(['B','C']),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B','F']),
    'F':set(['C','E'])
}

def Bfs(graph,start):
    visisted=set()
    queue=[start]
    while queue:
        node=queue.pop()

        if node not  in visisted:
            print(node,end=" ")
            visisted.add(node)
            for n in graph[node]:
                if n not in visisted:
                    queue.append(n)

Bfs(graph1,'A')