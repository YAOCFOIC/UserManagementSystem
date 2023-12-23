from django.contrib import admin
from .models import CustomUser
@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('first_name','email')
    list_display = ('id','first_name','email')
    def datas(self, obj):
        return obj.first_name.upper()