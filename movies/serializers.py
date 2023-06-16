from rest_framework import serializers
from movies.models import RATING_CHOICES
from movies.models import MovieOrder
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
    

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source='movie.title', read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.CharField(source='order_user.email', read_only=True)
    buyed_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
        

