'''
@Author: Prathamesh Deshpande
@Date:  2024-09-19
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-19
@Title : Python program to implement BFS(Breadth First Search).

'''

def bfs(graph, start):
    """
    Description:
        Perform Breadth First Search (BFS) on a graph starting from a given node.

    Parameters:
        - graph: 
            A dictionary representing the graph (adjacency list format).

        - start: 
            The starting node for BFS traversal.

    Returns:
    -   A list of all visited nodes in the order they were visited.

    """
    visited = set()   
    queue = [start]   
    result = []       

    visited.add(start)

    while queue:
        node = queue.pop(0)
        result.append(node)
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    bfs(graph, 'A')


if __name__ == "__main__":
    main()
    
