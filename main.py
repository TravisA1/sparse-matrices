from Node import Node
from LinkedList import LinkedList
import random
import typing
from typing import List, TypeVar, Tuple

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
    x, y = [int(i) for i in input("Give me the (x, y) coordinate of the value you wish to find. ").split()]
    try:
        print(sparse.coord(x, y))
    except IndexError as e:
        print(e)
    char = input("Give me a value you wish to search for. ")
    try:
        r = sparse.search(char)
        for i in range(0, len(r), 2):
            print(f"({r[i]}, {r[i+1]})")
    except IndexError as e:
        print(e)
    row = int(input("Please give me the index of the row you want. "))
    try:
        row_list = sparse.get_row(r=row)
        cur_node = row_list.start
        while cur_node is not None:
            print(f"(({cur_node.idx}, {row}), {cur_node.value})")
            cur_node = cur_node.next_node
    except IndexError as e:
        print(e)
    col = int(input("Please give me the index of the column you want. "))
    try:
        col_list = sparse.get_col(c=col)
        cur_node = col_list.start
        while cur_node is not None:
            print(f"(({col}, {cur_node.idx}), {cur_node.value})")
            cur_node = cur_node.next_node
    except IndexError as e:
        print(e)
