from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from kitchen.models import Cook, DishType, Dish

admin.site.unregister(Group)
admin.site.register(DishType)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("years_of_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info",
                                                {"fields": ("first_name", "last_name", "years_of_experience",)}),)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "dish_type", ]
    list_filter = ["name", "price", ]
    search_fields = ["name", ]



