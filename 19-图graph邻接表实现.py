"""
graph = {
    'A' : ['B', 'C'],
    'B' : ['A'],
    'C' : ['A']
}
"""
class Graph:
    def __init__(self):
        self.graph = {}
    # 添加节点
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    # 添加边 node1 <-> node2
    def add_edge(self, node1, node2, driected=False):
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)
            if not driected and node1 not in self.graph[node1]: # 无向图
                self.graph[node2].append(node1)

    # 删除边
    def remove_edge(self, node1, node2, driected=False):
        if node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
        if not driected and node1 in self.graph[node2]:
            self.graph[node2].remove(node1)

    # 删除节及其所有边
    def remove_node(self, node):
        if node in self.graph:
            for neighbor in self.graph[node]:
                self.remove_edge(neighbor, node)
            del self.graph[node]
    
    # 深度优先搜索
    def dfs(self, start_node):
        visited = set() # 记录已遍历的节点
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(f"'{node}'", end=' ')
            
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        print()
    # 广度优先搜索bfs
    def bfs(self, start_node):
        visited = set() # 记录已遍历的节点
        queue = [start_node]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(f"'{node}'", end=' ')
            
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    # 打印图
    def print_graph(self):
        for node in self.graph:
            print(f"'{node}' : {self.graph[node]}")
        print()

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.print_graph()
g.dfs('B')
g.bfs('B')
print()

g.remove_edge('C', 'A')
g.print_graph()
g.remove_node('C')
g.print_graph()
g.dfs('B')
g.bfs('B')