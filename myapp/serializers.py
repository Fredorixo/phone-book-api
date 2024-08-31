from rest_framework import serializers
from myapp.models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    # spam_likelihood = serializers.FloatField(read_only = True)

    class Meta:
        model = User
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        request = self.context.get("request", None)
        user = request.user if request else None

        if not user:
            return representation

        current_user = user.first_name + user.last_name
        
        contact_list = [contact.contact_number for contact in Contact.objects.filter(user_details = instance.phone_number)]
        user_list = [user.name for user in User.objects.filter(phone_number__in = contact_list)]

        if current_user not in user_list:
            representation.pop("email")
        
        return representation

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["alias"]