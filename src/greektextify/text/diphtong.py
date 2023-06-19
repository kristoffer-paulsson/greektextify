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
"""Greek diphthongs representing two vowels or more."""
from greektextify.alphabet import GreekAlphabet
from .chunk import GlyphChunk
from greektextify.diacritic import GreekDiacritic
from greektextify.glyph import GreekGlyph
from .pattern import GlyphPattern
from .vowel import GreekVowel


class GreekDiphthong(GreekVowel):

    ALPHA_IOTA = GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_IOTA
    EPSILON_IOTA = GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_IOTA
    OMICRON_IOTA = GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_IOTA
    # Should ALPHA_MACRON_SUBSCRIPT exist, different from Smyth § 5, ALPHA_SUBSCRIPT is indicated.
    ALPHA_SUBSCRIPT = GreekAlphabet.LOWER_ALPHA + GreekDiacritic.COMBINING_MACRON + GreekDiacritic.COMBINING_YPOGEGRAMMENI
    ETA_SUBSCRIPT = GreekAlphabet.LOWER_ETA + GreekDiacritic.COMBINING_YPOGEGRAMMENI
    OMEGA_SUBSCRIPT = GreekAlphabet.LOWER_OMEGA + GreekDiacritic.COMBINING_YPOGEGRAMMENI

    ALPHA_UPSILON = GreekAlphabet.LOWER_ALPHA + GreekAlphabet.LOWER_UPSILON
    EPSILON_UPSILON = GreekAlphabet.LOWER_EPSILON + GreekAlphabet.LOWER_UPSILON
    OMICRON_UPSILON = GreekAlphabet.LOWER_OMICRON + GreekAlphabet.LOWER_UPSILON
    ETA_UPSILON = GreekAlphabet.LOWER_ETA + GreekAlphabet.LOWER_UPSILON

    UPSILON_IOTA = GreekAlphabet.LOWER_UPSILON + GreekAlphabet.LOWER_IOTA

    IMPROPER = frozenset([
        GlyphPattern(ALPHA_SUBSCRIPT),
        GlyphPattern(ETA_SUBSCRIPT),
        GlyphPattern(OMEGA_SUBSCRIPT),
    ])

    PROPER = frozenset([
        GlyphPattern(ALPHA_IOTA),
        GlyphPattern(EPSILON_IOTA),
        GlyphPattern(OMICRON_IOTA),
        GlyphPattern(ALPHA_UPSILON),
        GlyphPattern(EPSILON_UPSILON),
        GlyphPattern(OMICRON_UPSILON),
        GlyphPattern(ETA_UPSILON),
        GlyphPattern(UPSILON_IOTA),
    ])

    # def __init__(self, affix: tuple[GreekGlyph]):
    #    GlyphChunk.__init__(self, affix)

    def is_genuine(self) -> bool:
        """Tells whether EPSILON_IOTA or OMICRON_UPSILON are genuine or spurious, based on Smyth § 6."""
        raise NotImplemented()

    def is_spurious(self) -> bool:
        """Tells whether EPSILON_IOTA or OMICRON_UPSILON are genuine or spurious, based on Smyth § 6."""
        raise NotImplemented()

    def is_proper(self) -> bool:
        """Tells if a diphthong is inverted improper, based on Smyth § 5."""
        return not self._chunk[0].ypogegrammeni

    def is_short(self) -> bool:
        """Tells if a diphthong is short (a property of vowels), based on Smyth § 5."""
        return False

    @classmethod
    def scan(cls, glyphs: tuple[GreekGlyph], initial: bool = False) -> tuple[GlyphChunk, int] | tuple[None, int]:
        for pattern in cls.IMPROPER:
            if GlyphPattern.overlap(pattern.affix[0], glyphs[0]):
                return cls(glyphs[0:1], initial), 1

        if len(glyphs) <= 1:
            return None, 0

        # According to Smyth § 8, if a diphthong has diaeresis over iota or upsilon, those are distinguished vowels.
        if glyphs[1].dialytika:
            return None, 0

        for pattern in cls.PROPER:
            if GlyphPattern.overlap(pattern.affix[0], glyphs[0]) and GlyphPattern.overlap(pattern.affix[1], glyphs[1]):
                return cls(glyphs[0:2], initial), 2

        return None, 0




