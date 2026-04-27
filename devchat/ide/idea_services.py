from .rpc import rpc_method
from .types import LocationWithText


class IdeaIDEService:
    def __init__(self):
        self._result = None

    @rpc_method
    def get_visible_range(self) -> LocationWithText:
        pass

    @rpc_method
    def get_selected_range(self) -> LocationWithText:
        pass
