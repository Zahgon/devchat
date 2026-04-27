from typing import Dict, List, Optional, Union

from .iobase import pipe_interaction
from .widgets import Button, Widget


class Form:
    """
    A container for different widgets

    Syntax:
    """

    def __init__(
        self,
        components: List[Union[Widget, str]],
        title: Optional[str] = None,
        submit_button_name: Optional[str] = None,
        cancel_button_name: Optional[str] = None,
    ):
        """
        components: components in the form, can be widgets (except Button) or strings
        title: title of the form
        """
        assert (
            any(isinstance(c, Button) for c in components) is False
        ), "Button is not allowed in Form"

        self._components = components
        self._title = title

        self._rendered = False
        self._submit = submit_button_name
        self._cancel = cancel_button_name

    @property
    def components(self) -> List[Union[Widget, str]]:
        """
        Return the components
        """
        pass

    def _in_chatmark(self) -> str:
        """
        Generate ChatMark syntax for all components
        """
        pass

    def _parse_response(self, response: Dict):
        """
        Parse response from user input
        """
        pass

    def render(self):
        """
        Render to receive user input
        """
        pass
