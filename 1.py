# https://github.com/netology-code/py-homeworks-advanced/tree/master/2.Iterators.Generators.Yield

# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    # def __iter__(self):
    #     self.index = 0
    #     self.index2 = 0
    #     return self

    # def __next__(self):
    #     if self.index2 >= len(self.list_of_list[self.index]):
    #         self.index +=1
    #         self.index2 = 0
    #     if self.index >= len(self.list_of_list):
    #         raise StopIteration
    #     item = self.list_of_list[self.index][self.index2]
    #     self.index2 += 1
    #     return item

    def __iter__(self):
        self.index = 0
        self.result = []
        for list in self.list_of_list:
            for item in list:
                self.result.append(item)
        return self
    
    def __next__(self):
        if self.index >= len(self.result):
            raise StopIteration
        self.index += 1
        return self.result[self.index -1]

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