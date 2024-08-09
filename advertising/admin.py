from django.contrib import admin
from .models import Category, City, Advert

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    readonly_fields = ('views',)

admin.site.register(Category)
admin.site.register(City)