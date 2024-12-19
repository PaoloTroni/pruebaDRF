from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(required=False, allow_null=True)
    sub_categories = serializers.SerializerMethodField()
    class Meta:
        model=Category
        fields=[
            'id',
            'parent',
            'name',
            'thumbnail',
            'description',  
           'sub_categories',  
        ]
    
    def get_sub_categories(self, obj):
        if not obj.id:  # Verificamos si el objeto tiene un id
            return None
        return CategorySerializer(obj.children.all(), many=True).data