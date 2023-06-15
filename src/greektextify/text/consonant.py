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
"""Greek consonants."""
from enum import Enum

from greektextify.alphabet import GreekAlphabet
from greektextify.glyph import GreekGlyph

from greektextify.diacritic import GreekDiacritic
from greektextify.text.pattern import GlyphPattern


class Voice(Enum):
    """Consonant voice, degree of noise, based on Smyth § 15.c"""
    VOWELS = 0
    NASALS = 1
    SEMIS = 2
    LIQUIDS = 3
    SPIRANTS = 4
    STOPS = 5
    DOUBLES = 6


# RHO can be Dental and Palatal, usually voiced but with rough breathing voiceless.

class GreekConsonant:

    GAMMA_NASAL = None

    VOICED = frozenset([
        GreekAlphabet.LOWER_BETA,
        GreekAlphabet.LOWER_DELTA,
        GreekAlphabet.LOWER_GAMMA,
        GreekAlphabet.LOWER_LAMBDA,
        GreekAlphabet.LOWER_RHO,
        GreekAlphabet.LOWER_SIGMA,  # Voiced when pronounced like Zeta, Smyth § 22
        GreekAlphabet.LOWER_MU,
        GreekAlphabet.LOWER_NU,
        GreekAlphabet.LOWER_ZETA,
        GreekAlphabet.LOWER_UPSILON,  # Vowel
        GreekAlphabet.LOWER_IOTA,  # Vowel

        GAMMA_NASAL,
    ])

    VOICELESS = frozenset([
        GreekAlphabet.LOWER_PI,
        GreekAlphabet.LOWER_TAU,
        GreekAlphabet.LOWER_KAPPA,
        GreekAlphabet.LOWER_PHI,
        GreekAlphabet.LOWER_THETA,
        GreekAlphabet.LOWER_CHI,
        GreekAlphabet.LOWER_SIGMA,
        GreekAlphabet.LOWER_SIGMA_FINAL,  # Only in text
        GreekAlphabet.LOWER_PSI,
        GreekAlphabet.LOWER_XI,
        GreekAlphabet.LOWER_RHO,  # With rough breathing only, Smyth § 15.a
    ])

    LABIAL = frozenset([
        GreekAlphabet.LOWER_MU,
        GreekAlphabet.LOWER_UPSILON,  # Vowel
        GreekAlphabet.LOWER_BETA,
        GreekAlphabet.LOWER_PI,
        GreekAlphabet.LOWER_PHI,
        GreekAlphabet.LOWER_PSI,
    ])

    LINGUALS = frozenset([  # Based on Smyth § 16.a
        GreekAlphabet.LOWER_TAU,
        GreekAlphabet.LOWER_DELTA,
        GreekAlphabet.LOWER_THETA,
    ])

    DENTAL = frozenset([
        GreekAlphabet.LOWER_NU,
        GreekAlphabet.LOWER_LAMBDA,
        GreekAlphabet.LOWER_RHO,
        GreekAlphabet.LOWER_SIGMA,
        GreekAlphabet.LOWER_SIGMA_FINAL,
        # GreekAlphabet.LOWER_DELTA,
        # GreekAlphabet.LOWER_TAU,
        # GreekAlphabet.LOWER_THETA,
        GreekAlphabet.LOWER_ZETA,
    ] | list(LINGUALS))

    PALATIAL = frozenset([
        GreekAlphabet.LOWER_IOTA,
        GreekAlphabet.LOWER_RHO,
        GreekAlphabet.LOWER_GAMMA,
        GreekAlphabet.LOWER_KAPPA,
        GreekAlphabet.LOWER_CHI,
        GreekAlphabet.LOWER_XI,
    ])

    NASALS = frozenset([
        GreekAlphabet.LOWER_MU,
        GreekAlphabet.LOWER_NU,
        GAMMA_NASAL  # Based on Smyth § 19
    ])

    SEMIS = frozenset([
        GreekAlphabet.LOWER_UPSILON,
        GreekAlphabet.LOWER_IOTA,
    ])

    LIQUIDS = frozenset([
        GreekAlphabet.LOWER_LAMBDA,
        GreekAlphabet.LOWER_RHO,  # Initial RHO is always rough breathing
    ])

    SIBILANT = frozenset([  # Sibilant based on Smyth § 17
        GreekAlphabet.LOWER_SIGMA,
    ])

    SPIRANTS = frozenset([
        GreekAlphabet.LOWER_SIGMA_FINAL,
    ] | list(SIBILANT))

    MIDDLE = frozenset([
        GreekAlphabet.LOWER_BETA,
        GreekAlphabet.LOWER_DELTA,
        GreekAlphabet.LOWER_GAMMA,
    ])

    SMOOTH = frozenset([
        GreekAlphabet.LOWER_PI,
        GreekAlphabet.LOWER_TAU,
        GreekAlphabet.LOWER_KAPPA,
    ])

    ROUGH = frozenset([
        GreekAlphabet.LOWER_PHI,
        GreekAlphabet.LOWER_THETA,
        GreekAlphabet.LOWER_CHI
    ])

    ASPIRATES = frozenset([GreekDiacritic.COMBINING_DASIA] | list(ROUGH))  # A group of voiceless consonants

    STOPS = frozenset(set(MIDDLE) | set(SMOOTH) | set(ROUGH))

    DOUBLES = frozenset([
        GreekAlphabet.LOWER_PSI,
        GreekAlphabet.LOWER_ZETA,
        GreekAlphabet.LOWER_XI,
    ])

    CONSONTANTS = frozenset([
        GreekAlphabet.LOWER_BETA, GreekAlphabet.LOWER_GAMMA, GreekAlphabet.LOWER_DELTA, GreekAlphabet.LOWER_ZETA,
        GreekAlphabet.LOWER_THETA, GreekAlphabet.LOWER_KAPPA, GreekAlphabet.LOWER_LAMBDA, GreekAlphabet.LOWER_MU,
        GreekAlphabet.LOWER_NU, GreekAlphabet.LOWER_XI, GreekAlphabet.LOWER_PI, GreekAlphabet.LOWER_RHO,
        GreekAlphabet.LOWER_SIGMA, GreekAlphabet.LOWER_TAU, GreekAlphabet.LOWER_PHI, GreekAlphabet.LOWER_CHI,
        GreekAlphabet.LOWER_PSI,  # Actual consonants

        GreekAlphabet.LOWER_SIGMA_FINAL, GreekAlphabet.LOWER_DIGAMMA  # Necessary consonants
    ])