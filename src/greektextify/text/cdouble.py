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
"""Double Consonant consonant cluster."""
from greektextify.alphabet import GreekAlphabet


class DoubleConsonant:
    SIGMA_DELTA = GreekAlphabet.LOWER_SIGMA + GreekAlphabet.LOWER_DELTA
    DELTA_SIGMA = GreekAlphabet.LOWER_DELTA + GreekAlphabet.LOWER_SIGMA
    DELTA_IOTA = GreekAlphabet.LOWER_DELTA + GreekAlphabet.LOWER_IOTA

    ZETA = frozenset([
        SIGMA_DELTA, DELTA_SIGMA, DELTA_IOTA
    ])

    KAPPA_SIGMA = GreekAlphabet.LOWER_KAPPA + GreekAlphabet.LOWER_SIGMA
    GAMMA_SIGMA = GreekAlphabet.LOWER_GAMMA + GreekAlphabet.LOWER_SIGMA
    CHI_SIGMA = GreekAlphabet.LOWER_CHI + GreekAlphabet.LOWER_SIGMA

    XI = frozenset([
        KAPPA_SIGMA, GAMMA_SIGMA, CHI_SIGMA
    ])

    PI_SIGMA = GreekAlphabet.LOWER_PI + GreekAlphabet.LOWER_SIGMA
    BETA_SIGMA = GreekAlphabet.LOWER_BETA + GreekAlphabet.LOWER_SIGMA
    PHI_SIGMA = GreekAlphabet.LOWER_PHI + GreekAlphabet.LOWER_SIGMA

    PSI = frozenset([
        PI_SIGMA, BETA_SIGMA, PHI_SIGMA
    ])
