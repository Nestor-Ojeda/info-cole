from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	pass
