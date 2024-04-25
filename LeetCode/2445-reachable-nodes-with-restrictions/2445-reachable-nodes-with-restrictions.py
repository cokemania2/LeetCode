# 엣지들을 딕셔너리에 매핑 한 후 갯수를 카운트한다.
# 카운트 하는 방식은 DFS를 이용한다.

from typing import Dict
from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        edge_dict: Dict[int, int] = defaultdict(list)
        visited_nodes: list[bool] = [False for _ in range(n)]
        restricted = set(restricted)
        for edge in edges:
            if edge[1] not in restricted:
                edge_dict[edge[0]].append(edge[1])
            if edge[0] not in restricted:
                edge_dict[edge[1]].append(edge[0])
        return self._count_nodes(0, edge_dict, visited_nodes)

    def _count_nodes(self, node_number: int, edge_dict: Dict[int, int], visited_nodes:list[bool]) -> int:
        count = 1
        
        visited_nodes[node_number] = True
        edge_list = edge_dict[node_number]        
        for edge in edge_list:
            if visited_nodes[edge]:
                continue
            count += self._count_nodes(edge, edge_dict, visited_nodes)
        return count
