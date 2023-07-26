class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty.")
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()

    print("Is the stack empty?", stack.isEmpty())

    # Push some elements into the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element of the stack:", stack.peek())
    print("Stack size:", stack.size())

    # Pop elements from the stack
    popped_item = stack.pop()
    print("Popped item:", popped_item)

    print("Top element of the stack:", stack.peek())
    print("Stack size:", stack.size())

    # Pop another element
    popped_item = stack.pop()
    print("Popped item:", popped_item)

    print("Is the stack empty?", stack.isEmpty())
