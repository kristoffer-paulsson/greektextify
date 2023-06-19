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
"""Glyph pattern classes."""
from greektextify.glyph import GreekGlyph
from greektextify.token.word import GreekWord


class GlyphPattern:

    def __init__(self, affix: str):
        self._affix = GreekWord(affix).glyphs

    @property
    def affix(self) -> tuple[GreekGlyph]:
        return self._affix

    def compare(self, word: tuple[GreekGlyph], pos: int = 0):
        for idx in range(0, len(self._affix)):
            if not word[pos + idx].compare(self._affix[idx], caseSensitive=False):
                return False

        return True

    @staticmethod
    def overlap(a: GreekGlyph, b: GreekGlyph, caseSensitive: bool = False) -> bool:
        """Tells if A fits inside B where the booleans counts as a set."""
        same = True
        for key in GreekGlyph._fields:
            af = getattr(a, key)
            bf = getattr(b, key)
            same = same if not af else same if af == bf else False
            if not same:
                return False
        return True
