from Node import Node
from LinkedList import LinkedList
import random
import typing
from typing import List, TypeVar

T = TypeVar("T")

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def setup(dim: int = 20, rate: float = 0.125):
    matrix = []
    for i in range(dim):
        matrix.append([])
        for j in range(dim):
            if random.random() < rate:
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
        l.add_to_end(item=temp, idx=idx)
    return l


def print_list(l: LinkedList):
    if l.is_empty():
        raise RuntimeError("What are the odds")
    temp = l.start
    first = True
    while temp is not None:
        if temp.value.start is not None:
            if not first:
                print("")
                print("\u2193")
            cur = temp.value.start
            print(f"({temp.idx})", end="")
            while cur is not None:
                print(f"\u2192({cur.idx}, {cur.value})", end="")
                cur = cur.next_node
            first = False
        temp = temp.next_node
    print("")


if __name__ == "__main__":
    mtrx = setup()
    sparse = build_list()
    print_matrix(mtrx)
    print_list(sparse)
    print(f"{len(sparse)=}")
