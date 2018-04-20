# Copyright (C) 2018 Duncan Macleod
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""Sphinx/RST for GWIn
"""

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'


def rst_dict_table(dict_, key_format=str, val_format=str, header=None):
    """Returns an RST-formatted table of keys and values from a `dict`

    Parameters
    ----------
    dict_ : `dict`
        data to display in table

    key_format : `callable`
        callable function with which to format keys

    val_format : `callable`
        callable function with which to format values

    header : `None`, `tuple` of `str`
        a 2-tuple of header for the two columns, or `None` to exclude
        a header line (default)

    Examples
    --------
    >>> a = {'key1': 'value1', 'key2': 'value2'}
    >>> print(rst_dict_table(a))
    ====  ======
    key1  value1
    key2  value2
    ====  ======
    >>> print(rst_dict_table(a, key_format='``{}``'.format,
    ...                      val_format=':class:`{}`'.format,
    ...                      header=('Key', 'Value'))
    ========  ===============
    Key       Value
    ========  ===============
    ``key1``  :class:`value1`
    ``key2``  :class:`value2`
    ========  ===============
    """
    keys, values = zip(*dict_.items())

    # apply formatting
    keys = map(key_format, keys)
    values = map(val_format, values)

    # work out longest elements in each column
    nckey = max(map(len, keys))
    ncval = max(map(len, values))
    if header:
        khead, vhead = header
        nckey = max(nckey, len(khead))
        ncval = max(ncval, len(vhead))

    # build table header line
    divider = "{}  {}".format('='*nckey, '='*ncval)

    def row(key, val):
        fmt = '{{0:{0}s}}  {{1}}'.format(nckey, ncval)
        return fmt.format(key, val)

    # build table of lines
    lines = [divider]
    if header:
        lines.extend((row(*header), divider))
    for key, val in zip(keys, values):
        fmt = '{{0:{0}s}}  {{1}}'.format(nckey, ncval)
        lines.append(fmt.format(key, val))
    lines.append(divider)

    return '\n'.join(lines)