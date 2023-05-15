from obstact_class import JSONS
import json
import os
from .description_vacancy import Vacancy
road_data = os.path.abspath("/Cours_job_OOP")

class JSONSaver(JSONS):
    """Данный класс сохраняет объекты класса Vacancy в файл storage_vac.json."""
    def __init__(self, file_name="vacancies.json"):
        self.file_name: str = file_name

    def read_file(self) -> list[Vacancy]:
        pass
    def save_file (self, data: list[Vacancy])-> None:
        pass

    def delete_by_id(self, id: int):
        pass

    def update_by_id(self, id: int, vac: Vacancy):
        pass

    def find_by_id(self, id: int) -> Vacancy:
        pass
    def find_by_name(self, name: str) -> list[Vacancy]:
        pass

    def update(self, new_data: list) -> None:
        """Обновление вакансий в файле"""

        not_vacancies = 0
        written = 0
        data_for_add = [self.to_dict(item) for item in new_data]
        self.save_vacancies = self.all_vacancies()

        for vacancy in data_for_add:
            if vacancy['id'] not in [x['id'] for x in self.save_vacancies]:
                self.save_vacancies.append(vacancy)
                written += 1
            else:
                not_vacancies += 1

        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(self.save_vacancies, data_file, ensure_ascii=False, indent=4)
        print(f"Добавлено вакансий - {written}, пропущено (дубликат в файле) - {not_vacancies}")

    def add_vacancy(self, keywords: str = "") -> list:

        """Метод загружает вакансии данные из файла, фильтрует их по параметру keywords и возвращает их в виде списка."""

        result = []
        if keywords:
            with open(self.path, 'rt', encoding='utf-8') as data_file:
                for item in json.load(data_file):
                    for keyword in keywords.split():
                        for item.values in item.values():
                            if keyword.isdigit() and str(item.values).isdigit():
                                if int(keyword) <= item.values:
                                    result.append(item)
                                    break
                            elif keyword.isalpha() and not str(item.values).isdigit() and item.values is not None:
                                if keyword.lower() in item.values.lower():
                                    result.append(item)
        else:
            with open(self.path, 'rt', encoding='utf-8') as data_file:
                result = json.load(data_file)

        return result

    def mark_del(self, id: str) -> None:
        """Метод добавляет id вакансии в список для удаления из файла"""

        for item in id.split():
            self.marked_delete.append(item)

        def clear_marks(self) -> None:
            """Метод очищает список вакансий для удаления из файла"""

        self.marked_delete = []

        def del_marked(self) -> None:
            """Метод удаляет вакансии из файла согласно списку id для удаления"""

        self.save_vacancies = []
        file_data = self.add_vacancy()
        for vacancy in file_data:
            if vacancy['id'] not in self.marked_delete:
                self.save_vacancies.append(vacancy)
        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(self.save_vacancies, data_file, ensure_ascii=False, sort_keys=False, indent=4)
        self.clear_marks()

    def del_all(self) -> None:
        """Метод удаляет все вакансии из файла"""

        empty_list = []
        with open(self.path, 'w', encoding='utf-8') as data_file:
            json.dump(empty_list, data_file, ensure_ascii=False, sort_keys=False, indent=4)

    @staticmethod
    def display_vac(data: list) -> None:
        """Метод выводит список вакансий на экран"""

        if data:
            for vacancies in data:
                for key, value in vacancies.items():
                    print(key, value)
                print("+" * 30)
        else:
            print("Нет данных для вывода")


