import web
import braintree

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

class PaymentForm(object):
    def __init__(self, params={}):
        self.params = params

    def form(self):
        form = self.__build_form()
        return form()

    def __build_form(self):
        return web.form.Form(
            web.form.Textbox(description="First Name", name="transaction[customer][first_name]", id="transaction_customer_first_name"),
            web.form.Textbox(description="Last Name", name="transaction[customer][last_name]", id="transaction_customer_last_name"),
            web.form.Textbox(description="Email", name="transaction[customer][email]", id="transaction_customer_email"),
            web.form.Textbox(description="Number", name="transaction[credit_card][number]", id="transaction_credit_card_number"),
            web.form.Textbox(description="Expiration Date", name="transaction[credit_card][expiration_date]", id="transaction_credit_card_exipration_date"),
            web.form.Textbox(description="Cvv", name="transaction[credit_card][cvv]", id="transaction_credit_card_cvv"),
            web.form.Hidden("tr_data", value=braintree.Transaction.tr_data_for_sale({"transaction": {"amount": "100.00"}}, "http://localhost:8080/payments/confirm"))
        )

class Payment:
    def GET(self):
        return render.new_payment(PaymentForm().form(), braintree.Transaction.transparent_redirect_create_url())

class Confirm:
    def GET(self):
        query_string = web.ctx.query[1:]
        print query_string
        braintree.Transaction.confirm_transparent_redirect(query_string)
        return "hi"

if __name__ == "__main__":
    app.run()
