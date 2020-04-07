from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Contacts

# Create your views here.
def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

    if request.user.is_authenticated:
        has_contacted = Contacts.objects.all().filter(user_id=user_id, listing_id=listing_id)
        if has_contacted:
            messages.error(request, 'you have already made a request')
            return redirect('/listings/'+listing_id)


    contactt = Contacts(user_id=user_id, listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)
    contactt.save()
    messages.success(request, 'You has been placed successfully')
    return redirect('/listings/'+listing_id)