import web
import braintree

class PaymentForm(object):
    def __init__(self, params={}, errors=braintree.ValidationErrorCollection()):
        self.params = params
        self.errors = errors

    def form(self):
        form = self.__build_form()
        return form()

    def __build_form(self):
        return web.form.Form(
            web.form.Textbox(
                description="First Name",
                name="customer[first_name]",
                id="customer_customer_first_name",
                value=self.__get_nested_param("customer", "first_name"),
                post=self.__error_message(self.errors.for_object("customer").for_object("customer").on("first_name")),
                class_=self.__error_class(self.errors.for_object("customer").for_object("customer").on("first_name"))
            ),
            web.form.Textbox(
                description="Last Name",
                name="customer[last_name]",
                id="customer_customer_last_name",
                value=self.__get_nested_param("customer", "last_name"),
                post=self.__error_message(self.errors.for_object("customer").for_object("customer").on("last_name")),
                class_=self.__error_class(self.errors.for_object("customer").for_object("customer").on("last_name"))
            ),
            web.form.Textbox(
                description="Email",
                name="customer[email]",
                id="customer_customer_email",
                value=self.__get_nested_param("customer", "email"),
                post=self.__error_message(self.errors.for_object("customer").for_object("customer").on("email")),
                class_=self.__error_class(self.errors.for_object("customer").for_object("customer").on("email"))
            ),
            web.form.Textbox(
                description="Number",
                name="customer[credit_card][number]",
                id="customer_credit_card_number",
                value=self.__get_nested_param("customer", "credit_card", "number"),
                post=self.__error_message(self.errors.for_object("customer").for_object("credit_card").on("number")),
                class_=self.__error_class(self.errors.for_object("customer").for_object("credit_card").on("number"))
            ),
            web.form.Textbox(
                description="Expiration Date",
                name="customer[credit_card][expiration_date]",
                id="customer_credit_card_exipration_date",
                value=self.__get_nested_param("customer", "credit_card", "expiration_date"),
                post=self.__error_message(self.errors.for_object("customer").for_object("credit_card").on("expiration_date")),
                class_=self.__error_class(self.errors.for_object("customer").for_object("credit_card").on("expiration_date"))
            ),
            web.form.Textbox(
                description="CVV",
                name="customer[credit_card][cvv]",
                id="customer_credit_card_cvv",
                value=self.__get_nested_param("customer", "credit_card", "cvv"),
                post=self.__error_message(self.errors.for_object("customer").for_object("credit_card").on("cvv")),
                class_=self.__error_class(self.errors.for_object("customer").for_object("credit_card").on("cvv"))
            ),
            web.form.Hidden(
                "tr_data",
                value=braintree.Customer.tr_data_for_create({}, "http://localhost:8080/subscriptions/confirm/")
            )
        )

    def __error_class(self, errors):
        if len(errors) == 0:
            return ""
        else:
            return "error"

    def __error_message(self, errors):
        if len(errors) == 0:
            return ""
        else:
            message = "<div class=\"errors\">"
            message += " ".join([error.message for error in errors])
            return message + "</div>"

    def __get_nested_param(self, *keys):
        val = self.params.get(keys[0])
        for key in keys[1:]:
            val = val and val.get(key)
        return val

