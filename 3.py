# Необязательное задание. Написать итератор, аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.index = 0
        self.result = []
        while self.index < len(self.list_of_list):
            flag = True
            data = self.list_of_list[self.index]
            while flag:
                array = []
                flag = False
                for item in data:
                    if isinstance(item, list):
                        flag = True
                        array.extend(item)
                    else:
                        array.append(item)
                data = array
            self.result += data    
            self.index += 1
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.result):
            raise StopIteration
        self.index += 1
        return self.result[self.index -1]
  
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


if __name__ == '__main__':
    test_3()