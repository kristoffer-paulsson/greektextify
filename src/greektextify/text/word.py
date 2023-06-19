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
"""Greek word alteration and analyzation."""
from greektextify.glyph import GreekGlyph
from greektextify.nlp.contextual import NlpWarning
from greektextify.text.cdouble import DoubleConsonant
from greektextify.text.chunk import GlyphChunk
from greektextify.text.cluster import GlyphCluster
from greektextify.text.consonant import GreekConsonant
from greektextify.text.diphtong import GreekDiphthong
from greektextify.text.ngamma import GammaNasal
from greektextify.text.vowel import GreekVowel


class GreekWord(GlyphCluster):

    SCAN_ANALYZER = (
        (GreekDiphthong, 1),
        (GreekVowel, 1),
        (GammaNasal, 2),
        (DoubleConsonant, 2),
        (GreekConsonant, 1),
    )

    def __init__(self, syllables: tuple[GlyphCluster]):
        GlyphCluster.__init__(self, syllables)

    @classmethod
    def analyze(cls, glyphs: tuple[GreekGlyph]) -> tuple[GlyphChunk]:
        initial = True
        chunks = list()
        subject = glyphs

        while len(subject):
            for scanner, min_req in cls.SCAN_ANALYZER:
                if len(subject) < min_req:
                    continue

                chunk, size = scanner.scan(subject, initial)
                if chunk is not None:
                    chunks.append(chunk)
                    initial = False
                    subject = subject[size:]
                    break
            # raise NlpWarning(*NlpWarning.PROCESS_ERROR)
        chunks = tuple(chunks)
        return chunks

    @classmethod
    def syllabify(cls, chunks: tuple[GlyphChunk]) -> tuple[GlyphCluster]:
        pass
