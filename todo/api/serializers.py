from rest_framework import serializers
from todoapp.models import Tlist

class TlistSerializer(serializers.ModelSerializer):
    completion_date = serializers.ReadOnlyField()
    date_completed = serializers.ReadOnlyField()

    class Meta:
        model = Tlist
        fields = ['id','item','description','completion_date','date_completed']

class TlistCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tlist
        fields = ['id']
        read_only_fields = ['title','item','description','completion_date','date_completed']