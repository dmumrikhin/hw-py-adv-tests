'''
1. Дан список с визитами по городам и странам. Напишите код, который 
возвращает отфильтрованный список geo_logs, содержащий только визиты 
из России."
'''

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def create_geo_logs_filtered(source_list: list) -> list:
    geo_logs_filtered = []
    for item in source_list:
        for visit in item.values():
            if 'Россия' in visit:
                geo_logs_filtered.append(item)
    return geo_logs_filtered
 
'''
2. Выведите на экран все уникальные гео-ID из значений словаря ids.
Т.е. список вида [213, 15, 54, 119, 98, 35]
'''

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def create_unique_ids(source_ids: dict) -> list:
    unique_ids = []
    for item in source_ids.values():
        for geo_id in item:
            if geo_id not in unique_ids:
                unique_ids.append(geo_id)
    return unique_ids

'''
3. Дана статистика рекламных каналов по объемам продаж.
Напишите скрипт, который возвращает название канала с максимальным объемом.
Т.е. в данном примере скрипт должен возвращать 'yandex'.
'''

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def popular_channel(statistic: dict) -> str:
    channel = max(statistic, key=statistic.get)
    return channel

if __name__ == '__main__':
    print(create_geo_logs_filtered(geo_logs))
    print(create_unique_ids(ids))
    print(popular_channel(stats))
    