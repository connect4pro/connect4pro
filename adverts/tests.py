from django.test import TestCase
from adverts.models import Category, UserAdvert
# Create your tests here.

class GrantModelTest(TestCase):

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