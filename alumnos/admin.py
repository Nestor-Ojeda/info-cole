from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Alumno, TutorA, TutorB)
class AlumnosAdmin(admin.ModelAdmin):
	pass