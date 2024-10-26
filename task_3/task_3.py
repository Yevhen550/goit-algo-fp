import heapq
from collections import defaultdict
import math


class Graph:
    def __init__(self):
        # Створюємо порожній граф, де кожна вершина
        # пов'язана зі списком пар (сусід, вага)
        self.graph = defaultdict(list)
        self.vertices = set()  # Множина для збереження всіх вершин

    def add_edge(self, u, v, weight):
        # Додаємо орієнтоване ребро з вершини u в v з вагою weight
        self.graph[u].append((v, weight))
        # Додаємо вершини до множини
        self.vertices.add(u)
        self.vertices.add(v)

    def dijkstra(self, start):
        # Встановлюємо відстані до всіх вершин як нескінченність
        distances = {vertex: math.inf for vertex in self.vertices}
        distances[start] = 0

        # Мін-купа для зберігання вершин та поточної відстані до них
        priority_queue = [(0, start)]  # (distance, vertex)

        while priority_queue:
            # Витягуємо вершину з мінімальною відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо знайдена відстань більша за збережену, пропускаємо вершину
            if current_distance > distances[current_vertex]:
                continue

            # Перевіряємо сусідів поточної вершини
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Якщо знайшли коротший шлях, оновлюємо та додаємо в купу
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Приклад використання
if __name__ == "__main__":
    # Створюємо граф
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)
    g.add_edge("D", "E", 3)

    # Знаходимо найкоротші шляхи від вершини A
    distances = g.dijkstra("A")
    print("Найкоротші відстані від вершини A до інших вершин:")
    for vertex, distance in distances.items():
        print(f"Відстань до вершини {vertex}: {distance}")
