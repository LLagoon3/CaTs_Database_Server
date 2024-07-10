from rest_framework import serializers
from . import models


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = "__all__"


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Letter
        fields = "__all__"


class LoverRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoverRelationship
        fields = "__all__"
