from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
import allure
import os


@fixture()
def browser_headed(context):
    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=False, slow_mo=500)
        yield context.browser
        context.browser.close()


@fixture()
def browser_headless(context):
    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=True, slow_mo=900)
        yield context.browser
        context.browser.close()


def before_tag(context, tag):
    if tag == "browser.headed":
        use_fixture(browser_headed, context)
    elif tag == "browser.headless":
        use_fixture(browser_headless, context)
    if tag == "no_cleanup":
        context.cleanup = False
    else:
        context.cleanup = True


def before_all(context):
    if not os.path.exists("allure-results"):
        os.makedirs("allure-results")


# def after_scenario(context, scenario):
#     for attachment in context.attachments:
#         allure.attach.file(attachment, attachment_type=allure.attachment_type.PNG)
