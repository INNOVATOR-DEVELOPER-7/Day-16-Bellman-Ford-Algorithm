# Day-16-Bellman-Ford-Algorithm
Here's python Program for Bellman Ford Algorithm. Day 16 of Day 365.
- Initial Setup: Start with a graph represented as nodes (vertices) and edges with weights. Choose a starting node (source).
- Distance Initialization: Assign initial distances to all nodes as infinity, except the source node, which is assigned a distance of zero.
- Edge Relaxation: Repeat the following for each edge in the graph (total ( V-1 ) times, where ( V ) is the number of vertices):
  - For each edge (u, v) with weight w:
    - If the distance to u + weight of the edge (u, v) is less than the distance to v:
      - Update the distance to v.
- Check for Negative Cycles: After ( V-1 ) iterations, check for any negative-weight cycles in the graph. If an edge (u, v) can still be relaxed, then the graph contains a negative-weight cycle.

Example:
Graph:

```
    (4)       (2)
  A ----> B ----> C
         |      |
  (1)    |     |(3)
        |      |
      v  v     v v
      D ----> E
         (-3)
```

Starting Node: A

1. Initial Distances: A = 0, B = ∞, C = ∞, D = ∞, E = ∞
2. Relaxation (1st Iteration):
   - Relax edge (A, B, 4): B = 4
   - Relax edge (A, D, 1): D = 1
   - Relax edge (B, C, 2): C = 6
   - Relax edge (B, E, 3): E = 7
   - Relax edge (D, E, -3): E = -2
   - Updated Distances: A = 0, B = 4, C = 6, D = 1, E = -2
3. Relaxation (2nd Iteration):
   - No further updates (all edges already relaxed)
4. Relaxation (3rd Iteration):
   - No further updates
5. Relaxation (4th Iteration):
   - No further updates
6. Check for Negative Cycles:
   - No negative cycles detected

Final Distances: A = 0, B = 4, C = 6, D = 1, E = -2
