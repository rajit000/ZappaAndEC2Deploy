from rest_framework import serializers

class StudentList_s(serializers.Serializer):
    first_name = serializers.CharField(required=False,allow_blank=False,allow_null=True)
    last_name = serializers.CharField(required=False,allow_blank=False,allow_null=True)
    email = serializers.CharField(required=False,allow_blank=False,allow_null=True)
    ProfileImage = serializers.FileField(required=False)
    class Meta:
        fields='__all__'