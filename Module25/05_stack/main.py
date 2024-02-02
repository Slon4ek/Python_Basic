class Stack:
    def __init__(self):
        self.stack_lst = []

    def __str__(self):
        if self.stack_lst:
            sack_str = ' '.join(str(elem) for elem in self.stack_lst)
            return sack_str
        else:
            return str(self.stack_lst)

    def add(self, *args):
        for arg in args:
            self.stack_lst.append(arg)
        return self.stack_lst

    def pop(self):
        if self.stack_lst:
            elem = self.stack_lst.pop(-1)
            return elem
        else:
            return self.stack_lst

    def clear(self):
        self.stack_lst = []
        return self.stack_lst


class TaskManager:
    def __init__(self):
        self.dict = {}
        self.task = Stack()

    def __str__(self):
        string = ''
        for key, val in sorted(self.dict.items()):
            if not isinstance(val, list):
                string += ''.join('{key}: {val}\n'.format(key=key, val=val))
            else:
                val_str = ', '.join(val)
                string += ''.join('{}: {}\n'.format(key, val_str))
        return string

    def add_task(self, task, priority):
        if task in self.dict.values():
            return
        if priority not in self.dict.keys():
            self.dict[priority] = task
        else:
            self.dict[priority] = self.task.add(self.dict[priority], task)
            self.task.clear()

    def pop(self, key):
        if key in self.dict:
            if not isinstance(self.dict[key], list):
                pop_item = self.dict.pop(key)
                return pop_item
            else:
                for elem in self.dict[key]:
                    self.task.add(elem)
                pop_task = self.task.pop()
                if self.task.stack_lst:
                    self.dict[key] = self.task.stack_lst
                else:
                    self.dict.pop(key)
                self.task.clear()
                return pop_task


task_manager = TaskManager()
task_manager.add_task("сделать уборку", 4)
task_manager.add_task("помыть посуду", 4)
task_manager.add_task("отдохнуть", 1)
task_manager.add_task("поесть", 2)
task_manager.add_task("сдать ДЗ", 2)
print(task_manager)
task_manager.pop(4)
print()
print(task_manager)
task_manager.pop(4)
print()
print(task_manager)
task_manager.pop(2)
print()
print(task_manager)
task_manager.pop(2)
print()
print(task_manager)
task_manager.pop(1)