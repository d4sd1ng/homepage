require 'dotenv'
require 'stripe'
require 'sinatra'

env_file = File.expand_path(ENV.fetch('NUROVELLE_STRIPE_ENV_FILE', '~/.config/nurovelle-stripe/.env'))
Dotenv.load(env_file)
secret_key = ENV.fetch('STRIPE_SECRET_KEY')
raise 'STRIPE_SECRET_KEY must not be empty' if secret_key.strip.empty?

client = Stripe::StripeClient.new(secret_key)

set :static, true
set :port, 4242

YOUR_DOMAIN = 'http://localhost:4242'

post '/create-checkout-session' do
  content_type 'application/json'

  session = client.v1.checkout.sessions.create({
    line_items: [{
      price: '{{PRICE_ID}}',
      quantity: 1,
    }],
    mode: 'payment',
    success_url: YOUR_DOMAIN + '/success.html',
    integration_identifier: '{{INTEGRATION_ID}}',
  })
  redirect session.url, 303
end
