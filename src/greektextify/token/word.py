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
"""Greek word class segment."""

from greektextify.alphabet import GreekAlphabet
from greektextify.diacritic import GreekDiacritic
from greektextify.uni.extended import GreekExtended
from greektextify.glyph import GreekGlyph
from greektextify.token.immaterializer import TokenImmaterializableMixin
from greektextify.text.ipa import IPA
from greektextify.uni.midway import GreekMidway
from greektextify.text.syllable import GreekSyllable
from greektextify.text.vowels import GreekVowels


class GreekWord(TokenImmaterializableMixin):
    """Greek word analyzer and parsers."""

    WORD_CHARS = frozenset(
        set(GreekExtended.LETTERS) | set(GreekExtended.DIACRITICS) | set(GreekMidway.LETTERS) |
        set(GreekAlphabet.ALPHABET) | set(GreekDiacritic.DIACRITICS) |
        set(GreekMidway.MODIFIERS)
    )

    def __init__(self, word: str):
        self._word = word
        self._glyphs = self.glyphen(word)
        self._syllables = self.syllabify(self._glyphs)

    @property
    def glyphs(self) -> tuple[GreekGlyph]:
        return self._glyphs

    @property
    def hyphen(self) -> bool:
        return GreekAlphabet.HYPHEN_MINUS in self._word

    @property
    def apostrophe(self) -> bool:
        return self._word[-1] == GreekMidway.APOSTROPHE

    @classmethod
    def immaterialize(cls, text: str) -> tuple[str]:
        token = list()
        for ch in text:
            if ch in cls.WORD_CHARS:
                token.append(ch)
            else:
                break

        if len(token) == 0:
            return tuple()
        elif token[-1] == GreekAlphabet.HYPHEN_MINUS:
            return tuple(token[:-1])
        elif token[0] == GreekAlphabet.HYPHEN_MINUS:
            return tuple()
        else:
            return tuple(token)

    @classmethod
    def glyphen(cls, word: str) -> tuple[GreekGlyph]:
        position = 0
        length = len(word)-1 if word[-1] == GreekMidway.APOSTROPHE else len(word)
        glyphs = list()

        while position != length:
            glyph, size = GreekGlyph.glyphen(word[position:])
            glyphs.append(glyph)
            position += size

        return tuple(glyphs)

    @classmethod
    def syllabify(cls, glyphs: tuple[GreekGlyph]) -> tuple[GreekSyllable]:
        pass

    # Under development
    @classmethod
    def pronounce(cls, word: tuple[GreekGlyph]):
        """Generates an IPA phonetic key string for Koine words."""
        ipa = ""
        for glyph in word:
            ipa += GreekAlphabet.SOUNDS[glyph.ch.lower()]
            if GreekVowels.is_vowel(glyph):
                if not GreekVowels.is_short(glyph):
                    ipa += IPA.LONG.unicode_repr

        return ipa

    # Lacks support for uppercase currently
    # Lacks support for diphthongs
    @classmethod
    def romanize(cls, word: tuple[GreekGlyph]):
        """Generates a transliterated romanized string for Koine words."""
        roman = ""
        for glyph in word:
            if glyph.rough:
                roman += 'h'
            roman += GreekAlphabet.ROMAN[glyph.ch.lower()]
            if glyph.subscript:
                roman += 'i'

        return roman
