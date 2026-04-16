"""Defines a git hook to allow pre-commit warnings and errors about import order.

usage:
    exit_code = git_hook(strict=True|False, modify=True|False)
"""

import os
import subprocess  # nosec
from pathlib import Path

from isort import Config, api, exceptions


def get_output(command: list[str]) -> str:
    """Run a command and return raw output

    :param str command: the command to run
    :returns: the stdout output of the command
    """
    pass


def get_lines(command: list[str]) -> list[str]:
    """Run a command and return lines of output

    :param str command: the command to run
    :returns: list of whitespace-stripped lines output by command
    """
    pass


def git_hook(
    strict: bool = False,
    modify: bool = False,
    lazy: bool = False,
    settings_file: str = "",
    directories: list[str] | None = None,
) -> int:
    """Git pre-commit hook to check staged files for isort errors

    :param bool strict - if True, return number of errors on exit,
        causing the hook to fail. If False, return zero so it will
        just act as a warning.
    :param bool modify - if True, fix the sources if they are not
        sorted properly. If False, only report result without
        modifying anything.
    :param bool lazy - if True, also check/fix unstaged files.
        This is useful if you frequently use ``git commit -a`` for example.
        If False, only check/fix the staged files for isort errors.
    :param str settings_file - A path to a file to be used as
                               the configuration file for this run.
        When settings_file is the empty string, the configuration file
        will be searched starting at the directory containing the first
        staged file, if any, and going upward in the directory structure.
    :param list[str] directories - A list of directories to restrict the hook to.

    :return number of errors if in strict mode, 0 otherwise.
    """
    pass
