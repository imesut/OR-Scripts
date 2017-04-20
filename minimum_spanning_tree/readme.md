# Minimum Spanning Tree Script

**Definition:** A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight. [[Wikipedia](https://en.wikipedia.org/wiki/Minimum_spanning_tree)]

![A spanning tree example form Wikimedia](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Minimum_spanning_tree.svg/350px-Minimum_spanning_tree.svg.png)

Script starts with ```cnk``` array. Each node is entered to this array. This array also named ad "unconnected nodes" as literature.

```
cnk = ["0", "A", "B", "C", "D", "E", "T"]
```

Each arc(edge) is described via its nodes and weight as ```item = [from, to, weight]```

Full example is:

```
arcs = [
["0", "A", 2], ["0", "C", 4], ["0", "B", 5],
["A", "B", 2], ["A", "D", 7], ["B", "C", 1],
["B", "D", 4], ["B", "E", 3], ["D", "E", 1],
["D", "T", 5], ["E", "T", 7], ["C", "E", 4]
]
```

