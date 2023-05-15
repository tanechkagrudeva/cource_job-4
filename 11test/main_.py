from src.api import HeadHunterAPI, SuperJobAPI
from src.vacancies import HHVacancy, SJVacancy, VacancyCount, GetTopVacancies


def user_interact():
    headhunter = HeadHunterAPI()
    superjob = SuperJobAPI()
    print('Добро пожаловать!!!')
    platform = input('Где ищем?\n'
                     '1. HeadHunter\n'
                     '2. SuperJob\n'
                     '3. Везде\n')
    platform_dict = {
        '1': 'HeadHunter',
        '2': 'SuperJob',
        '3': ''
    }
    query_input = input('Введите поисковый запрос\n')
    print('Ожидайте...')
    try:
        headhunter.get_vacancies(query_input)
        headhunter.add_vacancies()
        HHVacancy.insert_data()
        superjob.get_vacancies(query_input)
        superjob.add_vacancies()
        SJVacancy.insert_data()
    except Exception as e:
        print(e)
    vacancy_count = VacancyCount(query_input, platform_dict.get(platform))
    print(f'Найдено {vacancy_count.get_vacancy_count()} вакансий')
    ton_n = int(input('Какое количество вакансий с самой высокой зарплатой Вы хотите отобразить?\n'))
    top_vacancies = GetTopVacancies(query_input, ton_n, platform_dict.get(platform))

    for vacancy in top_vacancies.search_vacancy():
        print(f'Сайт: {vacancy[1]}\n'
              f'Название вакансии: {vacancy[3]}\n'
              f'Зарплата от: {vacancy[7]}\n'
              f'Зарплата до: {vacancy[8]}\n'
              f'Валюта: {vacancy[9]}\n'
              f'Ссылка на вакансию: {vacancy[10]}\n')
    del_input = input('Желаете удалить результаты поиска?\n')
    if del_input.lower() == 'да':
        SJVacancy.delete_from_db()
        HHVacancy.delete_from_db()
        print('Данные удалены!')
    print('Всего доброго!')


if __name__ == '__main__':
    user_interact()