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
from .alphabet import GreekAlphabet


class GreekVowels:
    """Koine vowels described as in Smyth grammar 1.1.2."""

    VOWELS_SHORT = frozenset((
        GreekAlphabet.LOWER_EPSILON,
        GreekAlphabet.LOWER_OMICRON
    ))

    VOWELS_LONG = frozenset((
        GreekAlphabet.LOWER_ETA,
        GreekAlphabet.LOWER_OMEGA
    ))

    VOWELS_VAR = frozenset((
        GreekAlphabet.LOWER_ALPHA,
        GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_UPSILON
    ))

    VOWELS = frozenset(set(VOWELS_SHORT) + set(VOWELS_LONG) + set(VOWELS_VAR))
