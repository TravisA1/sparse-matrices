from Node import Node
from LinkedList import LinkedList
import random
import typing
from typing import List, TypeVar
T = TypeVar("T")

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def setup(dim: int = 20):
    matrix = []
    for i in range(dim):
        matrix.append([])
        for j in range(dim):
            if random.random() < 0.25:
                matrix[i].append(alphabet[random.randint(0, 25)])
            else:
                matrix[i].append('')
    return matrix


def print_matrix(matrix: List[List[T]]):
    for row in matrix:
        print(row)


def build_list():
    l = LinkedList()
    for idx, r in enumerate(mtrx):
        temp = LinkedList()
        for n, c in enumerate(r):
            if c != '':
                temp.add_to_end(item=c, idx=n)
        if not temp.is_empty():
            l.add_to_end(item=temp.start, idx=idx)
    return l


def print_list(l: LinkedList):
    if l.is_empty():
        raise RuntimeError("What are the odds")
    temp = l.start
    while temp is not None:
        cur = temp.value
        print(f"({cur.idx}, {cur.value})", end="")
        cur = cur.next_node
        while cur is not None:
            print(f"->({cur.idx}, {cur.value})", end="")
            cur = cur.next_node
        if temp.has_next():
            print("")
            print("|")
            print("v")
        temp = temp.next_node



if __name__ == "__main__":
    mtrx = setup(dim=5)
    sparse = build_list()
    print_matrix(mtrx)
    print_list(sparse)
