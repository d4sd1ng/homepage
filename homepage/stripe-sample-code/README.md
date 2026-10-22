# Accept a Payment with Stripe Checkout

Stripe Checkout is the fastest way to get started with payments. Included are some basic build and run scripts you can use to start up the application.

## Set Price ID

In the server code, replace `{{PRICE_ID}}` with a Price ID (`price_xxx`) that you created.

## Running the sample

The server loads `STRIPE_SECRET_KEY` from `~/.config/nurovelle-stripe/.env`.
Keep this file outside the repository and webroot with permissions `600`.
Set `NUROVELLE_STRIPE_ENV_FILE` to use another private location, or provide
`STRIPE_SECRET_KEY` through the process environment. The server stops if the
key is missing or empty. Never put secret keys in HTML, public files or Git.

The sample is not a completed package checkout: price and integration IDs still
need configuration. No payment or webhook verification is implied.

1. Build the server

~~~
bundle install
~~~

2. Run the server

~~~
ruby server.rb -o 0.0.0.0
~~~

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)
