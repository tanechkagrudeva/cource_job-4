from abc import abstractmethod, ABC


class VacanciesSearch(ABC):
    """
    Абстрактный класс для взаимодействия с API
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all_vacancies(self, name_vacancy):
        """
        Абстрактный метод для получения списка вакансий
        :param name_vacancy:
        :return:
        """
        pass





