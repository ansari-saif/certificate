from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'unique_code')
    search_fields = ('name', 'email', 'unique_code')
admin.site.register(UserProfile,UserProfileAdmin)
