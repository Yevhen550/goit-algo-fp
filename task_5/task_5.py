import uuid
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import numpy as np


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left = x - 1 / 2**layer
            pos[node.left.id] = (left, y - 1)
            left = add_edges(graph, node.left, pos, x=left, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Tree Visualization"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def generate_color_gradient(n, start_color="#000080", end_color="#ADD8E6"):
    """
    Генерує градієнт кольорів від темного
    до світлого (від start_color до end_color).
    """
    start_rgb = np.array(matplotlib.colors.hex2color(start_color))
    end_rgb = np.array(matplotlib.colors.hex2color(end_color))
    colors = [
        to_hex((1 - i / (n - 1)) * start_rgb + (i / (n - 1)) * end_rgb)
        for i in range(n)
    ]
    return colors


def visualize_traversal(order, traversal_type):
    """
    Візуалізація обходу дерева
    """
    # Генерація градієнта кольорів
    colors = generate_color_gradient(len(order))

    # Присвоєння кольорів вузлам у порядку обходу
    for idx, (node, _) in enumerate(order):
        node.color = colors[idx]
        draw_tree(root, title=f"{traversal_type} Обхід - крок {idx + 1}")


def depth_first_search(root):
    """
    Обхід дерева в глибину (стек)
    """
    stack = [(root, 0)]
    order = []

    while stack:
        node, depth = stack.pop()
        if node:
            order.append((node, depth))
            # Спочатку додаємо правий вузол, щоб лівий був оброблений першим
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

    return order


def breadth_first_search(root):
    """
    Обхід дерева в ширину (черга)
    """
    from collections import deque

    queue = deque([(root, 0)])
    order = []

    while queue:
        node, depth = queue.popleft()
        if node:
            order.append((node, depth))
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

    return order


def build_heap_tree(arr, index=0):
    """
    Рекурсивно будує дерево з бінарної купи,
    представленої у вигляді масиву.
    """
    if index < len(arr):
        node = Node(arr[index])
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(arr):
            node.left = build_heap_tree(arr, left_index)
        if right_index < len(arr):
            node.right = build_heap_tree(arr, right_index)
        return node
    return None


# Побудова дерева з бінарної купи
heap = [10, 5, 8, 3, 2, 7, 6]
root = build_heap_tree(heap)

# Візуалізація обходу в глибину
dfs_order = depth_first_search(root)
visualize_traversal(dfs_order, "Пошук в глибину DFS")

# Відновлення кольорів дерева для нового обходу
root = build_heap_tree(heap)

# Візуалізація обходу в ширину
bfs_order = breadth_first_search(root)
visualize_traversal(bfs_order, "Пошук в ширину BFS")
