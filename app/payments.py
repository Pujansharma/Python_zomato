import stripe

# Set your Stripe API key (replace with your actual Stripe API key)
stripe.api_key = 'your_stripe_api_key_here'

def process_payment(amount):
    try:
        # Create a payment intent with the specified amount (in cents)
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert amount to cents
            currency='usd',  # Replace with your preferred currency
        )

        # If the payment intent is successful, return True
        if payment_intent.status == 'succeeded':
            return True
        else:
            return False
    except stripe.error.StripeError as e:
        # Handle Stripe errors (e.g., card declined)
        # You can log the error or perform other error handling here
        return False
