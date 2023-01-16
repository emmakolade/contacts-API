from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields =[
            'is_favourite', 'phone_number', 'contact_picture', 'last_name', 'first_name', 'country_code'
        ]