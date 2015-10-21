from django.contrib import admin

from home.models import *

# Register your models here.

class AboutPromoInline(admin.TabularInline):
    model = AboutPromotion

class AboutAdmin(admin.ModelAdmin):
    fields = ('text',)
    inlines = [
        AboutPromoInline,
    ]

admin.site.register(ShopCategory)
admin.site.register(Business)
admin.site.register(CategoryImage)

admin.site.register(AboutPage, AboutAdmin)

admin.site.register(Event)