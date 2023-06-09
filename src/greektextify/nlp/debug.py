#
# Copyright (c) 2023 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
#
# Permission to use, copy, modify, and/or distribute this software for any purpose with
# or without fee is hereby granted, provided that the above copyright notice and this
# permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO
# THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
#     https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC
#
# Contributors:
#     Kristoffer Paulsson - initial implementation
#
"""Utility for NLP debugging in case of errors not visible to the human eye."""
import unicodedata
from typing import List

from greektextify.diacritic import GreekDiacritic
from greektextify.token.spacing import Spacing


class Debugger:

    @staticmethod
    def glyph(text: str) -> List[str]:
        debugging = list()
        for ch in text:
            try:
                symbol_name = unicodedata.name(ch)
            except ValueError:
                symbol_name = "NAME N/A"

            combining = "combining" in symbol_name.lower()
            glyph = Spacing.DEBUG_SPACE if ch in Spacing.BLANK_SPACE else ch
            row = "U+{ch:04X}       {symbol:<8} {name}".format(
                ch=ord(ch),
                symbol=(GreekDiacritic.DEBUG_CIRCLE if combining else "") + glyph,
                name=symbol_name
            )
            debugging.append(row)
        return debugging
