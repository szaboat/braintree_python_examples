# these requires are necessary on OSX 10.6.x to prevent
# thread issues
import urllib2
urllib2.install_opener(urllib2.build_opener())

import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from config import config

import braintree
import web
import payment_form

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    config['BRAINTREE_MERCHANT_ID'],
    config['BRAINTREE_PUBLIC_KEY'],
    config['BRAINTREE_PRIVATE_KEY'],
)

urls = (
    "/", "Payment",
    "/payments/new", "Payment",
    "/payments/confirm", "Confirm"
)

app = web.application(urls, globals())
render = web.template.render("templates", base="layout")

class Payment:
    def GET(self):
        return render.new_payment(
            payment_form.PaymentForm().form(),
            0,
            braintree.TransparentRedirect.url()
        )

class Confirm:
    def GET(self):
        # remove leading ? from query string
        query_string = web.ctx.query[1:]
        result = braintree.TransparentRedirect.confirm(query_string)
        if result.is_success:
            return render.confirm_payment(result.transaction)
        else:
            return render.new_payment(
                payment_form.PaymentForm(result.params, result.errors).form(),
                len(result.errors),
                braintree.TransparentRedirect.url()
            )

if __name__ == "__main__":
    app.run()
