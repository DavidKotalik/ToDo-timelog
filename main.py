# -*- coding: utf-8 -*-
#!/usr/bin/python

import os

class TodoItem:

    def __init__(self, text):
        self.text = text

    def printSelf (self):
        print self.text

class TodoList:

    def __init__(self):
        self.int_todoCount = 0
        self.arr_todoList = []

    def addTodo(self, item):
        self.arr_todoList.append(item)

    def printSelf(self):
        for item in self.arr_todoList:
            item.printSelf()

def display_title_bar():
    os.system('clear')
    
    print("\t*************************************************")
    print("\t**************     TODO list     ****************")
    print("\t*************************************************")


todoList = TodoList()

choice = ''

while True:
    display_title_bar()
    todoList.printSelf()

    choice = raw_input("User input")

    if choice == 'q':
        break;
    else:
        todoList.addTodo(TodoItem(choice))
