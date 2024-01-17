import time
from behave import *
from Helpers.common_methods import CommonMethods
from Locators.page_locators import Locators
from Logs import logs_file

log = logs_file.get_logs()


@when('user enters valid username and password')
def step_impl(context):
    time.sleep(5)
    email_field = Locators().email
    email_ele = CommonMethods().find_element(context.driver, email_field)
    log.info("Email field is located")
    password_field = Locators().password
    password_ele = CommonMethods.find_element(context.driver, password_field)
    log.info("Password field is located")
    submit_field = Locators().submit
    CommonMethods.send_keys(email_ele, "gvigne22@ford.com")
    time.sleep(5)
    CommonMethods.send_keys(password_ele, "Ford@2024")
    time.sleep(5)
    CommonMethods().click(context.driver, submit_field)
    time.sleep(5)


@when('user enters invalid username and password')
def step_impl(context):
    time.sleep(5)
    email_field = Locators().email
    email_ele = CommonMethods().find_element(context.driver, email_field)
    password_field = Locators().password
    password_ele = CommonMethods.find_element(context.driver, password_field)
    submit_field = Locators().submit
    CommonMethods.send_keys(email_ele, "gvigne23@ford.com")
    time.sleep(5)
    CommonMethods.send_keys(password_ele, "Ford@2023")
    time.sleep(5)
    CommonMethods().click(context.driver, submit_field)
    time.sleep(5)


@then('login should be successful')
def step_impl(context):
    time.sleep(10)
    dashboard_string = Locators.dashboard_text
    found_text = CommonMethods().get_text(context.driver, dashboard_string)
    assert found_text == "Dashboard"


@then('login should fail')
def step_impl(context):
    time.sleep(10)
    exp_error_field = Locators.cant_find_account
    error_msg = CommonMethods().get_text(context.driver, exp_error_field)
    assert error_msg == "We can't seem to find your account"


