from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')
    list_display = ('username', 'email', 'is_superuser')

admin.site.register(User, UserAdmin)