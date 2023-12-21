class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj

    def pop(self):
        if self.top.next is None:
            i = self.top
            self.top = None
            return i

        last = self.top
        i = None
        while last.next is not None:
            if last.next.next is None:
                i = last.next
                last.next = None
            else:
                last = last.next
        return i

    def get_data(self):
        current = self.top
        e = []
        while current is not None:
            e.append(current.data)
            current = current.next
        return e


if __name__ == '__main__':
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    popped_obj = st.pop()
    print(popped_obj.data)
