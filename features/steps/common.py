from behave import given, when, then


def go_to(context, url):
    if hasattr(context, "pages_list") is False:
        context.pages_list = []
    context.new_context = context.browser.new_context()
    context.page = context.new_context.new_page()
    context.page.wait_for_load_state("load")
    context.page.goto(url)
    context.pages_list.append(context.page)
    print(f'LIST OF PAGES  ...  {context.pages_list}')
    print(f'Number of Pages: {len(context.pages_list)}')
    return context.page


@given('user open "{url}" site')
def step_def(context, url):
    go_to(context, url)


@when('user chooses "{req_type}" type of the request in dd')
def step_def(context, req_type):
    locator = context.page.locator('//select[@id="select"]')
    locator.select_option(req_type)
