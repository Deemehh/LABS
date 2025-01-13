class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return self.name, self.id


class Manager(Employee):
    def __init__(self, name, id, department=''):
        super().__init__(name, id)
        self.department = department

    def manage_project(self, ):
        return f'Управляет отделом - {self.department}'


class Technician(Employee):
    def __init__(self, name, id, specialization=''):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Выполнение технического обслуживания: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id)
        self.department = department
        self.specialization = specialization

    def add_employee(self, employee):
        if not hasattr(self, 'team'):
            self.team = []
        self.team.append(employee)

    def get_team_info(self):
        if hasattr(self, 'team'):
            return [emp.get_info() for emp in self.team]
        return "Нет сотрудников"


emp1 = Employee('Козлов К.К.', 4)
emp2 = Employee('Морозов М.М.', 13)
manager1 = Manager('Новиков Н.Н.', 6, 'Маркетинг')
technician1 = Technician('Павлов П.П.', 2, 'Системное администрирование')
tech_manager = TechManager('Федоров Ф.Ф.', 43, 'Отдел сетевых технологий', 'Настройка серверов')

tech_manager.add_employee(emp1)
tech_manager.add_employee(emp2)

print(tech_manager.get_info())
print(manager1.manage_project())
print(technician1.perform_maintenance())
print(tech_manager.get_team_info())