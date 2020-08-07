from django.urls import include,path

from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'parents', views.UserModelViewSet, basename='parent')

user_router = DefaultRouter()
user_router.register(r'children', views.ChildrenModelViewSet, basename='child')

urlpatterns = [
    path('',include(router.urls)),
    path('parents/<uuid:parent_id>/', include(user_router.urls))

]