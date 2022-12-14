from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Main Page')
def open_url(context):
    context.app.main_page.open_url()


@then('Verify phone number in correct order')
def verify_element_phone_text(context):
    context.app.main_page.verify_element_phone_text()


@then('Verify the word favorites is spelled correctly')
def verify_element_headline_text(context):
    context.app.main_page.verify_element_headline_text()


@then('Verify the word fair is deleted')
def verify_element_title_text(context):
    context.app.main_page.verify_element_title_text()

