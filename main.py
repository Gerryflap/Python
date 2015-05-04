import random
from tkinter import *

# --< Bash import statement: >--
#import sys; sys.path.append("/home/tim/git/Python"); import main
import _thread

root = Tk()
list = 'Carl Patric Lindsay Helmut Chris Gwen'.split()
listb = Listbox(root)
for item in list:
    listb.insert(0, item)



class Worker:
    """  """
    def __init__(self, condition, task):
        self.condition = condition
        self.task = task
        self.workspace = 0

    def __str__(self):
        return str(self.task)

    def assignTask(self, task):
        pass


class Mine:
    """  """
    def __init__(self):
        self.assignedWorkers = []

    def assignWorker(self, worker):
        self.assignedWorkers += [worker]
        worker.workspace = self
        worker.task = 'mining'


d = Worker(1, 2);
m = Mine();
m.assignWorker(d);
for worker in m.assignedWorkers:
    print(worker)

def guiLoop(integer):

    while True:
        integer += 1
        print ('Potje vet?: ' + str(integer))


def Pressed():
    d.assignTask('mining')
    print ('Assigned Worker to' + ' ' + str(d.task))


button = Button(root, text='Assign current to mines', command = Pressed)
entry = Entry(root)

button.pack(pady=20, padx=20)
listb.pack()
entry.pack()

_thread.start_new_thread(guiLoop, tuple([10]))
root.mainloop()