from django.contrib import admin

from polls.models import Bike


class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'color', 'brand')

admin.site.register(Bike, BikeAdmin)