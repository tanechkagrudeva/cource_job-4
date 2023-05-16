
class Vacancy:
    id = None
    name = None
    salary_to = None
    salary_from = None
    description = None
    experience = None
    all = []

    def __init__(self, item):
        for k, v in item.items():
            setattr(self, k, v)


    def __str__(self):
        """Переопределяет строковое представление объекта класса"""
        return f'{self.name}\n{self.experience}\n{self.salary_from}\n{self.salary_to}\n{self.description}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.id}')"

    def __lt__(self, other):
        """Сравниваем объекты по зарплате"""

        return self.salary_from < other.salary

    @classmethod
    def top_n(cls, n: int):
        """Возвращаем TOP N вакансий по зарплате"""
        cls.all.sort(reverse=True)
        return cls.all[:n]

    def display_vac(self):
        """Выводит список вакансий класса на экран"""

        for vac in self.all:
            print(vac)
        print(f"Всего вакансий - {len(Vacancy.all)}")




