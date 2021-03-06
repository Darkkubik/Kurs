from dataclasses import dataclass
from typing import Any

@dataclass
class Bank(object):
    name: str = None
    owner: str = None
    data: str = None
    period: str = None
    percant: float = None
    conditions: str = None

    def __str__(self):
        return f'<Bank name: {self.name}, owner: {self.owner}, data: {self.data}, period: {self.period}, percant: {self.percant}>, conditions: {self.conditions}'

@dataclass
class Node(object):
    data: Any
    next: 'Node' = None
 
@dataclass
class LinkedList(object):
    root: Node = None
    last: Node = root
 
    def __str__(self):
        return '<Creditors {}>'.format(
            [_.owner for _ in self]   
        )
 
    def __getitem__(self, index: int) -> Any:
        cur_node = self.root
        for _ in range(index-1):
            cur_node = cur_node.next
        return cur_node.data
 
    def __iter__(self):
        cur_node = self.root
        while cur_node is not None:
            yield cur_node.data
            cur_node = cur_node.next
 
    def append(self, x: Any) -> None:
        node = Node(data = x)
        if self.last is None:
            self.root = node
            self.last = self.root
            return
        self.last.next = node

    def count_len(self):
        i = 0
        cur_node = self.root
        while cur_node is not None:
            i += 1
            cur_node = cur_node.next
        return i


# Вывод списка кредиторов
def print_list(l, n):
    print("\nList of Creditors:")
    i = 0
    while i < n:
        print('Bank name: ', l[i].name, '| Owner name: ', l[i].owner, '| Data: ', l[i].data, '| Period: ', l[i].period,
          '| Percant: ', l[i].percant, '| Conditions: ', l[i].conditions)
        i +=1

# Главная функция
if __name__ == '__main__':
    l = LinkedList()
    #inter_creditors(l)
    l.append(Bank(name = "l", owner = "l", data = "l", period = "l", percant = 5, conditions = "l"))
    l.append(Bank(name = "p", owner = "p", data = "p", period = "p", percant = 5, conditions = "p"))
    l.append(Bank(name = "u", owner = "u", data = "u", period = "u", percant = 5, conditions = "u"))
    l.append(Bank(name = "y", owner = "y", data = "y", period = "y", percant = 5, conditions = "y"))
    n = l.count_len()
    print_list(l, n)
