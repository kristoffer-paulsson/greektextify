from unittest import TestCase

from greektextify.text.alphabet import GreekAlphabet
from greektextify.text.diphtong import GreekDiphthong
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

    def test_smyth5(self):
        ALPHA_IOTA = tuple([GreekGlyph(GreekAlphabet.LOWER_ALPHA), GreekGlyph(GreekAlphabet.LOWER_IOTA)])
        EPSILON_IOTA = tuple([GreekGlyph(GreekAlphabet.LOWER_EPSILON), GreekGlyph(GreekAlphabet.LOWER_IOTA)])
        OMICRON_IOTA = tuple([GreekGlyph(GreekAlphabet.LOWER_OMICRON), GreekGlyph(GreekAlphabet.LOWER_IOTA)])
        ALPHA_SUBSCRIPT = tuple([GreekGlyph(GreekAlphabet.LOWER_ALPHA, ypogegrammeni=True, macron=True)])
        ETA_SUBSCRIPT = tuple([GreekGlyph(GreekAlphabet.LOWER_ETA, ypogegrammeni=True)])
        OMEGA_SUBSCRIPT = tuple([GreekGlyph(GreekAlphabet.LOWER_OMEGA, ypogegrammeni=True)])

        ALPHA_UPSILON = tuple([GreekGlyph(GreekAlphabet.LOWER_ALPHA), GreekGlyph(GreekAlphabet.LOWER_UPSILON)])
        EPSILON_UPSILON = tuple([GreekGlyph(GreekAlphabet.LOWER_EPSILON), GreekGlyph(GreekAlphabet.LOWER_UPSILON)])
        OMICRON_UPSILON = tuple([GreekGlyph(GreekAlphabet.LOWER_OMICRON), GreekGlyph(GreekAlphabet.LOWER_UPSILON)])
        ETA_UPSILON = tuple([GreekGlyph(GreekAlphabet.LOWER_ETA), GreekGlyph(GreekAlphabet.LOWER_UPSILON)])

        UPSILON_IOTA = tuple([GreekGlyph(GreekAlphabet.LOWER_UPSILON), GreekGlyph(GreekAlphabet.LOWER_IOTA)])

        self.assertEqual(ALPHA_IOTA, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.ALPHA_IOTA).glyphs)[0].affix)
        self.assertEqual(EPSILON_IOTA, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.EPSILON_IOTA).glyphs)[0].affix)
        self.assertEqual(OMICRON_IOTA, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.OMICRON_IOTA).glyphs)[0].affix)
        self.assertEqual(ALPHA_SUBSCRIPT, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.ALPHA_SUBSCRIPT).glyphs)[0].affix)
        self.assertEqual(ETA_SUBSCRIPT, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.ETA_SUBSCRIPT).glyphs)[0].affix)
        self.assertEqual(OMEGA_SUBSCRIPT, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.OMEGA_SUBSCRIPT).glyphs)[0].affix)
        self.assertEqual(ALPHA_UPSILON, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.ALPHA_UPSILON).glyphs)[0].affix)
        self.assertEqual(EPSILON_UPSILON, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.EPSILON_UPSILON).glyphs)[0].affix)
        self.assertEqual(OMICRON_UPSILON, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.OMICRON_UPSILON).glyphs)[0].affix)
        self.assertEqual(ETA_UPSILON, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.ETA_UPSILON).glyphs)[0].affix)
        self.assertEqual(UPSILON_IOTA, GreekDiphthong.diphthong(GreekWord(GreekDiphthong.UPSILON_IOTA).glyphs)[0].affix)
