from django.urls import path

from payments.views import pay_result, pay_premium, pay_success

app_name = 'payments'

urlpatterns = [
    path('paybox-result', pay_result, name='paybox_result'),
    path('paybox', pay_premium, name='paybox_init'),
    path('paybox-success', pay_success, name='paybox-success'),
]
