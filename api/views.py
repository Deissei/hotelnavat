from rest_framework import viewsets

from api.serializers import RoomsSerialzier, RoomEquipmentSerializer, CategoryRoomsSerializer
from api.models import CategoryRooms, Rooms, RoomEquipment


class CategoryRoomsViewSet(viewsets.ModelViewSet):
    queryset = CategoryRooms.objects.all()
    serializer_class = CategoryRoomsSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerialzier


class RoomsEquipmentViewSet(viewsets.ModelViewSet):
    queryset = RoomEquipment.objects.all()
    serializer_class = RoomEquipmentSerializer
    