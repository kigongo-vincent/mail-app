from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def getHtmlContent(full_name, email, phone, service, booking_date, number_of_people, duration):
    return f"""
    <html>
        <head>
            <title>Training Hub Booking Confirmation</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                h2 {{ color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 10px; }}
                .summary {{ background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 20px 0; }}
                .summary p {{ margin: 8px 0; }}
                .footer {{ margin-top: 30px; padding-top: 15px; border-top: 1px solid #eee; font-size: 0.9em; }}
            </style>
        </head>
        <body>
            <div class='container'>
                <h2>Thank You for Your Booking Request</h2>
                <p>Dear {full_name},</p>
                <p>We have received your booking request for the Training Hub. Here is a summary of your request:</p>
                
                <div class='summary'>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Service Type:</strong> {service}</p>
                    <p><strong>Booking Date:</strong> {booking_date}</p>
                    <p><strong>Number of People:</strong> {number_of_people}</p>
                    <p><strong>Duration:</strong> {duration}</p>
                    <p><strong>Phone number:</strong> {phone}</p>
                </div>
                
                <p>Our team will review your request and get back to you shortly.</p>
                <p>If you have any questions, please feel free to contact us.</p>
                
                <div class='footer'>
                    <p>Best regards,</p>
                    <p>The Training Hub Team</p>
                </div>
            </div>
        </body>
    </html>
    """
    return 

@api_view(['POST', 'GET'])
def send_email(request):
    
    if request.method == "GET":
        return Response({"full_name": "string", "email": "string", "phone": "string", "service": "string", "booking_date": "string", "number_of_people": "number", "duration": "number"})
    
    # try:
    subject = "Thank you for your Training Hub booking request"
    email_from = request.data["email"]
    recipient_list = ["hello@training-hub.uk", request.data["email"]]
    mail = send_mail(subject=subject, message="",from_email= email_from,recipient_list= recipient_list, html_message=getHtmlContent(full_name=request.data["full_name"], email=request.data["email"], phone=request.data["phone"], service=request.data["service"], booking_date=request.data["booking_date"],number_of_people= request.data["number_of_people"], duration=request.data["duration"]))
    return Response(status=status.HTTP_201_CREATED)
    # except:
        # return Response(status=status.HTTP_400_BAD_REQUEST)
        
