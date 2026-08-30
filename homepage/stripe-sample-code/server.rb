require 'stripe'
require 'sinatra'

# This is your test secret API key.
# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
client = Stripe::StripeClient.new('sk_test_51U9Z6jHhj2rcxrubesAFCiel86aMf8jwXEkjszhl02UbjLfUelpEHDLb2ZmaAJhqLdPetnxDeikeVVORWo4RhnvY005iRaqN92')

set :static, true
set :port, 4242

YOUR_DOMAIN = 'http://localhost:4242'

post '/create-checkout-session' do
  content_type 'application/json'

  session = client.v1.checkout.sessions.create({
    line_items: [{
      # Provide the exact Price ID (for example, price_1234) of the product you want to sell
      price: '{{PRICE_ID}}',
      quantity: 1,
    }],
    mode: 'payment',
    success_url: YOUR_DOMAIN + '/success.html',
    # Provide a name (for example, hosted_web_0001) to label this Checkout integration and measure its conversion independently
    integration_identifier: '{{INTEGRATION_ID}}',
  })
  redirect session.url, 303
end