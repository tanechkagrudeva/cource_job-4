from parsing_hh import HeadhunterAPI
from parsing_sj import SuperJobAPI
from description_vacancy import Vacancy
from details_json import JSONSaver


def info_customer():
    hh = HeadhunterAPI()
    sj = SuperJobAPI()
    json_saver = JSONSaver()


    platforms = input('Сбор вакансий\n'
                      'С какой платформы:\n'
                      '1 - www.hh.ru\n'
                      '2 - www.SuperJob.ru\n'
                      '3 - данные с двух сайтов\n')
    platforms_dict = {
        '1': 'HeadHunter',
        '2': 'SuperJob',
        '3': ''
    }

    name_vacancy = input("Введите название вакансии, которая Вас интересует...\n")

    try:
        vac_hh = [Vacancy(item) for item in hh.get_all_vacancies(name_vacancy)]
        json_saver.save_file(vac_hh)
        vac_sj = [Vacancy(item) for item in sj.get_all_vacancies(name_vacancy)]
        json_saver.save_file(vac_sj)
    except Exception as e:
        print(e)

    ton_n = int(input('Какое количество вакансий вакансий для вывода в топ N:?\n'))
    top_vacancies = Vacancy.top_n(ton_n)

    for vacancy in top_vacancies.all():
        print(f'Название вакансии: {vacancy.name}\n'
              f'Зарплата от: {vacancy.salary_from}\n'
              f'Зарплата до: {vacancy.salary_to}\n'
              f'Описание: {vacancy.description}\n'
              f'Навыки: {vacancy.experience}\n')
    del_input = input('Желаете удалить результаты поиска?\n')
    if del_input.lower() == 'да':
        json_saver.delete_by_id()
        print('Данные удалены!')


if __name__ == "__main__":
    info_customer()
