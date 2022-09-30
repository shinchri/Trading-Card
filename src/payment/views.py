import stripe
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.shortcuts import render
from account.models import CustomUser

from main.models import Cart

# Create your views here.
@csrf_exempt
def stripe_config(request):
  if request.method == 'GET':
    stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
  if request.method == 'GET':
    domain_url = settings.DOMAIN_URL
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:

      cart = Cart.objects.get(user=request.user.id)
      subtotal = 0
      tax = 12

      for order in cart.order_set.all():
        price = order.price
        qty = order.quantity
        subtotal += (price * qty)


      order_total = int((subtotal + tax) * 100) # convert to cents in integer


      # Create new Checkout Session for the order
      # Other optional params include:
      # [billing_address_collection] - to display billing address details on the page
      # [customer] - if you have an existing Stripe Customer ID
      # [payment_intent_data] - capture the payment later
      # [customer_email] - prefill the email input in the form
      # For full details see https://stripe.com/docs/api/checkout/sessions/create

      # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
      checkout_session = stripe.checkout.Session.create(
        client_reference_id=request.user.id if request.user.is_authenticated else None,
        success_url = domain_url + 'payment/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url = domain_url + 'payment/cancelled/',
        payment_method_types=['card'],
        mode='payment',
        line_items=[
          {
            'name': 'FusionTrading',
            'quantity': 1,
            'currency': 'usd',
            'amount': order_total,
          },
        ]
      )
      return JsonResponse({'sessionId': checkout_session['id']})
    except Exception as e:
      return JsonResponse({'error': str(e)})

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

        # Delete all orders from Cart (in later date implement history order section...)
        user_id = int(event['data']['object']['client_reference_id'])

        # check if the user had logged in
        if user_id:
          user = CustomUser.objects.get(id=user_id)
          cart = Cart.objects.get(user=user)

          for order in cart.order_set.all():

            # TODO: put order into history

            # delete
            order.delete()

    return HttpResponse(status=200)

class SuccessView(generic.TemplateView):
  template_name = 'success.html'

class CancelledView(generic.TemplateView):
  template_name = 'cancelled.html'