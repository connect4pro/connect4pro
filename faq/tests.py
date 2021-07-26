from django.test import TestCase
from faq.models import WriteUs, QuestionsAndAnswers
# Create your tests here.




class WriteUsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        WriteUs.objects.create(full_name='Живайкин Александр Романович', phone = '+996551337397', email = 'sashkewicha@gmail.com', message = 'Сообщение')

    def test_full_name_label(self):
        message = WriteUs.objects.get(id=1)
        field_label = message._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'Фамилия, имя, отчество')

    def test_phone_label(self):
        message = WriteUs.objects.get(id=1)
        field_label = message._meta.get_field('phone').verbose_name
        self.assertEquals(field_label,'Контактный номер телефона')

    def test_email_label(self):
        message = WriteUs.objects.get(id=1)
        field_label = message._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Контактный адрес почты')

    def test_grant_message_label(self):
        message = WriteUs.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEquals(field_label, 'Ваше сообщение')






class QuestionsAndAnswersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        QuestionsAndAnswers.objects.create(question ='В каких валютах могут выдаваться гранты и инвестиции?', answer = 'Гранты и инвестиции могут выдаваться в четырех валютах - в Американских долларах, Российских рублях, Кыргызских сомах, и евро')

    def test_question_label(self):
        invest = QuestionsAndAnswers.objects.get(id=1)
        field_label = invest._meta.get_field('question').verbose_name
        self.assertEquals(field_label, 'Вопрос')

    def test_answer_label(self):
        invest = QuestionsAndAnswers.objects.get(id=1)
        field_label = invest._meta.get_field('answer').verbose_name
        self.assertEquals(field_label, 'Ответ')