graph1={
    'A':set(['B','C']),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B','F']),
    'F':set(['C','E'])
}


def Dfs(graph,node,visisted):
    if node not in visisted:
        visisted.append(node)
        for n in graph[node]:
            Dfs(graph,n,visisted)
        return visisted

visisted=Dfs(graph1,'A',[])
print(visisted)