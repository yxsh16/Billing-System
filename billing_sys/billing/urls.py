from django.urls import path
from billing_sys.billing.views import billing_home

app_name = "billing"

urlpatterns = [
    path("", view=billing_home, name="home"),
]
