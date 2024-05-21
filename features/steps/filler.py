from behave import given, when, then
# from playwright.async_api import expect
from playwright.sync_api import expect
import Data.requests as requests


@when('user fills url page of "{req_type}" "{req_name}" request')
def step_def(context, req_type, req_name):
    context.page.pause()
    loc = '//input[@id="basic-url"]'

    # Отримуємо об'єкт за допомогою getattr
    request_type = getattr(requests, req_type)
    url = request_type[req_name] if isinstance(request_type, dict) else None

    if url:
        # Якщо це GET-запит, url буде строкою
        if isinstance(url, str):
            context.page.locator(loc).fill("https://reqres.in" + url)
        # Якщо це POST чи PUT-запит, url буде частиною словника
        elif isinstance(url, dict) and "url" in url:
            context.page.locator(loc).fill("https://reqres.in" + url["url"])


@when('user clicks on "{btn_name}" button')
def step_def(context, btn_name):
    context.page.locator(f'//button[text()="{btn_name}"]').click()
    context.page.wait_for_timeout(1000)


@then('user sees "{code_num}" status code')
def step_def(context, code_num):
    expect(context.page.locator('//textarea[@id="status"]')).to_contain_text(f'status: {code_num}')
