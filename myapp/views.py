from django.db.models import Q
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from myapp.models import User, Contact
from myapp.serializers import UserSerializer, ContactSerializer

# Create your views here.
@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_users(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many = True)
    return HttpResponse(serializer.data)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def search_user_by_name(request):
    name = request.GET.get("name", None)

    if name is None:
        return HttpResponse("Didn't provide a Name", status.HTTP_400_BAD_REQUEST)
    
    queryset = User.objects.filter(Q(name__startswith = name) | Q(name__contains = name))

    # Compute spam likelihood
    # 
    # queryset = User.objects.filter(
    #     Q(name__startswith = name) | Q(name__contains = name)
    # ).annotate(
    #     total_contacts = Count('pk'),
    #     spam_contacts = Count('pk', filter = Q(is_spam = True))
    # ).annotate(
    #     spam_likelihood = Case(
    #         When(total_contacts = 0, then = 0.0),
    #         default = ExpressionWrapper(
    #             F('spam_contacts') * 1.0 / F('total_contacts'),
    #             output_field = FloatField()
    #         ),
    #         output_field = FloatField()
    #     )
    # )

    serializer = UserSerializer(queryset, many = True)
    
    return HttpResponse(serializer.data, status.HTTP_200_OK)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def search_user_by_phone_number(request):
    phone_number = request.GET.get("phone_number", None)

    if phone_number is None:
        return HttpResponse("Didn't provide a phone number", status.HTTP_400_BAD_REQUEST)
        
    queryset = User.objects.filter(phone_number = phone_number)

    if not queryset.first():
        queryset = Contact.objects.filter(contact_number = phone_number)
        serializer = ContactSerializer(queryset, many = True)
        
        return HttpResponse(serializer.data, status.HTTP_200_OK)

    serializer = UserSerializer(queryset, many = True)
    return HttpResponse(serializer.data, status.HTTP_200_OK)
