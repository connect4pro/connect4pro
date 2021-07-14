from django.contrib import admin

from payments.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'amount', 'get_start_date', 'get_end_date', 'status', 'pg_payment_id')
    list_filter = ['customer__user__start_date', 'customer__user__end_date', 'status']
    search_fields = ['pg_payment_id', 'customer']

    def get_start_date(self, obj):
        return obj.customer.user.start_date

    get_start_date.admin_order_field = 'customer__user__start_date'
    get_start_date.short_description = 'Начало'

    def get_end_date(self, obj):
        return obj.customer.user.end_date

    get_end_date.admin_order_field = 'customer__user__end_date'
    get_end_date.short_description = 'Конец'
