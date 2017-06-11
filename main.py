# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import sys
from PySide import QtGui
from PySide import QtCore

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

class MyListModel(QtCore.QAbstractListModel):
	def __init__(self, parent=None,*args):
		QtCore.QAbstractListModel.__init__(self, parent, *args)
	
	def rowCount(self, parent=QtCore.QModelIndex()):
		return 1

	def data(self, index, role):
		return 1

class ItemDelegate(QtGui.QItemDelegate):
	


class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
	super(MainWindow, self).__init__(parent)
	self.initialize()

    def initialize(self):

	self.todoList = TodoList()

	grid = QtGui.QGridLayout()
	grid.setSpacing(10)

	self.txt_todoEntry = QtGui.QLineEdit()
	grid.addWidget(self.txt_todoEntry, 0, 0, 1, 2)

	btn_addItem = QtGui.QPushButton("Add Item", self)
	btn_addItem.clicked.connect(self.addItem)
	grid.addWidget(btn_addItem, 0, 2)

	self.todoModel = MyListModel(self)

	btn_deleteItem = QtGui.QPushButton("Delete item", self)
	grid.addWidget(btn_deleteItem, 1, 0)

	btn_timeStart = QtGui.QPushButton("Start time", self)
	grid.addWidget(btn_timeStart, 1, 1)

	btn_timeStop = QtGui.QPushButton("Stop time", self)
	grid.addWidget(btn_timeStop, 1, 2)

	self.lst_todo = QtGui.QListView()
	self.lst_todo.setModel(self.todoModel)
	grid.addWidget(self.lst_todo, 2, 0, 5, 3)

	self.setLayout(grid)

	self.show()

    def addItem(self):
	self.todoModel.appendRow(QtGui.QStandardItem("test"))

def display_title_bar():
    os.system('clear')
    
    print("\t*************************************************")
    print("\t**************     TODO list     ****************")
    print("\t*************************************************")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frame = MainWindow()
    app.exec_()
