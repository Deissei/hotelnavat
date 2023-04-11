from django.contrib import admin

from .models import CategoryRooms, RoomEquipment, Rooms


class AdminRooms(admin.ModelAdmin):
    list_display = ['title', 'category', 'priceInDay']

admin.site.register(Rooms, AdminRooms)
admin.site.register(CategoryRooms)
admin.site.register(RoomEquipment)