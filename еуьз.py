from pprint import pprint
from obstact_class import VacanciesSearch

import requests


class SuperJobAPI(VacanciesSearch):
    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_all_vacancies(self, name_vacancy):
        req = requests.get(self.url, params={
            'count': 10,
            'page': 0,
            'keyword': name_vacancy,
        }, headers={'X-Api-App-Id': "v3.r.137534756.2713d0660f2c5e56e134d49ad7da954a75baf60c."
                                    "ecbfbabe681eae52da43c9b61c7bbe07684aebc8"})

        return [{'id': item['id'], 'name': item['profession'], 'salary_to': item['payment_to'],
                 'salary_for': item['payment_from'], 'description':item['candidat'],
                 'experience': item['experience']['title']} for item in req.json()['items']]


class HeadhunterAPI(VacanciesSearch):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_all_vacancies(self, name_vacancy):
        text = requests.get(self.url, params={
            'per_page': 100,
            'name': self.name_vacancy,
        }).json()
        for page in range(text['pages']):
            answer = requests.get(self.url, params={
                'per_page': 100,
                'name': self.name_vacancy,
                'page': page
            }).json()

            all_vacancies.extend(answer['items'])

        return [{'id': item['id'], 'name': item['profession'], 'salary_to': item['payment_to'],
                 'salary_for': item['payment_from'], 'description':item['candidat'],
                 'experience': item['experience']['title']} for item in req.json()['items']]

api_s = SuperJobAPI()
s = api_s.get_all_vacancies('python')

v1 = [sj_vacancie(id= a['id'], name= a['profession'], salary_to= a['payment_to'],
                  salary_for= a['payment_from'],description= a['candidat'],
                  experience= a['experience']['title']) for a in s]

api_hh = HeadhunterAPI()
hh = api_hh.get_all_vacancies('python')
v2 = [hh_vacancie(id= a['id'], name= a['profession'], salary_to= a['payment_to'],
                  salary_for= a['payment_from'],description= a['candidat'],
                  experience= a['experience']['title']) for a in s]

v = v1 + v2

pprint(s)
pprint(hh)
