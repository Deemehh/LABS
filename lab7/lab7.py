class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department="Отдел продаж"):
        super().__init__(name, id)
        self.department = department

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name}"

    def get_info(self):
        return f"{super().get_info()}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization=""):
        super().__init__(name, id)
        self.specialization = specialization

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.specialization}"

    def perform_maintenance(self, task=None):
        if task is None:
            task = self.specialization
        return f"Техник {self.name} выполняет техническое обслуживание в области {task}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = "Список сотрудников:\n"
        for emp in self.team:
            team_info += f"Имя: {emp.name}, ID: {emp.id}\n"
        return team_info

    def get_info(self):
        return (f"{super().get_info()}")


emp1 = Employee("Козлов К.К.", "1")
man1 = Manager('Морозов М.М.', '2', 'Отдел продаж')
tech1 = Technician('Павлов П.П.', '3', 'Системный администратор')
tm1 = TechManager("Федоров Ф.Ф.", "4", 'Управление командой', 'Глава отдела')

print("Данные о сотруднике:")
print(emp1.get_info(), "\n")

print("Данные о менеджере:")
print(man1.get_info())
print(man1.manage_project("Продажи"), "\n")

print("Данные о технике:")
print(tech1.get_info())
print(tech1.perform_maintenance("Настройка серверов"), "\n")

print("Данные о тех.менеджере:")
print(tm1.get_info())
print(tm1.manage_project("Набор сотрудников в команду"))
print(tm1.perform_maintenance("Собрание команды"), "\n")

tm1.add_employee(emp1)
tm1.add_employee(man1)
tm1.add_employee(tech1)

print(tm1.get_team_info())
