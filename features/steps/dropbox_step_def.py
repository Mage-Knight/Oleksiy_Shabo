from behave import given, when, then
from dropbox_methods import *
from os import path

@given('I have a file named "{file}"')
def step_impl(context, file):
    assert path.exists(f"files/{file}"), f"Couldn't find {file} in specified directory"


@when('I upload "{file}" to Dropbox')
def step_impl(context, file):
    context.app.upload_file(file)


@then('I should see "{file}" uploaded')
def step_impl(context, file):
    assert context.app.check_upload(file), f"File named {file} wasn't uploaded to the dropbox app main directory"


@given('I have a file named "{file}" uploaded')
def step_impl(context, file):
    assert context.app.find_file(file), f"File named {file} doesn't exist in the dropbox app main directory"


@when('I send request to get "{file}" metadata from Dropbox')
def step_impl(context, file):
    context.app.get_metadata(file)


@then('I should see "{file}" metadata')
def step_impl(context, file):
    assert context.app.check_metadata(file), f"error obtaining {file} metadata"


@when('I send request to delete "{file}" from Dropbox')
def step_impl(context, file):
    context.app.delete_file(file)


@then('"{file}" should be deleted')
def step_impl(context, file):
    assert context.app.check_delete(file), f"{file} wasn't deleted"