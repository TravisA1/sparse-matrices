from Node import Node
from typing import Generic, TypeVar, List
T = TypeVar("T")


class LinkedList(Generic[T]):
    def __init__(self, start: Node[T] = None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def add_to_end(self, item: T, idx: int):
        """
        appends a node with the given value at the end of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :param idx: index of the node within the matrix
        :return: None
        """
        # OK, I've written this one for you, to get you started.
        if self.start is None:
            self.start = Node(value=item, idx=idx)
        else:
            p: Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            p.set_next(Node(value=item, idx=idx))

    def add_to_start(self, item: T, idx: int):
        """
        inserts a node with the given value at the start of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :param idx: index of the node within the matrix
        :return: None
        """
        # ------------------------------
        temp = Node(value=item, idx=idx)
        if self.start is not None:
            temp.set_next(node=self.start)
        self.start = temp
        # ------------------------------

    # def add_all_to_end(self, items: List[T]):
    #     """
    #     appends each of the items in items as separate nodes at the end of this list, preserving order.
    #     Note: while you can call other methods, it might not be the most efficient!
    #     :param items: a list or tuple of items to add
    #     :return: None
    #     """
    #     # ------------------------------
    #     cur_idx = 1
    #     if self.start is not None:
    #         temp = self.start
    #         while temp.has_next():
    #             temp = temp.next_node
    #             cur_idx += 1
    #         for item in items:
    #             temp.set_next(node=Node(value=item, idx=cur_idx))
    #             temp = temp.next_node
    #             cur_idx += 1
    #     else:
    #         temp = Node(value=items[0], idx=0)
    #         self.start = temp
    #         for item in items[1:]:
    #             temp.set_next(node=Node(value=item, idx=cur_idx))
    #             temp = temp.next_node
    #             cur_idx += 1
    #     # ------------------------------

    def __len__(self):
        """
        overrides the "len" operator - gives the number of items in this list.
        :return: the number of items
        """
        length = 0
        # ------------------------------
        temp = self.start
        if temp is None:
            return 0
        else:
            length += 1
        while temp.has_next():
            length += 1
            temp = temp.next_node

        # ------------------------------
        return length

    def __contains__(self, item):
        """
        returns whether this linked list contains the item, at least once.
        :param item: the item to match
        :return: whether this item is in the linked list.
        """
        # ------------------------------
        temp = self.start
        if temp is None:
            return False
        while True:
            if temp.value == item:
                return True
            if temp.has_next():
                temp = temp.next_node
            else:
                break

        # ------------------------------
        return False

    def index(self, item):
        """
        gives the index of the first instance in this list with matching item, or throws an error if not found.
        :param item: item to match
        :return: the positive index of the first occurrence of the item.
        """
        # ------------------------------
        idx = 0
        temp = self.start
        if temp is not None:
            while True:
                if temp.value == item:
                    return idx
                if temp.has_next():
                    temp = temp.next_node
                else:
                    break
                idx += 1
        # ------------------------------
        raise RuntimeError(f"Item {item} not found in list.")

    def pointers_for_index(self, index: int) -> {Node[T], Node[T]}:
        """
        Internal method - not really intended for an outside class to use this, but other methods in this class may
        find it handy!

        Gets the pointer to the ith item in the list and the pointer to the (i-1)th item in the list. If i is zero,
        then the latter will be None. If i extends 1 past the end of the list, p will be None and back will be the last
        element. If i extends further than that past the end of the list, then both will be None.
        :param index: a non-negative integer
        :return: p, back - the pointers for the ith and (i-1)th items in the list.
        """
        # OK. I've written this one for you.
        p: Node[T] = self.start
        back: Node[T] = None
        count = 0
        while count < index:
            back = p
            if p is not None:
                p = p.get_next()
            count += 1
            if p is None and back is None:
                break
        return p, back

    def item_at_index(self, index: int) -> T:
        """
        gets the item stored in the list at position "index." Does not alter the list. Crashes if index is out of range.
        :param index: an index in range 0 ... len(list)-1, inclusive
        :return: the value stored in the list at this location.
        """
        # ------------------------------
        p, back = self.pointers_for_index(index=index)
        if p is None:
            raise IndexError
        # ------------------------------
        return p.value  # replace this to return an actual value.

    def item_at_start(self) -> T:
        """
        gets the value stored in the first node
        :return: value
        """
        # ------------------------------
        if self.start is not None:
            return self.start.value
        # ------------------------------
        return None  # replace this to return an actual value.

    def item_at_end(self) -> T:
        """
        gets the value stored in the last node.
        (Tip: remember, counting up the nodes is O(N)... try to avoid making two passes through this list.)
        :return:
        """
        # ------------------------------
        temp = self.start
        if temp is not None:
            while True:
                if temp.has_next():
                    temp = temp.next_node
                else:
                    return temp.value
        # ------------------------------
        return None

    def insert_value_at_start(self, value: T):
        """
        creates a new node with value and inserts it at the start of the list.
        :param value: item to add.
        :return: None
        """
        # ------------------------------
        self.add_to_start(item=value, idx=0)
        # ------------------------------

    def insert_value_at_index(self, value: T, index: int):
        """
        puts the given value into a new node and inserts it into the list so that it is now at position "index." If
        index > length of the list, this will put it at the end of the list.
        :param value:
        :param index:
        :return:
        """
        # I've written this one for you.
        p, back = self.pointers_for_index(index)
        if p == self.start:
            self.insert_value_at_start(value)
        else:
            back.next_node = Node(value=value, next_node=p, idx=index)

    def insert_all_at_index(self, in_list: List[T], index: int):
        """
        Goes through all the items in list, and adds them (in order) into this list, starting at the initial location.
        :param in_list:
        :param index:
        :return: None
        """
        # ------------------------------
        if index > len(self):
            raise IndexError
        for i in in_list:
            self.insert_value_at_index(value=i, index=index)
            index += 1
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove_first_item(self):
        """
        alters this list by removing the first item. If there is no first item, then throws an exception
        :return: None
        """
        # ------------------------------
        if self.start is None:
            raise IndexError("Cannot remove item from empty list.")
        self.start = self.start.next_node
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove_item_at_index(self, index: int):
        """
        alters this list by removing the ith element. If index is out of the range of the list, throws an exception.
        :param index: item number to remove
        :return: None
        """
        # ------------------------------
        temp = self.start
        if temp is None:
            raise IndexError("Cannot remove item from empty list.")
        if index > len(self)-1:
            raise IndexError("Index out of range.")
        p, back = self.pointers_for_index(index=index)
        if back is None:
            self.start = p.next_node
        else:
            back.next_node = p.next_node
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove_last_item(self):
        """
        removes the last item in this list, but does not return it. If list is empty, throw an exception
        (Note, since counting up the number of items in the list is O(N), try to avoid making two passes.)
        :return: None
        """
        # ------------------------------
        temp = self.start
        multi_item = False
        if temp is not None:
            while True:
                if temp.has_next():
                    back = temp
                    temp = temp.next_node
                    multi_item = True
                else:
                    break
        else:
            raise IndexError("Cannot remove item from empty list.")
        if multi_item:
            back.next_node = None
        else:
            self.start = None
        # ------------------------------

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove(self, val: T, first_only=False):
        """
        removes either the first or all items that match val from this list, depending on the state of first_only
        :param val:
        :param first_only:
        :return: None
        """
        # ------------------------------
        if first_only:
            try:
                idx = self.index(item=val)
                self.remove_item_at_index(idx)
            except RuntimeError:
                return
        else:
            while True:
                try:
                    idx = self.index(item=val)
                    self.remove_item_at_index(idx)
                except RuntimeError:
                    break

        # ------------------------------

    def to_list(self) -> List[T]:
        """
        generates a list of items in the same order as this linked list.
        """
        # I've written this one for you.
        result = []
        p: Node[T] = self.start
        while p is not None:
            result.append(p.get_value())
            p = p.get_next()
        return result

    def __str__(self) -> str:
        """
        This is akin to the "toString()" method in java - this makes a string representation of this list.
        :return: a string describing this list.
        """
        result = "["
        p: Node[T] = self.start
        while p is not None:
            result += f"{p.get_value()} "
            p = p.get_next()
        result += "]"
        return result

    def __repr__(self) -> str:
        """
                This is akin to the "toString()" method in java - this makes a string representation of this list.
                (For debugging.)
                :return: a string describing this list.
                """
        return self.__str__()  # in this case, the __repr__ and __str__ are the same.
