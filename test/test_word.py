from unittest import TestCase

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.glyph import GreekGlyph
from greektextify.text.vowels import GreekVowels
from greektextify.text.word import GreekWord


class TestGreekWord(TestCase):
    """The purpose is to only test greek spelling and no whatsoever function or logic."""

    def test_smyth4(self):
        length = (True, True, False, True, True, True, False)  # True equals short
        for vowel, short in zip(GreekAlphabet.VOWEL_UPPER, length):
            self.assertEqual(GreekVowels.is_short(GreekGlyph(vowel)), short)

        VAR_BREVE = (
            GreekGlyph(GreekAlphabet.UPPER_ALPHA, macron=True),
            GreekGlyph(GreekAlphabet.UPPER_IOTA, macron=True),
            GreekGlyph(GreekAlphabet.UPPER_UPSILON, macron=True),
        )
        for vowel in VAR_BREVE:
            self.assertEqual(GreekVowels.is_short(vowel), False)

        CIRCUMFLEX = (
            GreekGlyph(GreekAlphabet.UPPER_ALPHA, perispomeni=True),
            GreekGlyph(GreekAlphabet.LOWER_ETA, perispomeni=True),
            GreekGlyph(GreekAlphabet.UPPER_IOTA, perispomeni=True),
            GreekGlyph(GreekAlphabet.UPPER_UPSILON, perispomeni=True),
            GreekGlyph(GreekAlphabet.LOWER_OMEGA, perispomeni=True),
        )
        for vowel in CIRCUMFLEX:
            self.assertEqual(GreekVowels.is_short(vowel), False)


