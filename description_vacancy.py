
class Vacancy:
    id = None
    name = None
    salary_to = None
    salary_from = None
    description = None
    experience = None

    def __init__(self, item):
        for k,v in item.items():
            setattr(self, k, v)


    def __str__(self):
        return f'{self.name}\n{self.experience}\n{self.salary_from}\n{self.salary_to}\n{self.description}'

    def __ge__(self):
        def


