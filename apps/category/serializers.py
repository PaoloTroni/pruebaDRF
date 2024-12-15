from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(required=False, allow_null=True)
    #sub_categories = serializers.SerializerMethodField()
    class Meta:
        model=Category
        fields=[
            'id',
            'name',
            'thumbnail',
            'description',  
           #'sub_categories',       
        ]
    
    def get_sub_categories(self, obj):
        if obj.id is not None:
            return CategorySerializer(obj.children.all(), many=True).data
            #sub_categories = Category.objects.filter(parent=obj.id)
        return None