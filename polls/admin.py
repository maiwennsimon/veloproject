from django.contrib import admin

from polls.models import Bike, CustomUser
from django.contrib.admin.models import LogEntry


class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'color', 'brand')


admin.site.register(Bike, BikeAdmin)
admin.site.register(CustomUser)
admin.site.register(LogEntry)