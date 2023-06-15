'''
Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» 
нужно написать тесты на любые 3 задания из Лекции 4. Необходимо использовать своё 
решение домашнего задания.
'''


from unittest import TestCase
import pytest

from task_1 import create_geo_logs_filtered, geo_logs
from task_1 import create_unique_ids, ids
from task_1 import popular_channel, stats


# class Test_create_geo_logs_filtered(TestCase):

#     def test_if_list(self):
#         result = create_geo_logs_filtered(geo_logs)
#         self.assertIsInstance(result, list)  

#     def test_list_lenght(self):
#         result_lenght = len(create_geo_logs_filtered(geo_logs))
#         self.assertEqual(result_lenght, 6)

#     def test_every_item_contain_russia(self):
#         result = create_geo_logs_filtered(geo_logs)
#         for item in result:
#             for visit in item.values():
#                 self.assertIn('Россия', visit)
    
#     def test_new_list(self):
#         new_list = [
#             {'visit1': ['Москва', 'Россия']},
#             {'visit6': ['Лиссабон', 'Португалия']},
#         ]
#         result = create_geo_logs_filtered(new_list)
#         expected = [{'visit1': ['Москва', 'Россия']}]
#         self.assertListEqual(result, expected)
    
# class Test_create_unique_ids():

#     def test_if_list(self):
#         result = create_unique_ids(ids)
#         assert isinstance(result, list)

#     def test_if_unique(self):
#         result = create_unique_ids(ids)
#         expected = list(set(result))
#         assert sorted(result) == sorted(expected)

# class Test_popular_channel():

#     def test_if_string(self):
#         result = popular_channel(stats)
#         assert isinstance(result, str)

#     def test_if_yandex(self):
#         result = popular_channel(stats)
#         expected = 'yandex'
#         assert result == expected

#     @pytest.mark.parametrize(
#         'x, expected_res',
#         [
#             ({
#                 'facebook': 1, 
#                 'yandex': 1, 
#                 'vk': 1, 
#                 'google': 1, 
#                 'email': 1, 
#                 'ok': 2
#             },
#             'ok'),
#             ({
#                 'facebook': 1, 
#                 'yandex': 1, 
#                 'vk': 5, 
#                 'google': 1, 
#                 'email': 1, 
#                 'ok': 1
#             },
#             'vk')
#         ]
#     )

#     def test_with_params(self, x, expected_res):
#         result = popular_channel(x)
#         assert result == expected_res




