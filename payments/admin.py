from django.contrib import admin
from . models import Payment
# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking','payment_method','status','transaction_time','amount']
    