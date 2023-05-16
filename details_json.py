import json
from description_vacancy import Vacancy


class JSONSaver:
    """Данный класс сохраняет объекты класса Vacancy в файл storage_vac.json."""

    def __init__(self, file_name="vacancies.json"):
        self.file_name: str = file_name
        self.marked_delete: list = []
        self.data_list: list = []

    def read_file(self) -> list[Vacancy]:
        """чтение получившегося файла"""

        with open(self.file_name, 'r', encoding='utf8') as file:
            vac_list = json.load(file)
            return vac_list


    def save_file (self, data: list[Vacancy])-> None:
        """сохранение данных в файл"""

        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(json.dumps(vars(data), ensure_ascii=False) + '\n')

    def collect_del_id(self, id: str) -> None:
        """сбор id списка для удаления из файла"""

        for item in id.split():
            self.marked_delete.append(item)

    def clear_vac_id(self) -> None:
        """Метод очищает список вакансий для удаления из файла"""

        self.marked_delete = []

    def delete_by_id(self) -> None:
        """Удаление вакансий из файла согласно списку id"""

        self.data_dic = []
        new_file = self.save_file()
        for vac in new_file:
            if vac["id"] not in self.collect_del_id():
                self.data_dic.append(vac)

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.data_dic, file, ensure_ascii=False, sort_keys=False, indent=4)
        self.clear_vac_id()


    def update_by_id(self, id: int, vac: Vacancy):
        """Обновление вакансий в файле"""

        missed = 0
        written = 0
        data_for_add = [self.save_file(item) for item in vac]
        self.data_list = self.read_file()

        for vac in data_for_add:
            if id not in self.data_list:
                self.data_list.append(vac)
                written += 1
            else:
                missed += 1

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.data_list, file, ensure_ascii=False, indent=4)
        print(f"Записано вакансий - {written}, пропущено (уже есть в файле) - {missed}")


    def find_by_id(self, id: int) :

        if id:
            for vac in id:
                for key, value in vac.items():
                    print(key, value)

        else:
            print("Нет данных для вывода")

    def find_by_name(self, name: str):
        """Метод выводит список вакансий на экран"""

        if name:
            for vac in name:
                for key, value in vac.items():
                    print(key, value)

        else:
            print("Нет данных для вывода")




