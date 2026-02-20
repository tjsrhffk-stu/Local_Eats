from django.contrib import admin
from .models import Reservation, Visit

admin.site.register(Reservation)
admin.site.register(Visit)