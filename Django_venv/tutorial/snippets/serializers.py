from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    # problem: 
    # 1. what is ReadOnlyField?
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner')


class UserSerializer(serializers.ModelSerializer):
    #PrimaryKeyRelatedField:may be used to represent the target of the relationship using its primary key.
    # problem: 
    # 1. what is many?
    # answer 1: apply a many to relationship
    # 2. PrimaryKeyRelatedField example play
    # answer 2: reverse relation, related_name = snippets will call back to auth.User
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
