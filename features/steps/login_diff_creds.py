import time
from behave import *
from selenium.webdriver import Keys

from Helpers.common_methods import CommonMethods
from Locators.page_locators import Locators
from Logs import logs_file

log = logs_file.get_logs()


@when('user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    context.driver.refresh()
    time.sleep(5)
    email_field = Locators().email
    email_ele = CommonMethods().find_element(context.driver, email_field)
    log.info("Email field is located")
    password_field = Locators().password
    password_ele = CommonMethods.find_element(context.driver, password_field)
    log.info("Password field is located")
    submit_field = Locators().submit
    CommonMethods.send_keys(email_ele, username)
    time.sleep(5)
    CommonMethods.send_keys(password_ele, password)
    time.sleep(5)
    CommonMethods().click(context.driver, submit_field)


@then('login activities should take place')
def step_impl(context):
    time.sleep(5)
    exp_error_field = Locators.cant_find_account
    error_msg = CommonMethods().get_text(context.driver, exp_error_field)
    log.info(error_msg)
    assert error_msg == "Your password is incorrect"

