from django.contrib import admin
from .models import Story

# Register your models here.
@admin.register(Story)
class VendorAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Story._meta.fields]