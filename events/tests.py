from django.test import TestCase
from events.models import Event
# Create your tests here.

class EventModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Event.objects.create(name='Мероприятие 1', date = '2021-05-23', time = '10:00', location = 'Ул.Горького 25/2', event_format = 'Онлайн', sum = 0, event_image ='null')

    def test_name_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя мероприятия')

    def test_date_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'Дата мероприятия')

    def test_time_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('time').verbose_name
        self.assertEquals(field_label, 'Начало')

    def test_location_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'Место')

    def test_format_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('event_format').verbose_name
        self.assertEquals(field_label, 'Формат мероприятия')

    def test_sum_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('sum').verbose_name
        self.assertEquals(field_label, 'Стоимость входа')

    def test_event_image_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('event_image').verbose_name
        self.assertEquals(field_label, 'Плакат мероприятия')