from config.settings import STRIPE_SECRET_KEY
import stripe


class CreateCheckoutSession:

    def __init__(self):
        stripe.api_key = STRIPE_SECRET_KEY

    def create_payment(self, currency, amount):
        amount = amount
        currency = currency
        payment_method = ['card']

        product = stripe.Product.create(name="Gold Special")
        price = stripe.Price.create(
            unit_amount=amount,
            currency=currency,
            recurring={"interval": "month"},
            product=product,
        )

        stripe.checkout.Session.create(
            payment_method=payment_method,
            success_url="https://example.com/success",
            line_items=[
                {
                    "price": price,
                    "quantity": 1,
                },
            ],
            mode="subscription",
        )
