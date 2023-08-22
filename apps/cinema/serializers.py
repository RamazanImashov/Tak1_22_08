from rest_framework import serializers
from .models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['actors'] = ActorSerializer(instance.actors.all(), many=True).data
        return rep