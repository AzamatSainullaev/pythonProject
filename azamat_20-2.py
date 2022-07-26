class Company:

    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):

    def __init__(self, company_bank, company_name, first_name, last_name, salary):

        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.salary <= self.company_bank:
            self.company_bank -= self.salary
            print(f'ЗП сотрудника {self.salary}')
        else:
            print('У компании недостачно средств')

    def person_info(self):
        print(f'First_name: {self.first_name}, last_name: {self.last_name}, salary: {self.salary}')

Erenrak = Person(50000, 'erenrak', 'Azamat', 'Dastan', 50001)
Erenrak.person_info()
Erenrak.get_salary()