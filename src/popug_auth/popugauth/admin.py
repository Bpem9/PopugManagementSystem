from django.contrib import admin

from popugauth.models import Popug


@admin.register(Popug)
class PopugAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'role', )
