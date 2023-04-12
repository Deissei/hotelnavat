from rest_framework import serializers

from api.models import BookingRoom, CategoryRooms, RoomEquipment, Rooms


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


class BookingRoomSerializer(serializers.ModelSerializer):
    """Сериализатор Бронирование Комнат"""

    visitor = serializers.SlugRelatedField(slug_field="username", read_only=True)
    room = serializers.SlugRelatedField(slug_field="title", queryset=Rooms.objects.all())

    class Meta:
        model = BookingRoom
        exclude = ('id', )