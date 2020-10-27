from rest_framework import serializers
from todos import models

class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.ListItem