#!/usr/bin/env python3
"""a module that defines safe_first_element"""
import typing


def safe_first_element(lst: typing.Iterable[typing.Any]) -> typing.Union[typing.Any, None]:
    """function to get safe first element"""
    if lst:
        return lst[0]
    else:
        return None
    