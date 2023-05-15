from obstact_class import VacanciesSearch

import requests


class SuperJobAPI(VacanciesSearch):
    """
    Класс для взаимодействия с API SuperJob
    """
    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_all_vacancies(self, name_vacancy):
        """
        Метод для получения списка вакансий
        :param name_vacancy: Ключевое слово для поиска вакансий
        """

        all_vacancies = []

        req = requests.get(self.url, params={
            'count': 10,
            'page': 0,
            'keyword': name_vacancy,
        }, headers={'X-Api-App-Id': "v3.r.137534756.2713d0660f2c5e56e134d49ad7da954a75baf60c."
                                    "ecbfbabe681eae52da43c9b61c7bbe07684aebc8"}).json()

        all_vacancies.extend(req['objects'])

        vac_dic = []

        for item in all_vacancies:
            try:
                salary_to = item.get('payment_to', None)
            except (AttributeError, KeyError):
                salary_to = None
            try:
                salary_from = item.get('payment_from', None)
            except (AttributeError, KeyError):
                salary_from = None

            vac_dic.append({
                'id': item['id'],
                'name': item['profession'],
                'salary_to': salary_to,
                'salary_from': salary_from,
                'description': item['candidat'],
                'experience': item['experience']['title']}
            )

        return vac_dic



sj = SuperJobAPI()
print(sj.get_all_vacancies("python"))