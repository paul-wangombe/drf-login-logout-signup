from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('users', views.AccountsViewSet)
urlpatterns = router.urls


