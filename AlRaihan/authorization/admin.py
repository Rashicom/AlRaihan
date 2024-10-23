from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_superuser', 'is_active')
