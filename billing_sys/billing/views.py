from django.http import HttpRequest
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
import stripe

# Create your views here.

def billing_home(request: HttpRequest):
    return render(request, template_name = 'billing/billing_home.html')


def checkout_session(request: HttpRequest):
    if request.method == "POST":
        stripe.api_key=settings.STRIPE_SECRET_KEY
        if request.user.stripe_customer_id:
            customer_id = request.user.stripe_customer_id
        else:
            customer = stripe.Customer.create(
                email=request.user.email
            )    
            customer_id = customer['id']
            request.user.stripe_customer_id = customer_id
            request.user.save()
            
        session = stripe.checkout.Session.create(
            mode="setup",
            currency="inr",
            customer = customer_id,
            success_url=request.build_absolute_uri(reverse('billing:checkout_success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url="https://example.com/cancel",
        )
        return redirect(session.url, code=303)
    return render(request, template_name= 'billing/checkout_session.html')


def checkout_success(request: HttpRequest):
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    print(session)
    return render(request, template_name='billing/checkout_success.html')