from rest_framework import routers
from .views import BooksViewSet
 
router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
 
urlpatterns = router.urls