from django.urls import path

from .views import CancelledView, SuccessView, create_checkout_session, stripe_config, stripe_webhook

app_name = 'payment'

urlpatterns = [
  path('config/', stripe_config),
  path('create-checkout-session/', create_checkout_session),
  path('success/', SuccessView.as_view()),
  path('cancelled/', CancelledView.as_view()),
  path('webhook/', stripe_webhook),
]