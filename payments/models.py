from django.db import models

from users.models import Connect4ProUser


class Customer(models.Model):
    user = models.OneToOneField(Connect4ProUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Order(models.Model):
    amount = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.customer.user.email} - {self.amount}'

    def save(self, *args, **kwargs):
        if self.start_date:
            self.customer.user.is_premium = True
            self.customer.user.save()
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Оплата премиум-аккаунта'
        verbose_name_plural = 'Оплаты премиум-аккаунта'
