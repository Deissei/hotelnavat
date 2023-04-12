from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import BookingRoom, CategoryRooms, RoomEquipment, Rooms
from api.permissions import ISOwner
from api.serializers import (BookingRoomSerializer, CategoryRoomsSerializer,
                             RoomEquipmentSerializer, RoomsSerialzier)


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


class BookingRoomViewSet(viewsets.ModelViewSet):
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer

    permission_by_action = {
        'list': [IsAuthenticatedOrReadOnly],
        'create': [IsAuthenticatedOrReadOnly],
        'retrieve': [IsAuthenticatedOrReadOnly],
        'update': [ISOwner],
        'delete': [ISOwner]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


    def perform_create(self, serializer):
        serializer.save(user=self.request.visitor)
