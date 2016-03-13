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

class EventLinkInline(admin.TabularInline):
  model = EventLink

class EventAdmin(admin.ModelAdmin):
  inlines = [
    EventLinkInline,
  ]

class ShopCategoryAdmin(admin.ModelAdmin):
  fields = ('name',)

admin.site.register(ShopCategory, ShopCategoryAdmin)
admin.site.register(Business)
admin.site.register(CategoryImage)
admin.site.register(AboutPage, AboutAdmin)
admin.site.register(Event, EventAdmin)
