import re
from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .settings import Config
else:
    Config = Any

_import_line_intro_re = re.compile("^(?:from|import) ")
_import_line_midline_import_re = re.compile(" import ")


def module_key(
    module_name: str,
    config: Config,
    sub_imports: bool = False,
    ignore_case: bool = False,
    section_name: Any | None = None,
    straight_import: bool | None = False,
) -> str:
    match = re.match(r"^(\.+)\s*(.*)", module_name)
    if match:
        sep = " " if config.reverse_relative else "_"
        module_name = sep.join(match.groups())

    prefix = ""
    if ignore_case:
        module_name = str(module_name).lower()
    else:
        module_name = str(module_name)

    if sub_imports and config.order_by_type:
        if module_name in config.constants:
            prefix = "A"
        elif module_name in config.classes:
            prefix = "B"
        elif module_name in config.variables:
            prefix = "C"
        elif module_name.isupper() and len(module_name) > 1:  # see issue #376
            prefix = "A"
        elif module_name in config.classes or module_name[0:1].isupper():
            prefix = "B"
        else:
            prefix = "C"
    if not config.case_sensitive:
        module_name = module_name.lower()

    length_sort = (
        config.length_sort
        or (config.length_sort_straight and straight_import)
        or str(section_name).lower() in config.length_sort_sections
    )
    _length_sort_maybe = (str(len(module_name)) + ":" + module_name) if length_sort else module_name
    return f"{(module_name in config.force_to_top and 'A') or 'B'}{prefix}{_length_sort_maybe}"


def section_key(line: str, config: Config) -> str:
    pass


def sort(
    config: Config,
    to_sort: Iterable[str],
    key: Callable[[str], Any] | None = None,
    reverse: bool = False,
) -> list[str]:
    return config.sorting_function(to_sort, key=key, reverse=reverse)


def naturally(
    to_sort: Iterable[str], key: Callable[[str], Any] | None = None, reverse: bool = False
) -> list[str]:
    """Returns a naturally sorted list"""
    pass


def _atoi(text: str) -> Any:
    pass


def _natural_keys(text: str) -> list[Any]:
    pass
