import re

import ku

# Before BizrokeRules.py effects:


class Vowel:
    def vowel_change_remove_hemze(self, x):
        """
            simply remove "ئ" when it is located at first position and a vowel is following it
            """
        self.x = x
        return re.sub(re.compile(r"(^ئ|\bئ)([aeêiîouû])"), r"\2", x)

    def vowel_change_y1(self, x):
        """
            changing consonant "ی" to "y"
            """
        self.x = x
        return re.sub(
            re.compile(r"([aeêiîouû]|[^aeêiîouû])(ی)([aeêiîouû])"), r"\1y\3", x
        )

    def vowel_change_y2(self, x):
        """
            changing consonant "ی" to "y" [second rule]
            """
        self.x = x
        return re.sub(
            re.compile(r"([aeêiîouû])(ی)([aeêiîouû]|[^aeêiîouû])"), r"\1y\3", x
        )

    def vowel_change_ii1(self, x):
        """
            changing vowel "ی" to "î"
            """
        self.x = x
        return re.sub(re.compile(r"([^aeêiîouû])(ی$|ی\b)"), r"\1î", x)

    def vowel_change_ii2(self, x):
        """
            changing vowel "ی" to "î" [second rule]
            """
        self.x = x
        return re.sub(re.compile(r"([^aeêiîouû])(ی)([^aeêiîouû])"), r"\1î\3", x)

    def vowel_change_ii3(self, x):
        """
            changing vowel "ی" to "î" [third rule]
            """
        self.x = x
        return re.sub(re.compile(r"(ی$|ی\b)"), r"î", x)

    def vowel_change_w1(self, x):
        """
           changing consonant "و" to "w"
            """
        self.x = x
        return re.sub(
            re.compile(r"([^aeêiîouû]|[aeêiîouû])(و)([aeêiîouû])"), r"\1w\3", x
        )

    def vowel_change_w2(self, x):
        """
            changing consonant "و" to "w" [second rule]
            """
        self.x = x
        return re.sub(re.compile(r"([aeêiîouû])(و)([^aeêiîouû])"), r"\1w\3", x)

    def vowel_change_w3(self, x):
        """
            changing consonant "و" to "w" [third rule]
            """
        self.x = x
        return re.sub(re.compile(r"([aeêiîouû])(و$|و\b)"), r"\1w", x)

    def vowel_change_u1(self, x):
        """
            changing vowel "و" to "u"
            """
        self.x = x
        return re.sub(re.compile(r"([^aeêiîouû])(و)([^aeêiîouû])"), r"\1u\3", x)

    def vowel_change_u2(self, x):
        """
            changing vowel "u + و or وو" to "û"
            """
        self.x = x
        return re.sub(
            re.compile(r"(u)(و)([^aeêiîouû]|[^aeêiîouû]$|[^aeêiîouû]\b)"), r"û\3", x
        )

    def vowel_change_u3(self, x):
        """
            changing "uw" to "û" located at the end
            """
        self.x = x
        return re.sub(re.compile(r"(uw$|uw\b)"), r"û", x)

    def vowel_change_u4(self, x):
        """
            changinf (space/a word + u + space/a word) to (space/a word + û + space/a word)
            """
        self.x = x
        return re.sub(re.compile(r"(\b)(u)(\b)"), r"\1û\3", x)

    def vowel_change_u5(self, x):
        """
            changing "u" at first place + consonant to "w"
            """
        self.x = x
        return re.sub(re.compile(r"(^u|\bu)([^aeêiîouû]{2})"), r"w\2", x)

    def vowel_change_u6(self, x):
        """
            changing "ع" to "'u" at starting place.
            """
        self.x = x
        return re.sub(re.compile(r"(^عu|\bعu)"), r"'u", x)

    def vowel_change_u7(self, x):
        """
            changing "consonant + u" to "consonant + û" at end place.
            """
        self.x = x
        return re.sub(re.compile(r"([^aeêiîouû])(u$|u\b)"), r"\1û", x)

    def vowel_change_u8(self, x):
        """
            changing "consonant + u + ی" to "consonant + w"
            """
        self.x = x
        return re.sub(re.compile(r"([^aeêiîouû])(u)(ی)"), r"\1wî", x)

    def vowel_change_u9(self, x):
        """
            changing "u + consonant + vowel" at starting place --> w
            """
        self.x = x
        return re.sub(re.compile(r"(^u|\bu)([^aeêiîouû])([aeêiîouû])"), r"w\2\3", x)

    def vowel_change_ayn(self, x):
        """
            changing "ع" to "\'". In latin it will be changed to 'u', that is why here it is provided not in conconant section.
            """
        self.x = x
        return re.sub(re.compile(r"(ع)"), r"'", x)

    def vowel_change_uw(self, x):
        """
            changing "consonant + uw + consonant" to "consonant + û + consonant"
            """
        self.x = x
        return re.sub(re.compile(r"([^aeêiîouû])(uw)([^aeêiîouû])"), r"\1û\3", x)

    def vowel_change_yy(self, x):
        """
            changing "ی + u" to "î + w"
            """
        self.x = x
        return re.sub(re.compile(r"([^aeêiîouû])(ی)(u)"), r"\1îw", x)

    def vowel_change_hemze(self, x):
        """
            removing 'ئ' from middle texts
            """
        self.x = x
        return re.sub(re.compile(r"ئ"), r"", x)

    def vowel_rules(self, content):
        """
            Checking all vowel issues related to Latin-based Kurdish text at once
            """
        self.content = content
        all_funcs = (
            Vowel().vowel_change_y1,
            Vowel().vowel_change_y2,
            Vowel().vowel_change_w1,
            Vowel().vowel_change_u1,
            Vowel().vowel_change_ii1,
            Vowel().vowel_change_ii2,
            Vowel().vowel_change_w1,
            Vowel().vowel_change_w2,
            Vowel().vowel_change_w3,
            Vowel().vowel_change_u2,
            Vowel().vowel_change_u3,
            Vowel().vowel_change_u4,
            Vowel().vowel_change_ii2,
            Vowel().vowel_change_uw,
            Vowel().vowel_change_uw,
            Vowel().vowel_change_u1,
            Vowel().vowel_change_u5,
            Vowel().vowel_change_yy,
            Vowel().vowel_change_remove_hemze,
            Vowel().vowel_change_u6,
            Vowel().vowel_change_ayn,
            Vowel().vowel_change_hemze,
            Vowel().vowel_change_ii3,
            Vowel().vowel_change_u7,
            Vowel().vowel_change_u8,
            Vowel().vowel_change_u9,
            Vowel().vowel_change_ii2,
        )
        for func in all_funcs:
            content = func(content)
        return content
