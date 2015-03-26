from django.contrib import admin
from .models import City, Country, Currency, CityInfo, Section, Listing

admin.site.register(CityInfo)
admin.site.register(Section)
admin.site.register(Listing)


class CityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'country')
    list_display = ('name', 'country')

admin.site.register(City, CityAdmin)

class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'continent', 'phone', 'capital')

admin.site.register(Country, CountryAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    list_display = ('name', 'symbol', 'code')

admin.site.register(Currency, CurrencyAdmin)

# Register your models here.
