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
"""Betacode word class segment.

Following for standard: http://stephanus.tlg.uci.edu/encoding/BCM.pdf
"""
from greektextify.beta.alphabet import BetaAlphabet
from greektextify.beta.diacritic import BetaDiacritic
from greektextify.beta.glyph import BetaGlyph
from greektextify.beta.midway import BetaMidway
from greektextify.glyph import GreekGlyph
from greektextify.token.word import GreekWord


class BetaWord(GreekWord):
    """Greek word analyzer and parsers."""

    WORD_CHARS = frozenset(
        set(BetaAlphabet.ALPHABET) | set(BetaDiacritic.DIACRITICS) | set(BetaMidway.MODIFIERS)
    )

    def __init__(self, word: str):
        GreekWord.__init__(self, word)

    @property
    def glyphs(self) -> tuple[GreekGlyph]:
        return self._glyphs

    @property
    def hyphen(self) -> bool:
        return BetaAlphabet.HYPHEN_MINUS in self._word

    @property
    def apostrophe(self) -> bool:
        return self._word[-1] == BetaAlphabet.APOSTROPHE

    @classmethod
    def immaterialize(cls, text: str) -> tuple[str]:
        token = list()
        for ch in text.upper():
            if ch in cls.WORD_CHARS:
                token.append(ch)
            else:
                break

        if len(token) == 0:
            return tuple()
        elif token[-1] == BetaAlphabet.HYPHEN_MINUS:
            return tuple(token[:-1])
        elif token[0] == BetaAlphabet.HYPHEN_MINUS:
            return tuple()
        else:
            return tuple(token)

    @classmethod
    def glyphen(cls, word: str) -> tuple[GreekGlyph]:
        position = 0
        # length = len(word)-1 if word[-1] == BetaMidway.APOSTROPHE else len(word)
        length = len(word)
        glyphs = list()

        while position != length:
            glyph, size = BetaGlyph.glyphen(word[position:].upper())
            glyphs.append(glyph)
            position += size

        return tuple(glyphs)




