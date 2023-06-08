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
"""Greek diphthongs representing two vowels or more."""
from typing import Tuple

from .alphabet import GreekAlphabet
from .glyph import GreekGlyph
from .pattern import GlyphPattern


class GreekDiphthong(GlyphPattern):
    def __init__(self, affix: Tuple[GreekGlyph]):
        GlyphPattern.__init__(self, affix)

    def is_proper(self) -> bool:
        """Tells if a diphthong is inverted improper, based on Smyth § 5."""
        return not self._affix[0].ypogegrammeni

    def is_short(self) -> bool:
        """Tells if a diphthong is short (a property of vowels), based on Smyth § 5."""
        return False

    def is_upper(self) -> bool:
        """Tells if a diphthong is upper case."""
        return self._affix[0] in GreekAlphabet.CASE_UPPER


GREEK_DIPHTHONG = frozenset([
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_ALPHA),
        GreekGlyph(GreekAlphabet.LOWER_IOTA)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_EPSILON),
        GreekGlyph(GreekAlphabet.LOWER_IOTA)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_OMICRON),
        GreekGlyph(GreekAlphabet.LOWER_IOTA)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_ALPHA, ypogegrammeni=True, macron=True)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_ETA, ypogegrammeni=True)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_OMEGA, ypogegrammeni=True)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_ALPHA),
        GreekGlyph(GreekAlphabet.LOWER_UPSILON)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_EPSILON),
        GreekGlyph(GreekAlphabet.LOWER_UPSILON)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_OMICRON),
        GreekGlyph(GreekAlphabet.LOWER_UPSILON)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_ETA),
        GreekGlyph(GreekAlphabet.LOWER_UPSILON)
    ])),
])
