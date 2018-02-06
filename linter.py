#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jan Meischner
# Copyright (c) 2018 Jan Meischner
#
# License: MIT
#

"""This module exports the Xqlint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Xqlint(NodeLinter):
    """Provides an interface to xqlint."""

    syntax = 'xquery'
    cmd = ('xqlint', 'lint', '@')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r'''(?xi)
        ^\s*(?P<line>\d+).*$\r?\n
        ^\s{4,5}(?P<col>[^\^]*)\^\s\[(?:(?P<error>[X].*)|(?P<warning>[W].*))\]\s(?P<message>.*)
    '''
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'