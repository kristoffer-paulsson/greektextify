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
"""Greek syllable representing main letter plus diacritics."""
from greektextify.text.cluster import GlyphCluster
from greektextify.glyph import GreekGlyph


class GreekSyllable(GlyphCluster):

    def __init__(self, onset: GlyphCluster = None, nucleus: GlyphCluster = None, coda: GlyphCluster = None):
        GlyphCluster.__init__(self, list(filter(lambda item: item is not None, [onset, nucleus, coda])))

    # onset
    # nucleus
    # coda

    # n
    # on
    # nc
    # onc

    @staticmethod
    def syllabify(glyphs: tuple[GreekGlyph]) -> tuple['GreekSyllable', int] | tuple[None, int]:
        return None, 0
