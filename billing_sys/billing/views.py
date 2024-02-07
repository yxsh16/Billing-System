from django.http import HttpRequest
from django.shortcuts import render
import stripe

# Create your views here.

def billing_home(request: HttpRequest):
    return render(request, template_name = 'billing/billing_home.html')


def checkout_session(request: HttpRequest):
    if request.method == "POST":
        session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:4242/success',
    cancel_url='http://localhost:4242/cancel',
  )

        return redirect(session.url, code=303)
    return render(request, template_name= 'billing/checkout_session.html')
