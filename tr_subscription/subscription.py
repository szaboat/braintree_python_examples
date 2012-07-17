# these requires are necessary on OSX 10.6.x to prevent
# thread issues
import urllib2
urllib2.install_opener(urllib2.build_opener())

import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
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
    "/", "Subscription",
    "/subscriptions/new", "Subscription",
    "/subscriptions/confirm/", "Confirm",
)

app = web.application(urls, globals())
render = web.template.render("templates", base="layout")


class Subscription:
    def GET(self):
        return render.new_subscription(
            payment_form.PaymentForm().form(),
            0,
            braintree.TransparentRedirect.url())


class Confirm:
    def GET(self):
        # remove leading ? from query string
        query_string = web.ctx.query[1:]
        confirm_result = braintree.TransparentRedirect.confirm(query_string)
        import pdb;pdb.set_trace()
        if confirm_result.is_success:
            token = confirm_result.customer.credit_cards[0].token
            subscription_result = braintree.Subscription.create({
                "payment_method_token": token,
                "plan_id": "plan_1",
            })
            if subscription_result.is_success:
                return render.confirm_subscription(subscription_result.subscription)
            else:
                return render.new_subscription(
                            payment_form.PaymentForm(confirm_result.params, confirm_result.errors).form(),
                            len(confirm_result.errors),
                            braintree.TransparentRedirect.url())
        else:
            return render.new_subscription(
                payment_form.PaymentForm(confirm_result.params, confirm_result.errors).form(),
                len(confirm_result.errors),
                braintree.TransparentRedirect.url())

if __name__ == "__main__":
    app.run()
