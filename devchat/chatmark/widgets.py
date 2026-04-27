from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple
from uuid import uuid4

from .iobase import pipe_interaction


class Widget(ABC):
    """
    Abstract base class for widgets
    """

    def __init__(self, submit: Optional[str] = None, cancel: Optional[str] = None):
        self._rendered = False
        # Prefix for IDs/keys in the widget
        self._id_prefix = self.gen_id_prefix()
        self._submit = submit
        self._cancel = cancel

    @abstractmethod
    def _in_chatmark(self) -> str:
        """
        Generate ChatMark syntax for the widget
        """

    @abstractmethod
    def _parse_response(self, response: Dict) -> None:
        """
        Parse ChatMark response from user input
        """

    def render(self) -> None:
        """
        Render the widget to receive user input
        """
        pass

    @staticmethod
    def gen_id_prefix() -> str:
        pass

    @staticmethod
    def gen_id(id_prefix: str, index: int) -> str:
        pass

    @staticmethod
    def parse_id(a_id: str) -> Tuple[Optional[str], Optional[int]]:
        pass


class Checkbox(Widget):
    """
    ChatMark syntax:
    ```chatmark
    Which files would you like to commit? I've suggested a few.
    > [x](file1) devchat/engine/prompter.py
    > [x](file2) devchat/prompt.py
    > [](file3) tests/test_cli_prompt.py
    ```

    Response:
    ```yaml
    file1: checked
    file3: checked
    ```
    """

    def __init__(
        self,
        options: List[str],
        check_states: Optional[List[bool]] = None,
        title: Optional[str] = None,
        submit_button_name: str = "Submit",
        cancel_button_name: str = "Cancel",
    ):
        """
        options: options to be selected
        check_states: initial check states of options, default to all False
        title: title of the widget
        """
        super().__init__(submit_button_name, cancel_button_name)

        if check_states is not None:
            assert len(options) == len(check_states)
        else:
            check_states = [False for _ in options]

        self._options = options
        self._states = check_states
        self._title = title

        self._selections: Optional[List[int]] = None

    @property
    def selections(self) -> Optional[List[int]]:
        """
        Get the indices of selected options
        """
        pass

    @property
    def options(self) -> List[str]:
        """
        Get the options
        """
        pass

    def _in_chatmark(self) -> str:
        """
        Generate ChatMark syntax for checkbox options
        Use the index of option to generate id/key
        """
        pass

    def _parse_response(self, response: Dict):
        pass


class TextEditor(Widget):
    """
    ChatMark syntax:
    ```chatmark
    I've drafted a commit message for you as below. Feel free to modify it.

    > | (ID)
    > fix: prevent racing of requests
    >
    > Introduce a request id and a reference to latest request. Dismiss
    > incoming responses other than from latest request.
    >
    > Reviewed-by: Z
    > Refs: #123
    ```

    Response:
    ```yaml
    ID: |
        fix: prevent racing of requests

        Introduce a request ID and a reference to latest request. Dismiss
        incoming responses other than from latest request.

        Reviewed-by: Z
        Refs: #123
    ```
    """

    def __init__(
        self,
        text: str,
        title: Optional[str] = None,
        submit_button_name: str = "Submit",
        cancel_button_name: str = "Cancel",
    ):
        super().__init__(submit_button_name, cancel_button_name)

        self._title = title
        self._text = text

        self._editor_key = self.gen_id(self._id_prefix, 0)
        self._new_text: Optional[str] = None

    @property
    def new_text(self):
        pass

    def _in_chatmark(self) -> str:
        """
        Generate ChatMark syntax for text editor
        Use _editor_key as id
        """
        pass

    def _parse_response(self, response: Dict):
        pass


class Radio(Widget):
    """
    ChatMark syntax:
    ```chatmark
    How would you like to make the change?
    > - (insert) Insert the new code.
    > - (new) Put the code in a new file.
    > - (replace) Replace the current code.
    ```

    Reponse:
    ```yaml
    replace: checked
    ```
    """

    def __init__(
        self,
        options: List[str],
        default_selected: Optional[int] = None,
        title: Optional[str] = None,
        submit_button_name: str = "Submit",
        cancel_button_name: str = "Cancel",
    ) -> None:
        """
        options: options to be selected
        default_selected: index of the option to be selected by default, default to None
        title: title of the widget
        """
        if default_selected is not None:
            assert 0 <= default_selected < len(options)

        super().__init__(submit_button_name, cancel_button_name)

        self._options = options
        self._title = title

        self._selection: Optional[int] = default_selected

    @property
    def options(self) -> List[str]:
        """
        Return the options
        """
        pass

    @property
    def selection(self) -> Optional[int]:
        """
        Return the index of the selected option
        """
        pass

    def _in_chatmark(self) -> str:
        """
        Generate ChatMark syntax for options
        Use the index of option to generate id/key
        """
        pass

    def _parse_response(self, response: Dict):
        pass


class Button(Widget):
    """
    ChatMark syntax:
    ```chatmark
    Would you like to pay $0.02 for this LLM query?
    > (Confirm) Yes, go ahead!
    > (Cancel) No, let's skip this.
    ```

    ```yaml
    Confirm: clicked
    ```

    # NOTE: almost the same as Radio essentially
    """

    def __init__(
        self,
        buttons: List[str],
        title: Optional[str] = None,
    ) -> None:
        """
        buttons: button names to show
        title: title of the widget
        """
        super().__init__()

        self._buttons = buttons
        self._title = title

        self._clicked: Optional[int] = None

    @property
    def clicked(self) -> Optional[int]:
        """
        Return the index of the clicked button
        """
        pass

    @property
    def buttons(self) -> List[str]:
        """
        Return the buttons
        """
        pass

    def _in_chatmark(self) -> str:
        """
        Generate ChatMark syntax for options
        Use the index of button to generate id/key
        """
        pass

    def _parse_response(self, response: Dict[str, str]):
        pass
