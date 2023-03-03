# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited_nodes = set()
        total_flipped = 0
        frontier = [0] # used as stack, for smooth DFS jazz
        adjacency_map = self.build_adjacencies(range(n), connections)

        while frontier:
            node = frontier.pop()
            visited_nodes.add(node)

            parents, children = adjacency_map[node]

            unvisited_parents = [parent for parent in parents if parent not in visited_nodes]
            unvisited_children = [child for child in children if child not in visited_nodes]
            # Roads to children need to be flipped
            total_flipped += len(unvisited_children)

            frontier.extend([*unvisited_parents, *unvisited_children])

        return total_flipped
        
    
    def build_adjacencies(self, nodes, edges):
        # Map<int, tuple<parents, children>>
        node_map = { n: ([], []) for n in nodes }
        for edge in edges:
            parent, child = edge
            node_map[parent][1].append(child)
            node_map[child][0].append(parent)
        return node_map
