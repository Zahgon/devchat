import os

from .rpc import rpc_call
from .types import LocationWithText


@rpc_call
def run_code(code: str):
    pass


@rpc_call
def diff_apply(filepath, content):
    pass


@rpc_call
def get_symbol_defines_in_selected_code():
    pass


def find_symbol(command, abspath, line, col):
    pass


def find_definition(abspath: str, line: int, col: int):
    pass


def find_type_definition(abspath: str, line: int, col: int):
    pass


def find_declaration(abspath: str, line: int, col: int):
    pass


def find_implementation(abspath: str, line: int, col: int):
    pass


def find_reference(abspath: str, line: int, col: int):
    pass


def document_symbols(abspath: str):
    pass


def workspace_symbols(query: str):
    pass


def active_text_editor():
    pass


def open_folder(folder: str):
    pass


def visible_lines():
    pass


def visible_range() -> LocationWithText:
    pass


def selected_lines():
    pass


def selected_range() -> LocationWithText:
    pass
