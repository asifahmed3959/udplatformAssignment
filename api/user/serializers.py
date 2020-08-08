from rest_framework import serializers

from base.models import Parent
from base.models import Child


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('id', 'first_name', 'last_name')


class UserListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Parent
        fields = ('id', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip', 'children')

    def get_children(self, user):
        queryset = user.children.all()
        serializer = ChildSerializer(queryset, many=True)
        return serializer.data
