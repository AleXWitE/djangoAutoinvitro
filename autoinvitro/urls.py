from rest_framework import routers
from .api import NewsViewSet, NotificationViewSet, SaleViewSet, SaleItemViewSet, CarViewSet, ForumViewSet, PostsViewSet

router = routers.DefaultRouter()
router.register('api/new', NewsViewSet, 'new')
router.register('api/notification', NotificationViewSet, 'notifications')
router.register('api/sale', SaleViewSet, 'sale')
router.register('api/saleitem', SaleItemViewSet, 'sale item')
router.register('api/car', CarViewSet, 'car')
router.register('api/forum', ForumViewSet, 'forum')
router.register('api/post', PostsViewSet, 'post')


urlpatterns = router.urls
