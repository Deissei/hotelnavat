from rest_framework import serializers
from .models import CategoryRooms, Rooms, RoomEquipment


class RoomsSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
        