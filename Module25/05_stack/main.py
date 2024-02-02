class Stack:
    def __init__(self):
        self.__stack_lst = []

    def __str__(self):
        return ', '.join(self.__stack_lst)

    def add(self, elem):
        self.__stack_lst.append(elem)

    def pop(self):
        if self.__stack_lst:
            return self.__stack_lst.pop()
        else:
            return None

    def is_empty(self):
        if not self.__stack_lst:
            return True


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{prior}: {task}\n'.format(
                    prior=str(i_priority),
                    task=self.task[i_priority]
                ))
        return ''.join(display)

    def add_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].add(task)

    def pop(self, key):
        if key in self.task:
            elem = self.task[key].pop()
            if self.task[key].is_empty():
                del self.task[key]
            return elem
        else:
            return None


task_manager = TaskManager()
task_manager.add_task("сделать уборку", 4)
task_manager.add_task("помыть посуду", 4)
task_manager.add_task("отдохнуть", 1)
task_manager.add_task("поесть", 2)
task_manager.add_task("сдать ДЗ", 2)
print(task_manager)
task_manager.pop(4)
print(task_manager)
task_manager.pop(4)
print(task_manager)
task_manager.pop(2)
print(task_manager)
task_manager.pop(2)
print(task_manager)
task_manager.pop(1)
print(task_manager)
