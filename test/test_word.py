from unittest import TestCase

from greektextify.alphabet import GreekAlphabet
from greektextify.text.diphtong import GreekDiphthong
from greektextify.glyph import GreekGlyph
from greektextify.text.vowel import GreekVowel, IPAVowelLength
from greektextify.token.word import GreekWord


class TestGreekWord(TestCase):
    """The purpose is to only test greek spelling and no whatsoever function or logic."""

    def test_smyth4(self):
        length = (
            IPAVowelLength.SHORT,
            IPAVowelLength.SHORT,
            IPAVowelLength.LONG,
            IPAVowelLength.SHORT,
            IPAVowelLength.SHORT,
            IPAVowelLength.SHORT,
            IPAVowelLength.LONG
        )  # True equals short
        for vowel, short in zip(GreekAlphabet.VOWEL_UPPER, length):
            self.assertEqual(GreekVowel.vowel_length(GreekGlyph(vowel)), short)

        VAR_BREVE = (
            GreekGlyph(GreekAlphabet.UPPER_ALPHA, macron=True),
            GreekGlyph(GreekAlphabet.UPPER_IOTA, macron=True),
            GreekGlyph(GreekAlphabet.UPPER_UPSILON, macron=True),
        )
        for vowel in VAR_BREVE:
            self.assertEqual(GreekVowel.vowel_length(vowel), IPAVowelLength.LONG)

        CIRCUMFLEX = (
            GreekGlyph(GreekAlphabet.UPPER_ALPHA, perispomeni=True),
            GreekGlyph(GreekAlphabet.LOWER_ETA, perispomeni=True),
            GreekGlyph(GreekAlphabet.UPPER_IOTA, perispomeni=True),
            GreekGlyph(GreekAlphabet.UPPER_UPSILON, perispomeni=True),
            GreekGlyph(GreekAlphabet.LOWER_OMEGA, perispomeni=True),
        )
        for vowel in CIRCUMFLEX:
            self.assertEqual(GreekVowel.vowel_length(vowel), IPAVowelLength.LONG)

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

        self.assertEqual(ALPHA_IOTA, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.ALPHA_IOTA))[0].chunk)
        self.assertEqual(EPSILON_IOTA, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.EPSILON_IOTA))[0].chunk)
        self.assertEqual(OMICRON_IOTA, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.OMICRON_IOTA))[0].chunk)
        self.assertEqual(ALPHA_SUBSCRIPT, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.ALPHA_SUBSCRIPT))[0].chunk)
        self.assertEqual(ETA_SUBSCRIPT, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.ETA_SUBSCRIPT))[0].chunk)
        self.assertEqual(OMEGA_SUBSCRIPT, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.OMEGA_SUBSCRIPT))[0].chunk)
        self.assertEqual(ALPHA_UPSILON, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.ALPHA_UPSILON))[0].chunk)
        self.assertEqual(EPSILON_UPSILON, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.EPSILON_UPSILON))[0].chunk)
        self.assertEqual(OMICRON_UPSILON, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.OMICRON_UPSILON))[0].chunk)
        self.assertEqual(ETA_UPSILON, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.ETA_UPSILON))[0].chunk)
        self.assertEqual(UPSILON_IOTA, GreekDiphthong.scan(
            GreekWord.glyphen(GreekDiphthong.UPSILON_IOTA))[0].chunk)

    def text_smyth6(self):
        pass

    def test_smyth138_148(self):
        pass
