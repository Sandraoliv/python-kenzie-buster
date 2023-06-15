from rest_framework import serializers
from movies.models import RATING_CHOICES
from movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField( 
        choices=RATING_CHOICES.choices, default=RATING_CHOICES.G)
    synopsis = serializers.CharField(default=None)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
    
    def update(self, instance: Movie, validated_data: dict) -> Movie:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance  
        

