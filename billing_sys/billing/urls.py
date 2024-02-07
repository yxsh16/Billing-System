from django.urls import path
from billing_sys.billing.views import billing_home, checkout_session

app_name = "billing"

urlpatterns = [
    path("", view=billing_home, name="home"),
    path("checkout", view=checkout_session, name="checkout")
]
