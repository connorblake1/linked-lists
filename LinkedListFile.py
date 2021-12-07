import sys
from typing import Generic, TypeVar, List
T = TypeVar("T")

class LL_Node(Generic[T]):
    def __init__(self, value:T = None, next: "LL_Node[T]" = None):
        self.set_value(value)
        self.set_next(next)

    def has_next(self):
        return self.next is not None

    def get_next(self)->"LL_Node[T]":
        return self.next

    def get_value(self) -> T:
        return self.value

    def set_value(self,in_val:T):
        self.value = in_val

    def set_next(self,nxt: "LL_Node[T]"):
        self.next = nxt

class LinkedList(Generic[T]):
    def __init__(self):
        self.start:LL_Node[T] = None

    def is_empty(self):
        return self.start is None

    def add_to_end(self, item:T):
        """
        appends a node with the given value at the end of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :return: None
        """
        # OK, I've written this one for you, to get you started.
        if self.start is None:
            self.start = LL_Node[T](value=item)
        else:
            p:LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            p.set_next(LL_Node[T](value=item))

    def add_to_start(self, item: T):
        """
        inserts a node with the given value at the start of this list.
        :param item: the sort of thing we are storing in this list. NOTE: NOT A NODE!
        :return: None
        """
        # ------------------------------
        n: LL_Node[T] = LL_Node[T](value=item)
        if not self.is_empty():
            n.next = self.start
        self.start = n
        # ------------------------------

    def add_all_to_end(self, items:List[T]):
        """
        appends each of the items in items as separate nodes at the end of this list, preserving order.
        Note: while you can call other methods, it might not be the most efficient!
        :param items: a list or tuple of items to add
        :return: None
        """
        if self.start is None:
            self.start = LL_Node[T](value=items[0])
            p = self.start
            for i in range(1, len(items)):
                n: LL_Node[T] = LL_Node[T](value=items[i])
                p.set_next(n)
                p = p.get_next()
        else:
            p:LL_Node[T] = self.start
            while p.has_next():
                p = p.get_next()
            for i in range(len(items)):
                n: LL_Node[T] = LL_Node[T](value=items[i])
                p.set_next(n)
                p = p.get_next()
        # ------------------------------

    def __len__(self):
        """
        overrides the "len" operator - gives the number of items in this list.
        :return: the number of items
        """
        # ------------------------------

        if self.start is None:
            return 0
        length = 1
        p:LL_Node[T] = self.start
        while p.has_next():
            p = p.get_next()
            length += 1
        return length
        # ------------------------------


    def __contains__(self, item):
        """
        returns whether this linked list contains the item, at least once.
        :param item: the item to match
        :return: whether this item is in the linked list.
        """
        # ------------------------------
        if self.start is None:
            return False
        p:LL_Node[T] = self.start
        if p.get_value().__eq__(item):
            return True
        while p.has_next():
            p = p.get_next()
            if p.get_value().__eq__(item):
                return True
        # ------------------------------
        return False

    def index(self, item):
        """
        gives the index of the first instance in this list with matching item, or throws an error if not found.
        :param item: item to match
        :return: the positive index of the first occurance of the item.
        """
        # ------------------------------
        if self.start is not None:
            p:LL_Node[T] = self.start
            index = 1
            if p.get_value().__eq__(item):
                return 0
            while p.has_next():
                p = p.get_next()
                if p.get_value().__eq__(item):
                   return index
                index += 1
        # ------------------------------
        raise RuntimeError(f"Item {item} not found in list.")

    def pointers_for_index(self, index:int)->{LL_Node[T], LL_Node[T]}:
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
        p:LL_Node[T] = self.start
        back:LL_Node[T] = None
        count = 0
        while count < index:
            back = p
            if p is not None:
                p = p.get_next()
            count += 1
            if p is None and back is None:
                break
        return p, back

    def item_at_index(self, index:int) -> T:
        """
        gets the item stored in the list at position "index." Does not alter the list. Crashes if index is out of range.
        :param index: an index in range 0 ... len(list)-1, inclusive
        :return: the value stored in the list at this location.
        """
        # ------------------------------
        if self.start is None:
            raise IndexError(f"Item at {index} not found in list.")
        if (self.pointers_for_index(index))[0] is not None:
            return (self.pointers_for_index(index))[0].get_value()
        raise IndexError(f"Item at {index} not found in list.")

    def item_at_start(self) -> T:
        """
        gets the value stored in the first node
        :return: value
        """
        # ------------------------------
        return self.item_at_index(0)

    def item_at_end(self) -> T:
        """
        gets the value stored in the last node.
        (Tip: remember, counting up the nodes is O(N)... try to avoid making two passes through this list.)
        :return:
        """
        # ------------------------------
        if self.start is None:
            return None
        p: LL_Node[T] = self.start
        while p.has_next():
            p = p.get_next()
        return p.get_value()


        # ------------------------------
        #return p.value  # replace this to return an actual value.

    def insert_value_at_start(self, value:T):
        """
        creates a new node with value and inserts it at the start of the list.
        :param value: item to add.
        :return: None
        """
        # ------------------------------
        n: LL_Node[T] = LL_Node[T](value=value)
        p:LL_Node[T] = self.start
        self.start = n
        n.set_next(p)
        # ------------------------------

    def insert_value_at_index(self, value:T, index:int):
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
            back.next = LL_Node[T](value=value, next = p)

    def insert_all_at_index(self, in_list:List[T], index:int):
        """
        Goes through all the items in list, and adds them (in order) into this list, starting at the intial location.
        :param in_list:
        :param index:
        :return: None
        """
        # ------------------------------
        p, back = self.pointers_for_index(index)
        if p is not None or back is not None:
            n = LL_Node[T](value=in_list[0])
            if back is None and self.start is p:
                self.start = n
                back = self.start
            else:
                back.set_next(n)
                back = n
            for i in range(1, len(in_list)):
                n = LL_Node[T](value=in_list[i])
                back.set_next(n)
                back = n
            back.set_next(p)
        else:
            raise IndexError("Index out of range.")

        # Note: if it goes out of bounds, use this:
        # raise IndexError("Index out of range.")

    def remove_first_item(self):
        """
        alters this list by removing the first item. If there is no first item, then throws an exception
        :return: None
        """
        # ------------------------------
        if self.start is not None:
            if self.start.get_next() is not None:
                self.start = self.start.get_next()
            else:
                raise IndexError("Index out of range.")
        else:
            raise IndexError("Index out of range.")
        # ------------------------------

    def remove_item_at_index(self, i:int):
        """
        alters this list by removing the ith element. If i is out of the range of the list, throws an exception.
        :param index: item number to remove
        :return: None
        """
        # ------------------------------
        if i == 0:
            self.remove_first_item()
            return
        if self.start is not None:
            p:LL_Node[T] = self.start
            p1:LL_Node[T] = None
            index = 0
            while p.has_next() and index < i:
                p1 = p
                p = p.get_next()
                index += 1
            if index != i:
                raise IndexError("Index out of range1.")
            else:
                p1.set_next(p.get_next())
        else:
            raise IndexError("Index out of range.")


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
        #
        if self.start is None:
            raise IndexError("Index out of range.")
        p:LL_Node[T] = self.start
        p1:LL_Node[T] = None
        while p.has_next():
            p1 = p
            p = p.get_next()
        p1.set_next(None)

        # ------------------------------

        # Note: if it goes out of bounds, use this:
        #


    def remove(self, val:T, first_only=False):
        """
        removes either the first or all items that match val from this list, depending on the state of first_only
        :param val:
        :param first_only:
        :return: None
        """
        if self.start is None:
            raise IndexError("Index out of range.")
        p:LL_Node[T] = self.start
        p1:LL_Node[T] = p
        if p.get_value().__eq__(val):
            self.start = p.get_next()
            if first_only:
                return
        while p.has_next():
            p=p.get_next()
            if p.get_value().__eq__(val):
                p1.set_next(p.get_next())
                if first_only:
                    return
                p = p1
            else:
                p1 = p





        # ------------------------------

    def toList(self)->List[T]:
        """
        generates a list of items in the same order as this linked list.
        """
        # I've written this one for you.
        result = []
        p:LL_Node[T] = self.start
        while p != None:
            result.append(p.get_value())
            p = p.get_next()
        return result
