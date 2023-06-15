'''
Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий 
создание папки на Диске.
Используя библиотеку requests напишите unit-test на верный ответ и возможные 
отрицательные тесты на ответы с ошибкой
Пример положительных тестов:
Код ответа соответствует 200.
Результат создания папки - папка появилась в списке файлов.
'''

import requests
import pytest
import configparser

config = configparser.ConfigParser()
config.read('/Users/a1/Google Диск/мое/Нетология/hw/settings.ini')
ya_token = config['Course_work']['ya_token']

def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {ya_token}'
    }

def test_create_new_folder():
    create_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers()
    params = {"path": "2/"}
    r = requests.put(create_url, headers=headers, params=params)
    assert r.status_code == 201

@pytest.mark.xfail(reason='Папка уже существует')
def test_create_second_folder():
    create_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers()
    params = {"path": "2/"}
    r = requests.put(create_url, headers=headers, params=params)
    assert r.status_code == 201

def test_delete_folder():
    create_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers()
    params = {"path": "2/"}
    r = requests.delete(create_url, headers=headers, params=params)
    assert r.status_code == 204

def test_no_authorization():
    create_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers()
    params = {"path": "2/"}
    r = requests.delete(create_url, params=params)
    assert r.status_code == 401


