"""Defines all wrap modes that can be used when outputting formatted imports"""

import enum
from collections.abc import Callable
from inspect import signature
from typing import Any

import isort.comments

_wrap_modes: dict[str, Callable[..., str]] = {}


def from_string(value: str) -> "WrapModes":
    pass


def formatter_from_string(name: str) -> Callable[..., str]:
    return _wrap_modes.get(name.upper(), grid)


def _wrap_mode_interface(
    statement: str,
    imports: list[str],
    white_space: str,
    indent: str,
    line_length: int,
    comments: list[str],
    line_separator: str,
    comment_prefix: str,
    include_trailing_comma: bool,
    remove_comments: bool,
) -> str:
    """Defines the common interface used by all wrap mode functions"""
    pass


def _wrap_mode(function: Callable[..., str]) -> Callable[..., str]:
    """Registers an individual wrap mode. Function name and order are significant and used for
    creating enum.
    """
    _wrap_modes[function.__name__.upper()] = function
    function.__signature__ = signature(_wrap_mode_interface)  # type: ignore
    function.__annotations__ = _wrap_mode_interface.__annotations__
    return function


@_wrap_mode
def grid(**interface: Any) -> str:
    pass


@_wrap_mode
def vertical(**interface: Any) -> str:
    pass


def _hanging_indent_end_line(line: str) -> str:
    pass


@_wrap_mode
def hanging_indent(**interface: Any) -> str:
    pass


@_wrap_mode
def vertical_hanging_indent(**interface: Any) -> str:
    _line_with_comments = isort.comments.add_to_line(
        interface["comments"],
        "",
        removed=interface["remove_comments"],
        comment_prefix=interface["comment_prefix"],
    )
    _imports = ("," + interface["line_separator"] + interface["indent"]).join(interface["imports"])
    _comma_maybe = "," if interface["include_trailing_comma"] else ""
    return (
        f"{interface['statement']}({_line_with_comments}{interface['line_separator']}"
        f"{interface['indent']}{_imports}{_comma_maybe}{interface['line_separator']})"
    )


def _vertical_grid_common(need_trailing_char: bool, **interface: Any) -> str:
    pass


@_wrap_mode
def vertical_grid(**interface: Any) -> str:
    pass


@_wrap_mode
def vertical_grid_grouped(**interface: Any) -> str:
    pass


@_wrap_mode
def vertical_grid_grouped_no_comma(**interface: Any) -> str:
    # This is a deprecated alias for vertical_grid_grouped above. This function
    # needs to exist for backwards compatibility but should never get called.
    raise NotImplementedError


@_wrap_mode
def noqa(**interface: Any) -> str:
    pass


@_wrap_mode
def vertical_hanging_indent_bracket(**interface: Any) -> str:
    pass


@_wrap_mode
def vertical_prefix_from_module_import(**interface: Any) -> str:
    pass


@_wrap_mode
def hanging_indent_with_parentheses(**interface: Any) -> str:
    pass


@_wrap_mode
def backslash_grid(**interface: Any) -> str:
    pass


WrapModes = enum.Enum(  # type: ignore
    "WrapModes", {wrap_mode: index for index, wrap_mode in enumerate(_wrap_modes.keys())}
)
