from django.contrib import admin
from .models import HomePage

class HomePageAdmin(admin.ModelAdmin):
   fieldsets = [
        (None, {'fields': ['header']}),
        ('Bio', {'fields': ['bio']}),
        ('Headshot', {'fields': ['headshot']}),
    ]

admin.site.register(HomePage, HomePageAdmin)
