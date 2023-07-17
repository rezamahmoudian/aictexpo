from django.contrib.auth import get_user_model
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.HyperlinkedIdentityField(view_name='user-detail', format='html')
    # username = serializers.ReadOnlyField()

    class Meta:
        model = get_user_model()
        fields = "__all__"

