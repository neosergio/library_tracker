from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'libraries', views.LibraryViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'library_books', views.LibraryBookViewSet)
router.register(r'library_activities', views.LibraryActivityViewSet)

api_urlpatterns = router.urls
