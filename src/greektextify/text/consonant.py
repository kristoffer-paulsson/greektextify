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
from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.glyph import GreekGlyph
from greektextify.text.pattern import GlyphPattern


class GreekConsonant:



    GAMMA_NASAL = None  # Only in pronunciation

    LABIAL = frozenset([
        GreekAlphabet.LOWER_MU,
        GreekAlphabet.LOWER_UPSILON,  # Vowel
    ])

    DENTAL = frozenset([
        GreekAlphabet.LOWER_NU,
    ])

    PALATIAL = frozenset([
        GAMMA_NASAL,
        GreekAlphabet.LOWER_IOTA,  # Vowel
    ])

    VOICED = frozenset([
        GreekAlphabet.LOWER_BETA,
        GreekAlphabet.LOWER_DELTA,
        GreekAlphabet.LOWER_GAMMA,
        GreekAlphabet.LOWER_LAMBDA,
        GreekAlphabet.LOWER_RHO,
        GreekAlphabet.LOWER_MU,
        GreekAlphabet.LOWER_NU,
        GAMMA_NASAL,
        GreekAlphabet.LOWER_ZETA,

        GreekAlphabet.LOWER_UPSILON,  # Vowel
        GreekAlphabet.LOWER_IOTA,  # Vowel
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
        GreekAlphabet.LOWER_XI
    ])

    ARRANGED = frozenset([

    ])

    # Nasals, Semivowels, liquids, spirant, stops and double consonants

    STOPS = frozenset([

    ])

    SPIRANTS = frozenset([
        GreekAlphabet.LOWER_SIGMA,
        GreekAlphabet.LOWER_SIGMA_FINAL,  # Only in text
    ])

    LIQUIDS = frozenset([
        GreekAlphabet.LOWER_LAMBDA,
        GreekAlphabet.LOWER_RHO,
    ])

    NASALS = frozenset([
        GreekAlphabet.LOWER_GAMMA
    ])

    SEMI = frozenset([
        GreekAlphabet.LOWER_UPSILON,  # Vowel
        GreekAlphabet.LOWER_IOTA,  # Vowel

    ])

    DOUBLES = frozenset([

    ])


    CONSONTANTS = frozenset([
        GreekAlphabet.LOWER_BETA, GreekAlphabet.LOWER_GAMMA, GreekAlphabet.LOWER_DELTA, GreekAlphabet.LOWER_ZETA,
        GreekAlphabet.LOWER_THETA, GreekAlphabet.LOWER_KAPPA, GreekAlphabet.LOWER_LAMBDA, GreekAlphabet.LOWER_MU,
        GreekAlphabet.LOWER_NU, GreekAlphabet.LOWER_XI, GreekAlphabet.LOWER_PI, GreekAlphabet.LOWER_RHO,
        GreekAlphabet.LOWER_SIGMA, GreekAlphabet.LOWER_TAU, GreekAlphabet.LOWER_PHI, GreekAlphabet.LOWER_CHI,
        GreekAlphabet.LOWER_PSI,  # Actual consonants

        GreekAlphabet.LOWER_SIGMA_FINAL, GreekAlphabet.LOWER_DIGAMMA  # Necessary consonants
    ])



GREEK_GAMMA_NASAL = frozenset([  # Gamma-nasal patterns according to Smyth § 19.a
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_GAMMA),
        GreekGlyph(GreekAlphabet.LOWER_GAMMA)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_GAMMA),
        GreekGlyph(GreekAlphabet.LOWER_KAPPA)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_GAMMA),
        GreekGlyph(GreekAlphabet.LOWER_XI)
    ])),
    GlyphPattern(tuple([
        GreekGlyph(GreekAlphabet.LOWER_GAMMA),
        GreekGlyph(GreekAlphabet.LOWER_CHI)
    ])),
])