"""рекурсия как в 1 таске не подойдет для списков с любым уровнем вложенности, решаем через стек"""
class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = [iter(list_of_list)]
        self.current_item = None #обозначить текущ элемент

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                self.current_item = next(self.stack[-1])
                if isinstance(self.current_item, list):
                    self.stack.append(iter(self.current_item))  # Добавить итератор вложенного списка в стек
                else:
                    return self.current_item 
            except StopIteration:
                self.stack.pop()  # Удалить итератор, если закончились элементы
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
for i in FlatIterator(list_of_lists_2):
   print(i)

if __name__ == '__main__':
    test_3()
