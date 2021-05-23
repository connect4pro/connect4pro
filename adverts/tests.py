from django.test import TestCase
from adverts.models import Category, UserAdvert
# Create your tests here.

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Category.objects.create(name='Кредиты и финансы', description = 'Работа с кредитной и финансовой составляющей')

    def test_category_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название категории')

    def test_category_description_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание категории')



# class UserAdvertModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         #Set up non-modified objects used by all test methods
#         UserAdvert.objects.create(name='Предоставление кредитов', category = Category.name(), description = 'Выдаем кредиты в течении 1 часа. Нужен только паспорт и справка о доходах', price = 120.0, currency = 'USD', completed = 'Да', skills = 'Кредиты')

#     def test_advert_name_label(self):
#         advert = UserAdvert.objects.get(id=1)
#         field_label = advert._meta.get_field('name').verbose_name
#         self.assertEquals(field_label, 'Название объявления')

#     def test_advert_category_label(self):
#         advert = UserAdvert.objects.get(id=1)
#         field_label = advert._meta.get_field('category').verbose_name
#         self.assertEquals(field_label, 'Категория объявления')

#     def test_advert_description_label(self):
#         advert = UserAdvert.objects.get(id=1)
#         field_label = advert._meta.get_field('description').verbose_name
#         self.assertEquals(field_label, 'Описание объявления')

#     def test_advert_price_label(self):
#         advert = UserAdvert.objects.get(id=1)
#         field_label = advert._meta.get_field('price').verbose_name
#         self.assertEquals(field_label, 'Цена')

#     def test_advert_currency_label(self):
#         advert = UserAdvert.objects.get(id=1)
#         field_label = advert._meta.get_field('currency').verbose_name
#         self.assertEquals(field_label, 'Валюта')
    
#     def test_advert_completed_label(self):
#         advert = UserAdvert.objects.get(id=1)
#         field_label = advert._meta.get_field('completed').verbose_name
#         self.assertEquals(field_label, 'Актуальность объявления')

#     def test_advert_skills_label(self):
#         advert = UserAdvert.objects.get(id=1)
#         field_label = advert._meta.get_field('skills').verbose_name
#         self.assertEquals(field_label, 'Умения')