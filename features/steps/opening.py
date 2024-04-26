from behave import given, when, then


def go_to(context, url):
    if hasattr(context, "pages_list") is False:
        context.pages_list = []
    context.new_context = context.browser.new_context()
    # context.new_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # context.new_context.grant_permissions(["clipboard-read"])
    # print(f"BROWSER NAME : {context.browser.browser_type.name}")
    # print(f"BROWSER VERSION : {context.browser.version}")
    context.page = context.new_context.new_page()
    context.page.wait_for_load_state("load")
    # context.page.set_default_timeout(15000)
    context.page.goto(url)
    context.pages_list.append(context.page)
    print(f'LIST OF PAGES  ...  {context.pages_list}')
    print(f'Number of Pages: {len(context.pages_list)}')
    return context.page


# @given('user open "{url}" site')
# def step_def(context, url):
#     context.page.goto(url)

@given('user open "{url}" site')
def step_def(context, url):
    go_to(context, url)

# @given('user open site')
# def step_def(context):
#     go_to(context, 'https://www.google.com/')
