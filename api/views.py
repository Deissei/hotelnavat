from rest_framework import viewsets

from api.serializers import RoomsSerialzier, RoomEquipmentSerializer, CategoryRoomsSerializer
from api.models import CategoryRooms, Rooms, RoomEquipment
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryRoomsViewSet(viewsets.ModelViewSet):
    queryset = CategoryRooms.objects.all()
    serializer_class = CategoryRoomsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerialzier
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomsEquipmentViewSet(viewsets.ModelViewSet):
    queryset = RoomEquipment.objects.all()
    serializer_class = RoomEquipmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
