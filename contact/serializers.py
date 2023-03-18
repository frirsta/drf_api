from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    accounts_id = serializers.ReadOnlyField(source='owner.accounts.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.accounts.profile_image.url')
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_date(self, obj):
        return naturaltime(obj.created_date)

    def get_updated_date(self, obj):
        return naturaltime(obj.updated_date)

    class Meta:
        model = Contact
        fields = [
            'id', 'owner', 'is_owner', 'accounts_id',
            'profile_image', 'created_date', 'updated_date',
            'title', 'content'

        ]
