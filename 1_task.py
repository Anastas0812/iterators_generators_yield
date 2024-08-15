class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []
        self.index = 0
        self._flatten(list_of_list)

    """Метод проходит по вложенному списку. 
    Если есть вложенный список, метод вызывается, 
    если нет вложенного списка - метод добавляет элемент в flat_list."""
    def _flatten(self, list_1):
        for item in list_1:
            if isinstance(item, list):
                self._flatten(item)
            else:
                self.flat_list.append(item)

    def __iter__(self):
        return self


    def __next__(self):
        if self.index < len(self.flat_list):
            result = self.flat_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration



list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


for i in FlatIterator(list_of_lists_1):
    print(i)

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()