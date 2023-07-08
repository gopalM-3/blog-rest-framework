from rest_framework import serializers
from blog.models import Blog
from users.models import BlogUser


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = ('id', 'user_name', 'full_name',)


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'slug',
            'category',
            'excerpt',
            'content',
            'author',
            'status',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = str(instance.author)
        representation['category'] = str(instance.category)
        return representation
