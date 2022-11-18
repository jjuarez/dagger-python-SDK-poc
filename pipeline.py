#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run tests for a single Python version.
"""
from enum import Enum
from typing import List, Final
import sys
import anyio
import dagger


class ErrorCode(Enum):
    """
    The collection of errors
    """
    OK = 0
    NOT_IMPLEMENTED = 1
    UNKNOWN = 127

PYTHON_VERSION: Final = "3.11"
PYTHON_DOCKER_OS: Final = "alpine"


async def test() -> int:
    build_config = dagger.Config(log_output=sys.stderr)
    async with dagger.Connection(build_config) as client:
        src_id = await client.host().workdir([".venv", "dist", "__pycache__"]).id()

        python = (
            client.container()
                .from_(f"python:{PYTHON_VERSION}-{PYTHON_DOCKER_OS}")
                .with_mounted_directory("/src", src_id)
                .with_workdir("/src")
                .exec(["pip", "install", "--upgrade", "pip"])
                .exec(["pip", "install", "poetry"])
                .exec(["poetry", "install"])
                .exec(["poetry", "run", "pytest"])
        )
        return await python.exit_code()


async def lint() -> int:
    build_config = dagger.Config(log_output=sys.stderr)
    async with dagger.Connection(build_config) as client:
        src_id = await client.host().workdir([".venv", "dist", "__pycache__"]).id()

        python = (
            client.container()
                .from_(f"python:{PYTHON_VERSION}-{PYTHON_DOCKER_OS}")
                .with_mounted_directory("/src", src_id)
                .with_workdir("/src")
                .exec(["pip", "install", "--upgrade", "pip"])
                .exec(["pip", "install", "poetry"])
                .exec(["poetry", "install"])
                .exec(["poetry", "run", "ruff", "."])
        )
        return await python.exit_code()


def main(arguments: List[str]) -> int:
    """
    Command launcher
    """
    if len(arguments) < 2:
        return ErrorCode.UNKNOWN

    command: str = arguments[1]

    if command == 'lint':
        return anyio.run(lint)
    elif command == 'test':
        return anyio.run(test)

    return ErrorCode.NOT_IMPLEMENTED


if __name__ == '__main__':
    main(arguments=sys.argv)
