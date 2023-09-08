class Employee:

    def __init__(self, name):
        self.name = name

    def register_hours(self, hours):
        print('Registered hours...')

    def show_tasks(self):
        print('Doing stuff...')


class Caelum(Employee):
    def show_tasks(self):
        print('Doing Caelum stuff...')

    def search_courses_of_month(self, month=None):
        print(f'Searching Caelum courses of {month}' if month else 'Searching Caelum courses of this month')


class Alura(Employee):
    def show_tasks(self):
        print('Doing Alura stuff...')

    def search_questions_without_answer(self):
        print('Searching unanswered questions in Alura')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.name}'


class Junior(Alura):
    pass


class MidLevel(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


rafael = Junior('Rafael')
rafael.search_questions_without_answer()
# NOTES:
# The order of inheritance is important.
# The first class will be the first to be searched for the method.
# MRO - Method Resolution Order takes into account the order of inheritance.
# First it will search in the class itself, then the first ancestor, in this case Alura,
# then the second ancestor, Caellum and not in Employee, because Employee is not a good head class.
# Since Employee is not a good head class, it will change the order of search,
# and only after looking inside Caelum it will look inside Employee.
cintia = MidLevel('Cintia')
cintia.search_questions_without_answer()
cintia.search_courses_of_month()

marco = Senior('Marco')
print(marco)
