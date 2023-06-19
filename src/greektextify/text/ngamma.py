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
"""Gamma Nasal consonant cluster."""
from greektextify.alphabet import GreekAlphabet
from greektextify.glyph import GreekGlyph
from greektextify.text.chunk import GlyphChunk
from greektextify.text.consonant import GreekConsonant
from greektextify.text.pattern import GlyphPattern


class GammaNasal(GreekConsonant):
    GAMMA_KAPPA = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_KAPPA
    GAMMA_GAMMA = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_GAMMA
    GAMMA_CHI = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_CHI
    GAMMA_XI = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_XI

    GAMMA_NASAL = frozenset([
        GlyphPattern(GAMMA_KAPPA),
        GlyphPattern(GAMMA_GAMMA),
        GlyphPattern(GAMMA_CHI),
        GlyphPattern(GAMMA_XI)
    ])

    @classmethod
    def scan(cls, glyphs: tuple[GreekGlyph], initial: bool = False) -> tuple[GlyphChunk, int] | tuple[None, int]:
        cluster = glyphs[0].lower + glyphs[1].lower
        if cluster in cls.GAMMA_NASAL:
            return cls(glyphs[0:2], initial), 2
        else:
            return None, 0
