import typing
from typing import Generic, TypeVar
T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, idx: int, value: T, next_node: "Node[T]" = None):
        self.idx = idx
        self.value = value
        self.next_node = next_node

    def has_next(self):
        return self.next_node is not None

    def get_index(self):
        return self.idx

    def get_value(self):
        return self.value

    def set_value(self, val: T):
        self.value = val

    def get_next(self):
        return self.next_node

    def set_next(self, node: "Node[T]"):
        self.next_node = node
