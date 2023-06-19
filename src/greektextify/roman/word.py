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
"""Ancient Greek romanization according to ALA-LC (American Library Association – Library of Congress) based on:
https://en.wikipedia.org/wiki/ALA-LC_romanization
https://en.wikipedia.org/wiki/Romanization_of_Greek

In the future, hopefully this is implemented
https://www.loc.gov/catdir/cpso/romanization/greek.pdf
"""
from greektextify.alphabet import GreekAlphabet
from greektextify.nlp.contextual import NlpWarning
from greektextify.text.chunk import GlyphChunk
from greektextify.text.consonant import GreekConsonant
from greektextify.text.diphtong import GreekDiphthong
from greektextify.text.rmedial import MedialRho
from greektextify.text.ngamma import GammaNasal
from greektextify.text.vowel import GreekVowel


class GreekWordToken:

    def __init__(self, chunks: tuple[GlyphChunk, ...]):
        self._chunks = chunks

    def __str__(self) -> str:
        out = ""
        upper = False
        for chunk in self._chunks:
            if chunk.initial:
                upper = chunk.is_upper()
                if isinstance(chunk, GreekDiphthong):
                    out += GreekAlphabet.ALALC2010[GreekAlphabet.ROUGH] if chunk.is_rough() else ''
                    out += chunk.ALALC2010[chunk.pattern.raw]
                elif isinstance(chunk, GreekVowel):
                    glyph = chunk.chunk[0]
                    out += GreekAlphabet.ALALC2010[GreekAlphabet.ROUGH] if glyph.rough else ''
                    out += GreekAlphabet.ALALC2010[glyph.lower]
                elif isinstance(chunk, GreekConsonant):
                    glyph = chunk.chunk[0]
                    if glyph.lower == GreekAlphabet.LOWER_RHO:
                        out += GreekAlphabet.ALALC2010[glyph.lower] + GreekAlphabet.ALALC2010[GreekAlphabet.ROUGH]
                    else:
                        out += GreekAlphabet.ALALC2010[glyph.lower]
                else:
                    raise NlpWarning(*NlpWarning.PROCESS_ERROR)
            else:
                if isinstance(chunk, GreekDiphthong):
                    out += chunk.ALALC2010[chunk.pattern.raw]
                elif isinstance(chunk, GreekVowel):
                    out += GreekAlphabet.ALALC2010[chunk.chunk[0].lower]
                elif isinstance(chunk, GammaNasal):
                    out += chunk.ALALC2010[chunk.pattern.raw]
                elif isinstance(chunk, MedialRho):
                    out += chunk.ALALC2010[chunk.pattern.raw]
                elif isinstance(chunk, GreekConsonant):
                    out += GreekAlphabet.ALALC2010[chunk.chunk[0].lower]
                else:
                    raise NlpWarning(*NlpWarning.PROCESS_ERROR)

        return out.title() if upper else out
