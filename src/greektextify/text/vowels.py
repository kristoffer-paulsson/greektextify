#
# Copyright (c) 2022 by Kristoffer Paulsson <kristoffer.paulsson@talenten.se>.
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
"""Greek alphabet vowels distinct in lowercase."""
from greektextify.alphabet import GreekAlphabet
from greektextify.glyph import GreekGlyph


class GreekVowels:
    """Koine vowels described as in Smyth grammar 1.1.2."""

    SHORT = frozenset([
        GreekAlphabet.LOWER_EPSILON,
        GreekAlphabet.LOWER_OMICRON
    ])  # Short Vowels acc. to Smyth § 4

    LONG = frozenset([
        GreekAlphabet.LOWER_ETA,
        GreekAlphabet.LOWER_OMEGA
    ])  # Long vowels acc. to Smyth § 4

    VARIABLE = frozenset([
        GreekAlphabet.LOWER_ALPHA,
        GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_UPSILON
    ])  # Indistinguishable vowels acc. to Smyth § 4

    NOT_SHORT = frozenset(set(LONG) | set(VARIABLE))
    # Only not short vowels may have a circumflex: https://en.wikipedia.org/wiki/Greek_diacritics

    VOWELS = frozenset(set(SHORT) | set(LONG) | set(VARIABLE))

    @staticmethod
    def is_vowel(glyph: GreekGlyph) -> bool:
        """Tells if a glyph is a vowel.
        Based on Smyth § 4."""
        return glyph.ch.lower() in GreekVowels.VOWELS

    @staticmethod
    def is_short(glyph: GreekGlyph) -> bool:
        """Tells if a vowel is short (true) or long (false).
        The glyph is expected to be a verified vowel.
        Based on Smyth § 4 and https://en.wikipedia.org/wiki/Greek_diacritics, § 144 & § 149 Not yet implemented."""
        ch = glyph.ch.lower()
        if ch in GreekVowels.SHORT:  # Always short
            return True
        elif ch in GreekVowels.NOT_SHORT and glyph.perispomeni:  # circumflex, always long
            return False
        elif ch in GreekVowels.VARIABLE and not glyph.macron:  # short if not marked with macron
            return True
        else:  # The rest that are always or considered long
            return False
