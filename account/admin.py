from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","date_joined","last_login","is_superuser")
    search_fields = ("first_name","last_name","email")
    readonly_fields = ("uid","date_joined","last_login")