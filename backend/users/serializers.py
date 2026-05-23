from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    faculty = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'faculty']
        read_only_fields = fields

    def get_faculty(self, obj):
        profile = getattr(obj, 'staff_profile', None)
        if profile:
            return {
                'id': profile.faculty_id,
                'name': profile.faculty.name,
                'short_name': profile.faculty.short_name,
            }
        return None