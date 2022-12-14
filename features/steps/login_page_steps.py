from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Login Page')
def open_url(context):
    context.app.login_page.open_url()


@then('Verify email is separate from schedule information')
def verify_element_text(context):
    context.app.login_page.verify_element_text()



