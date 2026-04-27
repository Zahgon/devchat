# flake8: noqa: E402
from functools import wraps

from devchat.chatmark import Checkbox, Form, TextEditor


class MissEditConfirmFieldException(Exception):
    pass


def edit_confirm(response):
    pass


def llm_edit_confirm(edit_confirm_fun=edit_confirm):
    pass
