from obstact_class import VacanciesSearch

import requests

class HeadhunterAPI(VacanciesSearch):
    """
    Класс для взаимодействия с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_all_vacancies(self, name_vacancy):
        """
        Метод для получения списка вакансий
        :param name_vacancy: Ключевое слово для поиска вакансий
        """
        all_vacancies = []

        text = requests.get(self.url, params={
            'per_page': 100,
            'name': name_vacancy,
        }).json()
        for page in range(text['pages']):
            answer = requests.get(self.url, params={
                'per_page': 100,
                'name': name_vacancy,
                'page': page
            }).json()

            all_vacancies.extend(answer['items'])



        vac_dic = []

        for item in all_vacancies:
            try:
                salary_to = item.get('salary', {'to': None}).get('to', None)
            except (AttributeError, KeyError):
                salary_to = None
            try:
                salary_from = item.get('salary', {'from': None}).get('from', None)
            except (AttributeError, KeyError):
                salary_from = None
            vac_dic.append({
                'id': item['id'],
                 'name': item['name'],
                 'salary_to': salary_to,
                 'salary_from': salary_from,
                 'description': item['snippet']['responsibility'],
                 'experience': item['experience']['name']}
            )
        return vac_dic


hh = HeadhunterAPI()
print(hh.get_all_vacancies("python"))