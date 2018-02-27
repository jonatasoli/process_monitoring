from django.contrib import admin
from core.models import StatusProcess, UserProfile


class StatusProcessModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'id_process', 'status_process')
    search_fields = ('user_profile', 'id_process', 'status_process')
    list_filter = ('user_profile',)


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'url', 'password')
    search_fields = ('email', 'name', 'url')


admin.site.register(UserProfile, UserProfileModelAdmin)
admin.site.register(StatusProcess, StatusProcessModelAdmin)
