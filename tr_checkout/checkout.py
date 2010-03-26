# these requires are necessary on OSX 10.6.x to prevent
# thread issues
import urllib2
urllib2.install_opener(urllib2.build_opener())

import braintree
import web
import payment_form

braintree.Configuration.configure(
    braintree.Environment.Development,
    "integration_merchant_id",
    "integration_public_key",
    "integration_private_key"
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
            braintree.Transaction.transparent_redirect_create_url()
        )

class Confirm:
    def GET(self):
        query_string = web.ctx.query[1:]
        result = braintree.Transaction.confirm_transparent_redirect(query_string)
        if result.is_success:
            return render.confirm_payment(result.transaction)
        else:
            return render.new_payment(
                payment_form.PaymentForm(result.params, result.errors).form(),
                len(result.errors),
                braintree.Transaction.transparent_redirect_create_url()
            )

if __name__ == "__main__":
    app.run()
