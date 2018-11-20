from dataclasses import dataclass
from typing import Any

with open("creditors_int.txt") as f:
        lines = f.read().split("\n")
 
 
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

# Добавление кредитора вручную
def inter_creditors(l):
    command = 0
    while command != 1:
        print("Новый кредитор")
        nm = str(input("Введите название банка: "))
        ow = str(input("Введите имя кредитора: "))
        dt = str(input("Введите дату взятие кредита: "))
        per = str(input("Введите период взятия кредита: "))
        pr = float(input("Введите процент кредита: "))
        cond = str(input("Введите условия: "))
        l.append(Bank(name = nm, owner = ow, data = dt, period = per, percant = pr, conditions = cond))
        command = int(input("Хотите добавить еще кредитора? Да - 0 | Нет - 1: "))

# Добавление кредиторов из файла
def inter_creditors_file(l):
    for line in lines:
        d = line.split(", ")
        l.append(Bank(name = d[0], owner = d[1], data = d[2], period = d[3], percant = d[4], conditions = d[5]))
    f.close()

# Вывод списка кредиторов
def print_list(l, n):
    print("\nList of Creditors:")
    i = 0
    while i < n:
        print('Bank name: ', l[i].name, '| Owner name: ', l[i].owner, '| Data: ', l[i].data, '| Period: ', l[i].period,
          '| Percant: ', l[i].percant, '| Conditions: ', l[i].conditions)
        i +=1

# Запись списка кредиторов в файл
def print_list_file(l, n):
    i = 0
    file = open("creditors_out.txt", 'a')
    while i < n:
        file.write(l[i].name + ', ' + l[i].owner + ', ' + l[i].data + ', ' +  l[i].period + ', ' + str(l[i].percant) + ', ' + l[i].conditions + '\n')
        i+=1
    file.close()

'''# Поиска владельца кредита
def find_owner(l, n):
    index = -1
    while index < 0:
        i = 1
        print("Введите фамилию кредитора: ")
        owner = str(input())
        while i < n:
            if(owner == l[i].owner):
                index = i
            i+=1
        if(index == -1):
            print("Такого кредитора нет в списке.")
        else:
            print('Bank name: ', l[index].name, '| Owner name: ', l[index].owner, '| Data: ', l[index].data, '| Period: ', l[index].period,
              '| Percant: ', l[index].percant, '| Conditions: ', l[index].conditions)

# Поиск банка
def find_bank(l, n):
    index = -1
    while index < 0:
        i = 1
        print("Введите название банка: ")
        bank = str(input())
        while i < n:
            if(bank == l[i].name):
                index = i
            i+=1
        if(index == -1):
            print("Такого банка нет в списке.")
        else:
            print('Bank name: ', l[index].name, '| Owner name: ', l[index].owner, '| Data: ', l[index].data, '| Period: ', l[index].period,
              '| Percant: ', l[index].percant, '| Conditions: ', l[index].conditions)

# Изменение имя владельца кредита
def change_owner(l, n):
    index = -1
    while index < 0:
        i = 1
        print("Введите фамилию кредитора: ")
        owner = str(input())
        while i < n:
            if(owner == l[i].owner):
                index = i
            i+=1
        if(index == -1):
            print("Такого кредитора нет в списке.")
        else:
            print("Введите новую фамилию кредитора: ")
            owner = str(input())
            l[index].owner = owner

# Изменение банка кредитора
def change_bank(l, n):
    index = -1
    while index < 0:
        i = 1
        print("Введите название банка: ")
        bank = str(input())
        while i < n:
            if(bank == l[i].name):
                index = i
            i+=1
        if(index == -1):
            print("Такого банка нет в списке.")
        else:
            print("Введите новый банк кредитора: ")
            bank = str(input())
            l[index].name = bank

file = open('creditors.txt', 'w')
file.write'''

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
    print(n)
    '''find_owner(l, n)
    find_bank(l, n)
    change_owner(l,n)
    change_bank(l,n)
    print_list(l,n)
    print_list_file(l,n)'''
