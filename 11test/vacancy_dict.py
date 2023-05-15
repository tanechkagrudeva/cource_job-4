from obstact_class import DescriptionVacancy


class Vacancy(DescriptionVacancy):
    """ Данный класс подключается к API hh.ru и получает вакансии.
    Полученные вакансии хранятся в классе в собственном формате.
    Все классы наследуемые от класса DescriptionVacancy имеют одинаковый формат хранения вакансий."""

    def __init__(self):
        self.url: str = 'https://api.hh.ru/vacancies'
        self.parametrs: dict = {"text": "", "search_field": [''], "per_page": 20, "period": 1}
        self.search_fields: list = ["name", "company_name", "description"]
        self.headers: str = ""
        self.response: int = 0
        self.vacancies: list = []
        self.base: str = "hh"

    def item_format(self, key: str, value: str | int) -> None:
        """ Метод получает в качестве параметров ключ и значение, которые добавляет в params запроса к API"""

        if key == "text":
            self.params["text"] = value
        # key search_field должен приходить в виде трёхсимвольной строки из цифр 1 или ноль - "101"
        # позиции единиц добавляют соответсвующее поле поиска из словаря self.search_fields:
        # ["name", "company_name", "description"]
        elif key == "search_field":
            self.params["search_field"] = []
            for i in range(3):
                if value[i] == "1":
                    self.params["search_field"].append(self.search_fields[i])
        elif key == "per_page":
            self.params["per_page"] = value
        elif key == "period":
            self.params["period"] = value
        else:
            print(f"Неверный параметр {key}")