from pathlib import PurePath
from typing import Tuple

import regex as regex

from greektextify.beta.pdl_standard import PdlBetaStandard
from greektextify.beta.punctuation import BetaPunctuation
from greektextify.nlp.contextual import NlpOperation, NlpContext, ContextObject
from greektextify.roman.word import GreekWordToken
from greektextify.token.bracket import Bracketing
from greektextify.token.quotation import GreekQuotation
from greektextify.token.spacing import Spacing
from greektextify.token.token import Tokenize
from greektextify.beta.word import BetaWord

from greektextify.text.word import GreekWord as GW2


class Example(ContextObject):

    def location(self) -> Tuple:
        return tuple()

    def __init__(self, path: PurePath):
        ContextObject.__init__(self)
        self._path = path
        self._tokenizer = Tokenize([
            BetaWord,
            Bracketing,
            BetaPunctuation,
            GreekQuotation,
            Spacing,
            # GreekHeard,
            # GreekUnheard,
        ], PdlBetaStandard())

    def _parse(self):
        with open(self._path, 'r') as fd:
            for line in fd:
                yield ' '.join(regex.split(r"\[\d+\]", line))

    @NlpOperation()
    def tokenize(self):
        for text in self._parse():
            text = self._tokenizer.standardize(text)
            for token in self._tokenizer.tokenize(text):
                if len(token) > 1:
                    # print(token, GreekWord.romanize(glyphs), GreekWord.pronounce(glyphs))
                    glyphs = BetaWord.glyphen(token)
                    # print(token, "".join([str(glyph) for glyph in glyphs]), GW2.analyze(glyphs))
                    print(GreekWordToken(GW2.analyze(glyphs)))
                else:
                    print(token)


if __name__ == '__main__':
    example = Example(PurePath('jul_or_4.txt'))
    with NlpContext(example):
        example.tokenize()
