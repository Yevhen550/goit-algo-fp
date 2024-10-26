class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Вставка на початок
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Вставка в кінець
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Вставка після конкретного вузла
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Видалення вузла за значенням
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # Пошук елемента
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Друк списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    # Реверсування списку
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування списку методом вставок
    def insertion_sort(self):
        sorted_list = None  # Відсортований список
        current = self.head

        while current:
            next_node = current.next
            # Знайти місце для поточного елементу в відсортованому списку
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next

                current.next = sorted_current.next
                sorted_current.next = current

            current = next_node

        self.head = sorted_list

    # Об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1: "LinkedList", list2: "LinkedList") -> "LinkedList":
        merged_list = LinkedList()
        dummy = Node()  # Допоміжний вузол для початку списку
        tail = dummy

        current1 = list1.head
        current2 = list2.head

        # Злияння двох відсортованих списків
        while current1 and current2:
            if current1.data <= current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        # Якщо є залишки в будь-якому з списків
        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        merged_list.head = dummy.next  # Пропускаємо допоміжний вузол
        return merged_list


# Приклад використання
llist = LinkedList()

# Вставка вузлів
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Початковий зв'язний список:")
llist.print_list()

# Реверсування списку
llist.reverse_list()
print("\nРеверсований зв'язний список:")
llist.print_list()

# Сортування списку методом вставок
llist.insertion_sort()
print("\nВідсортований зв'язний список методом вставок:")
llist.print_list()

# Створення двох відсортованих списків для об'єднання
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted_lists(llist1, llist2)
print("\nОб'єднаний відсортований список з двох відсортованих списків:")
merged_list.print_list()
