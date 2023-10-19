from rest_framework import serializers
from .models import Country, Brand, Car, Comment


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'brands']
        depth = 1


class BrandSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta:
        model = Brand
        fields = ['id', 'name', 'country', 'cars', 'comments_count', 'country_id']
        depth = 1

    def create(self, validated_data):
        validated_data['country'] = validated_data['country_id']
        validated_data.pop('country_id')
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country_id', instance.country)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def get_comments_count(self, instance):
        return Comment.objects.filter(car__brand=instance).count()


class CarSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())

    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'release_year', 'release_end_year', 'comments', 'comments_count', 'brand_id']
        depth = 1

    def create(self, validated_data):
        validated_data['brand'] = validated_data['brand_id']
        validated_data.pop('brand_id')
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand_id', instance.brand)
        instance.name = validated_data.get('name', instance.name)
        instance.release_year = validated_data.get('release_year', instance.release_year)
        instance.release_end_year = validated_data.get('release_end_year', instance.release_end_year)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    car_id = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'email', 'car', 'text', 'created_at', 'car_id']
        depth = 1

    def create(self, validated_data):
        validated_data['car'] = validated_data['car_id']
        validated_data.pop('car_id')
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.car = validated_data.get('car_id', instance.car)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
