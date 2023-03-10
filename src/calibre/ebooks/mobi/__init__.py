#!/usr/bin/env python


__license__   = 'GPL v3'
__copyright__ = '2008, Kovid Goyal <kovid at kovidgoyal.net>'


class MobiError(Exception):
    pass


# That might be a bit small on the PW, but Amazon/KG 2.5 still uses these values, even when delivered to a PW
MAX_THUMB_SIZE = 16 * 1024
MAX_THUMB_DIMEN = (180, 240)
