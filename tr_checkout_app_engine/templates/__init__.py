from web.template import CompiledTemplate, ForLoop


def confirm_payment():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (transaction):
        yield 'title', join_('Confirm Payment')
        yield '', join_('\n')
        yield '', join_('<h1>Payment Result</h1>\n')
        yield '', join_('\n')
        yield '', join_('<div>Thank you for your payment.</div>\n')
        yield '', join_('\n')
        yield '', join_('<h2>Transaction Details</h2>\n')
        yield '', join_('\n')
        yield '', join_('<table>\n')
        yield '', join_('    <tr><td>Amount:</td><td>', '$', '100.00</td></tr>\n')
        yield '', join_('    <tr><td>Transaction ID:</td><td>', escape_(transaction.id, True), '</td></tr>\n')
        yield '', join_('    <tr><td>First Name:</td><td>', escape_(transaction.customer_details.first_name, True), '</td></tr>\n')
        yield '', join_('\n')
        yield '', join_('    <tr><td>Last Name:</td><td>', escape_(transaction.customer_details.last_name, True), '</td></tr>\n')
        yield '', join_('    <tr><td>Email:</td><td>', escape_(transaction.customer_details.email, True), '</td></tr>\n')
        yield '', join_('    <tr><td>Credit Card:</td><td>', escape_(transaction.credit_card_details.masked_number, True), '</td></tr>\n')
        yield '', join_('    <tr><td>Card Type:</td><td>', escape_(transaction.credit_card_details.card_type, True), '</td></tr>\n')
        yield '', join_('</table>\n')
    return __template__

confirm_payment = CompiledTemplate(confirm_payment(), 'templates/confirm_payment.html')


def layout():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (page):
        yield '', join_('\n')
        yield '', join_('<html>\n')
        yield '', join_('  <head>\n')
        yield '', join_('    <title>', escape_(page.title, True), '</title>\n')
        yield '', join_('    <link rel="stylesheet" type="text/css" href="/static/styles.css" />\n')
        yield '', join_('  </head>\n')
        yield '', join_('  <body>\n')
        yield '', join_('    ', escape_(page, False), '\n')
        yield '', join_('  </body>\n')
        yield '', join_('</html>\n')
    return __template__

layout = CompiledTemplate(layout(), 'templates/layout.html')


def new_payment():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (form, error_count, url):
        yield 'title', join_('New Payment')
        yield '', join_('\n')
        yield '', join_('<h1>Payment: ', '$', '100.00</h1>\n')
        yield '', join_('\n')
        if error_count > 0:
            yield '', join_('<h3 id="error-count">', escape_(error_count, True), ' error(s)</h3>\n')
            yield '', join_('\n')
        yield '', join_('<form action="', escape_(url, True), '" method="post" autocomplete="off">\n')
        yield '', join_('  ', escape_(form.render(), False), '\n')
        yield '', join_('  <input type="submit" value="Submit" />\n')
        yield '', join_('</form>\n')
    return __template__

new_payment = CompiledTemplate(new_payment(), 'templates/new_payment.html')

