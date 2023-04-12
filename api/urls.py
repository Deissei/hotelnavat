from rest_framework import routers

from api.views import CategoryRoomsViewSet, RoomsViewSet, RoomsEquipmentViewSet


router = routers.DefaultRouter()
router.register('category-rooms', CategoryRoomsViewSet, basename='category')

router.register('rooms', RoomsViewSet, basename='room')

router.register('rooms-equipments', RoomsEquipmentViewSet, basename='equipment')


urlpatterns = router.urls
