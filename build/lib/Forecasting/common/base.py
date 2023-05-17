from typing import Union, Any
from pathlib import Path

T_FILE=Union[str, Path]

class Supplier:
    def get(self) -> Any:
        pass


class Applier:

    def apply(self, obj: Any) -> Any:
        pass


class Closable:

    def close(self):
        pass

