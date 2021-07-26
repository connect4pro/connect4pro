from django.db import models

from users.models import Connect4ProUser

STATUS_CHOICES = (
    ('1', 'В процессе'),
    ('2', 'Оплачен'),
    ('3', 'Отменен')
)

class Customer(models.Model):
    user = models.OneToOneField(Connect4ProUser, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Order(models.Model):
    pg_payment_id = models.IntegerField(verbose_name='Id PayBox', null=True, blank=True)
    amount = models.PositiveSmallIntegerField(verbose_name='Сумма')
    description = models.CharField(verbose_name='Описание', max_length=250)
    customer = models.ForeignKey(Customer, verbose_name='Пользователь', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES, default='1', max_length=8)

    def __str__(self):
        return f'{self.customer.user.email} - {self.status}'

    class Meta:
        verbose_name = 'Оплата премиум-аккаунта'
        verbose_name_plural = 'Оплаты премиум-аккаунта'
