'''
@Author: Prathamesh Deshpande
@Date:  2024-09-19
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-19
@Title : Python program to implement DFS(Depth First Search).

'''

def dfs(graph, start, visited=None):
    """
    Description:
        Perform Depth First Search (DFS) on a graph starting from a given node.
    
    Parameters:
        - graph: 
            A dictionary representing the graph (adjacency list format).

        - start: 
            The starting node for DFS traversal.

        - visited: 
            A set to keep track of visited nodes (default is None).
    
    Returns:
    -   A set of all visited nodes.

    """
    if visited is None:
        visited = set()

    visited.add(start)
    
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

def main():
    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
    }
    
    dfs(graph, 'A')


if __name__ == "__main__":
    main()
