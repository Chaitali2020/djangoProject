from django.contrib import admin
from .models import food

class foodAdmin(admin.ModelAdmin):
    list_display=['id','fname','fqty','fdetails','fimg']

# Register your models here.
# admin.site.register(food)
admin.site.register(food,foodAdmin)

admin.site.site_header="Food Management Admin Panel"

admin.site.site_title="Food Items"
