import braintree
import web
import payment_form

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    "your_merchant_id",
    "your_public_key",
    "your_private_key"
)
braintree.Configuration.use_unsafe_ssl = True

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
        # remove leading ? from query string
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
    app.cgirun()
