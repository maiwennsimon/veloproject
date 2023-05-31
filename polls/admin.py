from django.contrib import admin

from polls.models import Bike, User
from django.contrib.admin.models import LogEntry


class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'color', 'brand')


admin.site.register(Bike, BikeAdmin)
admin.site.register(User)
admin.site.register(LogEntry)