from rest_framework import routers

from api.views import CategoryRoomsViewSet, RoomsViewSet, RoomsEquipmentViewSet, BookingRoomViewSet


router = routers.DefaultRouter()
router.register('category-rooms', CategoryRoomsViewSet, basename='category')

router.register('rooms', RoomsViewSet, basename='room')

router.register('rooms-equipments', RoomsEquipmentViewSet, basename='equipment')

router.register('bookings', BookingRoomViewSet, basename='booking')


urlpatterns = router.urls
