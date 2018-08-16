from django.urls import path
from rest_framework_mongoengine import routers

from .views import DishListCreate


#router = routers.DefaultRouter()
#router.register(r'api/dishes', DishViewSet)
urlpatterns = [
    path('api/dishes/', DishListCreate.as_view()),
]

#urlpatterns += router.urls
