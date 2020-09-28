from django.contrib import admin

from .models import pets


@admin.register(pets)
class PetAdmin(admin.ModelAdmin):
    pass
