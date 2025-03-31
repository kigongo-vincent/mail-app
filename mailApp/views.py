from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def send_email(request):
    try:
        subject = request.data["subject"]
        message = request.data["body"]
        email_from = "TRAINING HUB"
        recipient_list = ["hello@training-hub.uk"]
        send_mail(subject, message, email_from, recipient_list, html_message="")
        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
