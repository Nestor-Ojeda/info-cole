
from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Depto)
class DeptoAdmin(admin.ModelAdmin):
	pass