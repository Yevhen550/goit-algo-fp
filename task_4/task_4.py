import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


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


# Приклад бінарної купи у вигляді масиву
heap = [10, 5, 8, 3, 2, 7, 6]

# Побудова дерева з бінарної купи
heap_tree_root = build_heap_tree(heap)

# Відображення дерева
draw_tree(heap_tree_root)
