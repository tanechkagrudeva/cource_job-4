from parsing_hh import HeadhunterAPI
from parsing_sj import SuperJobAPI
from description_vacancy import VacancyHH, VacancySj


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
        vac_hh = [Vacancy(item) for item in hh.get_all_vacancies()]
        json_saver.save(vac_hh)
        VacancyHH.update()
        sj.get_all_vacancies()
        VacancySj.update()
    except Exception as e:
        print(e)

    ton_n = int(input('Какое количество вакансий вакансий для вывода в топ N:?\n'))
    top_vacancies = VacancyHH.add_vacancy()+VacancySj.add_vacancy()

    for vacancy in top_vacancies.all_vacancies():
        print(f'Сайт: {vacancy[1]}\n'
              f'Название вакансии: {vacancy[4]}\n'
              f'Зарплата от: {vacancy[7]}\n'
              f'Зарплата до: {vacancy[6]}\n'
              f'Ссылка на вакансию: {vacancy[3]}\n')
    del_input = input('Желаете удалить результаты поиска?\n')
    if del_input.lower() == 'да':
        VacancySj.del_all()
        VacancyHH.del_all()
        print('Данные удалены!')
    print('До новых встреч')


if __name__ == "__main__":
    info_customer()
