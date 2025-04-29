class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class GuessLinkedList:
    def __init__(self):
        self.head = None
        self.words_set = set()

    def add_guess(self, word):
        if word in self.words_set:
            return False  # Duplicate = Game Over

        new_node = Node(word)
        self.words_set.add(word)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        return True

    def get_history(self):
        words = []
        curr = self.head
        while curr:
            words.append(curr.value)
            curr = curr.next
        return words
