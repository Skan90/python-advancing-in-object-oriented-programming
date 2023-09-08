class Employee:
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

