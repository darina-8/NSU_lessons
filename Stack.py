from dataclasses import dataclass


@dataclass()
class Stack:
    l: list

    def push(self, item):
        self.l.append(item)

    def pop(self):
        if not bool(self.l):
            raise ValueError("Стек пуст")
        return self.l.pop()

    def peek(self):
        if not self.l:
            raise ValueError("Стек пуст")
        return self.l[-1]

    def __len__(self):
        return len(self.l)

    def __contains__(self, item):
        return item in self.l
