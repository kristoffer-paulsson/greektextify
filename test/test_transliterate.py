from unittest import TestCase

from greektextify.nlp.debug import Debugger
from greektextify.text.word import GreekWord

"""Examples are taken from 'ALA-LC Romanization Tables: Greek' with numerals and modern Greek omitted.
https://www.loc.gov/catdir/cpso/romanization/greek.pdf"""

EXAMPLES = {
    """ΗΣΙΟΔΟΥ ΤΟΥ ΑΣΚΡΑΙΟΥ ΕΡΓΑ ΚΑΙ ΗΜΕΡΑΙ""": '''Hēsiodou tou Askraiou Erga kai hēmerai''',
    """Ἡσιόδου τοῦ Ἀσκραίου Ἔργα καὶ ἡμέραι""": '''Hēsiodou tou Askraiou Erga kai hēmerai''',

    """Η ΤΟΥ ΟΜΗΡΟΥ ΙΛΙΑΣ""": '''Hē tou Homērou Ilias''',
    """Ἡ τοῦ Ὁμήρου Ἰλιάς""": '''Hē tou Homērou Ilias ''',

    """ΦΙΛΗΒΟΣ Η ΠΕΡΙ ΗΔΟΝΗΣ""": '''Philēbos ē Peri hēdonēs''',
    """Φίληβος ἢ Περὶ ἡδονῆς""": '''Philēbos ē Peri hēdonēs''',

    """ΑΓΝΩΣΤΩΙ ΘΕΩΙ""": '''Agnōstō theō''',
    """Ἀγνώστῳ θεῷ""": '''Agnōstō theō''',

    """κεῖται παρ’ Ἅιδῃ""": '''keitai par’ Hadē''',

    """ΑΙΤΙΑ ΡΩΜΑΙΚΑ""": '''Aitia Rhōmaika''',
    """Αἴτια Ῥωμαϊκά""": '''Aitia Rhōmaika''',

    """Ὅτι οὐδ’ ἡδέως ζῆν ἔστι κατ’ Ἐπίκουρον""": '''Hoti oud’ hēdeōs zēn esti kat’ Epikouron''',

    """Περὶ τοῦ μὴ ῥᾳδίως πιστεύειν διαβολῇ""": '''Peri tou mē rhadiōs pisteuein diabolē''',

    """ἀΰπνους νύκτας ἴαυον""": '''aypnous nyktas iauon''',

    """Λητοῦς καὶ Διὸς υἱός""": '''Lētous kai Dios huios''',

    """ὑϊκὸν πάσχειν""": '''hyikon paschein''',

    """εἶπε πρὸς τὸν ἄνδρα τὸν ἑωυτῆς""": '''eipe pros ton andra ton heōutēs''',

    """τί τοῦδ’ ἂν εὕρημ’ ηὗρον εὐτυχέστερον;""": '''ti toud’ an heurēm’ hēuron eutychesteron?''',

    """Τοῦ Κατὰ πασῶν αἱρέσεων ἐλέγχου βιβλίον αʹ""": '''Tou Kata pasōn haireseōn elenchou biblion 1''',

    """καλὸν κἀγαθόν""": '''kalon kagathon''',

    """ᾤχοντο θοἰμάτιον λαβόντες μου""": '''ōchonto thoimation labontes mou''',

    """Περὶ ἰλίγγων""": '''Peri ilingōn''',

    """ὅτε τ’ ἴαχε σάλπιγξ""": '''hote t’ iache salpinx''',

    """Ἐγχειρίδιον ἁρμονικῆς""": '''Encheiridion harmonikēs ''',

    """ἄλαϲτα δὲ ϝέργα πάθον κακὰ μηϲαμένοι""": '''alasta de werga pathon kaka mēsamenoi''',

    """Δαμαρέτα τ’ ἐρατά τε Ϝιανθεμίϲ""": '''Damareta t’ erata te Wianthemis''',

    """ΞΕΝϜΟΣ""": '''xenwos''',
    """ξένϝος""": '''xenwos''',

    """ΠΑΤΡΟϘΛΟΣ""": '''Patroḳlos''',
    """Πάτροϙλος""": '''Patroḳlos''',
}


class TestGreekTransliteration(TestCase):
    """The purpose is to test Greek romanization."""

    def test_transliterate(self):
        for key, value in EXAMPLES.items():
            print(key)
            for row in Debugger.glyph(key):
                print(row)
            print('\n\n')
