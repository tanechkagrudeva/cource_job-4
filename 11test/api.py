from abc import ABC, abstractmethod
import requests as req
from dotenv import load_dotenv
import json
import os
import time
from src.vacancies import HHVacancy, SJVacancy

load_dotenv()


class APIConnector(ABC):
    """
    Абстрактный класс для взаимодействия с API
    """

    @abstractmethod
    def get_vacancies(self, keywords):
        """
        Абстрактный метод для получения списка вакансий
        :param keywords:
        :return:
        """
        pass


class HeadHunterAPI(APIConnector):
    """
    Класс для взаимодействия с API HeadHunter
    """
    vacancies = []
    url = "https://api.hh.ru/vacancies"
    response = None

    def __init__(self) -> None:
        self.response = None

    def get_vacancies(self, keyword: str) -> None:
        """
        Метод для получения списка вакансий
        :param keyword: Ключевое слово для поиска вакансий
        """
        params = {
            'text': keyword,
            'area': 113,
            'per_page': 100,
            'only_with_salary': True,
            'search_field': 'name',
            'page': 0,
        }
        self.response = req.get(self.url, params)
        self.response.content.decode()
        self.vacancies.extend(self.response.json().get('items'))
        if self.response.json().get('pages') > 1:
            for page in range(1, self.response.json().get('pages')):
                response = req.get(f'https://api.hh.ru/vacancies?area=113&text={keyword}&per_page=100&page={page}')
                response.content.decode()
                self.vacancies.extend(response.json().get('items'))

    def add_vacancies(self):
        for vacancy in self.vacancies:
            HHVacancy(vacancy)


class SuperJobAPI(APIConnector):
    token = os.getenv('SJ_TOKEN')
    headers = {'X-Api-App-Id': token}
    vacancies = []
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = None

    def __init__(self):
        self.response = None

    def get_vacancies(self, keywords: str) -> None:
        params = {
            'keywords': keywords,
            'not_archive': 1,
            'count': 50,
            'page': 0
        }
        temp_dict = {'more': True}

        while temp_dict.get('more'):
            if params['page'] == 119:
                time.sleep(60)
            self.response = req.get(self.url, params, headers=self.headers)
            if self.response.status_code == 200:
                self.vacancies.extend(self.response.json()['objects'])
                temp_dict['more'] = self.response.json().get('more')
                params['page'] += 1

    def add_vacancies(self):
        for vacancy in self.vacancies:
            SJVacancy(vacancy)