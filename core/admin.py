from django.contrib import admin
from core.models import StatusProcess


class StatusProcessModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'id_process', 'status_process')
    search_fields = ('user_profile', 'id_process', 'status_process')
    list_filter = ('user_profile',)


admin.site.register(StatusProcess, StatusProcessModelAdmin)
