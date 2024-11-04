from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost, Category, Tag, Reaction, Comment, UserProfile

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ReactionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Reaction
        fields = ['id', 'user', 'post', 'reaction_type']

class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    reactions = ReactionSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    love_count = serializers.SerializerMethodField()
    angry_count = serializers.SerializerMethodField()
    sad_count = serializers.SerializerMethodField()
    wow_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'reactions', 
                  'created_at', 'updated_at', 'like_count', 'love_count', 
                  'angry_count', 'sad_count', 'wow_count']

    def get_like_count(self, obj):
        return obj.reactions.filter(reaction_type='like').count()

    def get_love_count(self, obj):
        return obj.reactions.filter(reaction_type='love').count()

    def get_angry_count(self, obj):
        return obj.reactions.filter(reaction_type='angry').count()

    def get_sad_count(self, obj):
        return obj.reactions.filter(reaction_type='sad').count()

    def get_wow_count(self, obj):
        return obj.reactions.filter(reaction_type='wow').count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'status', 'created_at']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
