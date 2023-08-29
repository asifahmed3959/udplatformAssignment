from django.shortcuts import Http404

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from base.models import Parent
from base.models import Child

from .serializers import UserListSerializer
from .serializers import ChildSerializer


#CRUD Operation for the Parent Model
class UserModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Parent.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'parent_id'

    def get_object(self):
        obj = self.queryset.filter(id=self.kwargs.get('parent_id')).first()

        if obj is None:
            raise Http404

        return obj


#CRUD Operation for the Children Model
class ChildrenModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = ChildSerializer
    lookup_field = 'child_id'

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        self._parent = Parent.objects.filter(id=self.kwargs.get('parent_id', None)).first()

        if self._parent is None:
            raise Http404

    def get_object(self):
        obj = self.get_queryset().filter(id=self.kwargs.get('child_id')).first()

        if obj is None:
            raise Http404

        return obj

    def get_queryset(self):
        return Child.objects.filter(parent_id=self.kwargs.get('parent_id'))

    def perform_create(self, serializer):
        serializer.save(parent=self._parent)