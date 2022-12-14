from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Contact Us')
def open_url(context):
    context.app.contact_us_page.open_url()


@then('Verify email address is clickable')
def click(context):
    context.app.contact_us_page.click()



