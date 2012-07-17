# tr_subscription

## Overview

This code is a demonstration of creating one time transactions using the
Braintree transparent redirect API.  We decided to use the
[web.py](http://webpy.org/) framework because its simplicity
allows us to clearly demonstrate concepts without added noise.

Assuming you have a plan with the following details:

    plan_id: "plan_1"

## Getting started

* pip install braintree
* pip install web.py
* Update config.py with your merchant_id, public_key and private_key
* cd tr_subscription
* python subscription.py
* Visit [http://localhost:8080/payments/new](http://localhost:8080/payments/new)



