from pathlib import PurePath
from pprint import pp
from typing import Tuple

import regex as regex

from greektextify.nlp.contextual import NlpOperation, NlpContext, ContextObject
from greektextify.roman.word import GreekWordToken
from greektextify.token.bracket import Bracketing
from greektextify.token.pdl_standard import PdlUtfStandard
from greektextify.token.punctuation import GreekPunctuation
from greektextify.token.quotation import GreekQuotation
from greektextify.token.spacing import Spacing
from greektextify.token.token import Tokenize
from greektextify.token.word import GreekWord

from greektextify.text.word import GreekWord as GW2


class Example(ContextObject):

    def location(self) -> Tuple:
        return tuple()

    def __init__(self, path: PurePath):
        ContextObject.__init__(self)
        self._path = path
        self._tokenizer = Tokenize([
            GreekWord,
            Bracketing,
            GreekPunctuation,
            GreekQuotation,
            Spacing,
            # GreekHeard,
            # GreekUnheard,
        ], PdlUtfStandard())

    def _parse(self):
        with open(self._path, 'r') as fd:
            for line in fd:
                yield ' '.join(regex.split(r"\[\d+\]", line))

    @NlpOperation()
    def tokenize(self):
        tokens = list()
        for text in self._parse():
            text = self._tokenizer.standardize(text)
            for token in self._tokenizer.tokenize(text):
                if len(token) > 1 or token.isalpha():
                    tokens.append(GreekWordToken(GW2.analyze(GreekWord.glyphen(token))).__str__())
                else:
                    tokens.append(token)
        return " ".join(tokens)


if __name__ == '__main__':
    example = Example(PurePath('john_3.txt'))
    with NlpContext(example):
        pp(example.tokenize())
