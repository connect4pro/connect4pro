from django.urls import path

from payments.views import pay_premium, pay_success, pay_result, pay_failure

app_name = 'payments'

urlpatterns = [
    path('paybox', pay_premium, name='paybox_init'),
    path('paybox-success', pay_success, name='paybox_success'),
    path('paybox-result', pay_result, name='paybox_result'),
    path('paybox-failure', pay_failure, name='paybox_failure'),
]
