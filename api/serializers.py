from rest_framework import serializers

from .models import CategoryRooms, RoomEquipment, Rooms


class RoomEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomEquipment
        fields = '__all__'


class RoomsSerialzier(serializers.ModelSerializer):
    roomEquipment = RoomEquipmentSerializer(many=True)

    class Meta:
        model = Rooms
        fields = '__all__'
        

class CategoryRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRooms
        fields = '__all__'


