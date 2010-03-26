# tr_checkout_app_engine

## Overview

This code is a demonstration of creating one time transactions using the
Braintree transparent redirect API.  We decided to use the
[web.py](http://webpy.org/) framework because its simplicity
allows us to clearly demonstrate concepts without added noise. This example
was designed to run on Google App Engine. This example is identical to
tr_checkout except:

* the web.py source is placed at the top level of the example
* the braintree package source is placed at the top level of the example
* the braintree package is configured to use unsafe ssl (no certificate verification) because App Engine does not allow access to M2Crypto
* the web.py app is run using the cgirun() method rather than the run() method
* web.py templates were complied using the following command:
  * python web/template.py --compile templates

## Getting Started

To run the exmaple:

* Install the [Google App Engine SDK](http://code.google.com/appengine/downloads.html)
* Update checkout.py with your merchant_id, public_key and private_key
* point the Google App Engine dev server at this project directory:
  * dev_appserver.py tr_checkout_app_engine
* Visit [http://localhost:8080/payments/new](http://localhost:8080/payments/new)

