from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

#router helps connect views, when a server is turned on, it is listening on a port, and when a request is made,
#the request looks into the list of urls that are available, once connected, it connect with the views

router = DefaultRouter()
router.register(r'parents', views.UserModelViewSet, basename='parent')

user_router = DefaultRouter()
user_router.register(r'children', views.ChildrenModelViewSet, basename='child')

urlpatterns = [
    path('', include(router.urls)),
    path('parents/<uuid:parent_id>/', include(user_router.urls))
]
