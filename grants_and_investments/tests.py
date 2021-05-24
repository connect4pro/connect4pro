from django.test import TestCase
from grants_and_investments.models import Grant, Investment
# Create your tests here.

class GrantModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Grant.objects.create(grant_name='Грант на постройку стадиона', grant_sum = 100000, currency = 'RUB', grant_deadline = '12 месяцев', grant_description = 'Описание')

    def test_grant_name_label(self):
        grant = Grant.objects.get(id=1)
        field_label = grant._meta.get_field('grant_name').verbose_name
        self.assertEquals(field_label, 'Имя гранта')

    def test_grant_sum_label(self):
        grant = Grant.objects.get(id=1)
        field_label = grant._meta.get_field('grant_sum').verbose_name
        self.assertEquals(field_label,'Сумма гранта')

    def test_currency_label(self):
        grant = Grant.objects.get(id=1)
        field_label = grant._meta.get_field('currency').verbose_name
        self.assertEquals(field_label, 'Валюта')

    def test_grant_deadline_label(self):
        grant = Grant.objects.get(id=1)
        field_label = grant._meta.get_field('grant_deadline').verbose_name
        self.assertEquals(field_label, 'Срок гранта')

    def test_grant_description_label(self):
        grant= Grant.objects.get(id=1)
        field_label = grant._meta.get_field('grant_description').verbose_name
        self.assertEquals(field_label, 'Описание гранта')




class InvestmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Investment.objects.create(invest_name='Инвестиции на постройку завода', currency = 'KGS', invest_sum = 1500000, invest_deadline = '2 года', invest_description = 'Описание')

    def test_invest_name_label(self):
        grant = Investment.objects.get(id=1)
        field_label = grant._meta.get_field('invest_name').verbose_name
        self.assertEquals(field_label, 'Имя инвестиции')

    def test_invest_sum_label(self):
        grant = Investment.objects.get(id=1)
        field_label = grant._meta.get_field('invest_sum').verbose_name
        self.assertEquals(field_label,'Сумма инвестиции')

    def test_currency_label(self):
        grant = Investment.objects.get(id=1)
        field_label = grant._meta.get_field('currency').verbose_name
        self.assertEquals(field_label, 'Валюта')

    def test_invest_deadline_label(self):
        grant = Investment.objects.get(id=1)
        field_label = grant._meta.get_field('invest_deadline').verbose_name
        self.assertEquals(field_label, 'Срок инвестиции')

    def test_invest_description_label(self):
        grant= Investment.objects.get(id=1)
        field_label = grant._meta.get_field('invest_description').verbose_name
        self.assertEquals(field_label, 'Описание инвестиции')