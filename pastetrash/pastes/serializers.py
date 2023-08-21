from django.contrib.auth.models import User
from pastes.models import Paste
from rest_framework import serializers

class PasteInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paste
        fields = ['title', 'content', 'syntax', 'password']

class PasteBaseSerializer(serializers.HyperlinkedModelSerializer):
    isProtected = serializers.BooleanField(source='is_protected')

    class Meta:
        model = Paste
        fields = ['title', 'slug', 'isProtected']

class PasteListSerializer(PasteBaseSerializer):
    pass

class PasteSerializer(PasteBaseSerializer):
    class Meta(PasteBaseSerializer.Meta):
        fields = PasteBaseSerializer.Meta.fields + ['content']
