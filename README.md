# E-commerce website using Stripe and Flask

## Method:

- Clone this repo.
- Create a stripe account (https://dashboard.stripe.com/register).
- Toggle on View test data on left hand side of page.
- Replace publishable key and secret key on line 7 & 8 in app.py with your own test keys (make sure you can see test near the start of the key).
- Create a test product and save.
- Replace price id on line 22 of app.py with the Pricing API ID for the product.
- run: pipenv install -r requirements.txt.
- open new terminal and run stripe listen --forward-to 127.0.0.1:5000/stripe_webhook and replace the endpoint_secret on line 47 of app.py with the webhook signing secret given.
- In the original terminal:
  - open shell: pipenv shell
  - run code: flask run
- Open up website at http://127.0.0.1:5000/
- Click Buy Now
- Enter payment details
  - Any email
  - 4242 4242 4242 4242 for long card number in production
  - Any future expiry date
  - Any 3 digit CVC
  - Any Name
  - Any PostCode
- CLick pay and see payments in stripe account
