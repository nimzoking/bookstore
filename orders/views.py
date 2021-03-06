import stripe 
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.shortcuts import render 

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request): 
    # --- Review this section, commented out for testing purposes ----
    # --- Use this option to allow users to review orders ----

    # # Get the permission
    # permission = Permission.objects.get(codename='special_status')

    # # Get user
    # u = request.user

    # # Add to user's permission set
    # u.user_permissions.add(permission)

    if request.method == 'POST':
        
        # Stripe Current Charge Method

        charge = stripe.Charge.create(
            amount=5900,
            currency='gbp',
            description='Purchase Handbag',
            source=request.POST['stripeToken']
        )

        return render(request, 'orders/charge.html')

