from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['id', 'email', 'username','f_name', 'l_name', 'date_joined', 'last_login', 'is_admin', 'is_staff']
    search_fields = ['id', 'email', 'username','f_name', 'l_name']
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
    
