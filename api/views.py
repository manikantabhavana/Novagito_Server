from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Customer,Testinominal,Query
import logging
import json

logger = logging.getLogger(__name__)
def customer_list(request):
    customers = Customer.objects.all()
    data = [{'name': customer.name, 'company': customer.company, 'mail': customer.mail, 'location': customer.location,'industry': customer.industry, 'about': customer.about, 'review': customer.review, 'rating': customer.rating,'photo_url': customer.photo_url,'problem': customer.problem,'solution': customer.solution,'output1': customer.output1,'output1_text': customer.output1_text,'output2': customer.output2,'output2_text': customer.output2_text,'output3': customer.output3,'output3_text': customer.output3_text} for customer in customers]
    return JsonResponse(data, safe=False)

def testinominal_list(request):
    testinominals = Testinominal.objects.all()
    data = [{'name': testinominal.name, 'company': testinominal.company,  'review': testinominal.review, 'rating': testinominal.rating,'photo_url': testinominal.photo_url} for testinominal in testinominals]
    return JsonResponse(data, safe=False)

def query_list(request):
    if request.method == 'GET':
        queries = Query.objects.all()
        data = [{'first_name': query.first_name, 'last_name': query.last_name,  'email': query.email, 'mobile': query.mobile,'message': query.message,'date':query.date} for query in queries]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from request body
        logger.info(f'Received data: {data}') # Assuming form data is sent using POST method
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        mobile = data.get('mobile')
        message = data.get('message')
        date=data.get('date')
        
        # Create a new Query object with the received data
        query = Query.objects.create(first_name=first_name, last_name=last_name, email=email, mobile=mobile, message=message,date=date)
        #send_email_notification(query)
        return JsonResponse({'message': 'Query created successfully'}, status=201)



def send_email_notification(query):
    subject = 'New Query Submitted'
    message = f'Name: {query.first_name} {query.last_name}\nEmail: {query.email}\nMobile: {query.mobile}\nMessage: {query.message}\nDate: {query.date}'
    recipient_list = ['manikanta.7828@gmail.com']  # Replace with your email address
    sender_email = 'manikanta.7828@gmail.com'  # Replace with your email address
    send_mail(subject, message, sender_email, recipient_list)