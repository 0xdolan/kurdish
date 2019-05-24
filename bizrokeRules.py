import re

alphabet = "bcçdfghjklĺmnpqrŕsştvwxzaeêiîouûy"
consonants = "bcçdfghjklĺmnpqrŕsştvwxz"
vowels = "aeêiîouûy"


class Bizroke:
    def add_rule_01(self, x):
        """
            e.g. grft -> grift
            """
        self.x = x
        return re.sub(
            re.compile(
                r"([bcçdfghjklĺmnpqrŕsştvwxz])([fjlĺmnrŕsşvwxyz])([fjlĺmnrŕsşvwxyz])([^aeêiîouûy])"
            ),
            r"\1\2i\3\4",
            x,
        )

    def add_rule_02(self, x):
        """
            e.g. cejnt -> cejnit
            """
        self.x = x
        return re.sub(
            re.compile(
                r"([aeêiîouû])([bcçdfghjklĺmnpqrŕsştvwxz])([bcçdfghjklĺmnpqrŕsştvwxz])([bcçdfghjklĺmnpqrŕsştvwxz])"
            ),
            r"\1\2\3i\4",
            x,
        )

    def add_rule_03(self, x):
        """
            e.g. wrd --> wird
            """
        self.x = x
        return re.sub(
            re.compile(
                r"([fjlĺrŕsşwyz])([fjlĺmnrŕsşvwxyz])([bcçdfghjklĺmnpqrŕsştvwxz])"
            ),
            r"\1i\2\3",
            x,
        )

    def add_rule_04(self, x):
        """
            e.g. prd --> pird
            """
        self.x = x
        return re.sub(
            re.compile(r"([bcçdghĥkmnpqtvx])([fjlĺmnrŕsşvwxyz])($|[^aeêiîouû])"),
            r"\1i\2\3",
            x,
        )

    def add_rule_05(self, x):
        """
            e.g. ktk --> kitk
            """
        self.x = x
        return re.sub(
            re.compile(
                r"(^|[^aeêiîouy])([bcçdfghjklĺmnpqrŕsştvwxz])([bcçdfghjklĺmnpqrŕsştvwxz])($|[^aeêiîouû])"
            ),
            r"\1\2i\3\4",
            x,
        )

    def add_rule_06(self, x):
        """
            e.g. j --> ji / ç --> çi
            """
        self.x = x
        return re.sub(
            re.compile(r"(^|[^a-zçşêîûĺŕ\'])([bcçdfghjklĺmnpqrŕsştvwxz])(\b)"),
            r"\1\2i\3",
            x,
        )

    def re_rule_01(self, x):
        """
            e.g. Ŕabridû --> Ŕabirdû
            """
        self.x = x
        return re.sub(
            re.compile(
                r"([aeou]?)([brcmxkwtdzhpgĺ])([nlsrmzĺrş])(i)([rcdmtbsŕnkg][lnw]?)([aêîueo]?)"
            ),
            r"\1\2\4\3\5\6",
            x,
        )

    def re_rule_02(self, x):
        """
            e.g. daŕşitin --> daŕiştin
            """
        self.x = x
        return re.sub(re.compile(r"([ŕ])([ş])(i)([t])(i?)([n])"), r"\1i\2\4\5\6", x)

    def rm_rule_01(self, x):
        """
            e.g. aşkiray --> aşkray
            """
        self.x = x
        return re.sub(
            re.compile(r"([şsnĺlrŕz])([ktgfbşdc])(i)([rŕhpwşkdxtnjgbm])([aeêîo])"),
            r"\1\2\4\5",
            x,
        )

    def rm_rule_02(self, x):
        """
            removing bizroke "i"
            e.g. Feŕenisiyekan --> Feŕensyekan
            """
        self.x = x
        return re.sub(re.compile(r"([n])(i)([s])(i?)([y])([aeêiîouû])"), r"\1\3\5\6", x)

    def rm_rule_03(self, x):
        """
            removing bizroke "i"
            e.g. xodewĺemendikirdin --> xodewĺemendkirdin
            e.g. bunyadinirawe --> bunyadnirawe
            """
        self.x = x
        return re.sub(
            re.compile(r"([^aeêiîouû])(i)([^aeêiîouû])(i)([^aeêiîouû])"), r"\1\3\4\5", x
        )

    def extra_add_rule_01(self, x):
        """
            adding bizroke "i"
            e.g. Bŕewêndrênewe --> Bŕewêndirênewe
            """
        self.x = x
        return re.sub(re.compile(r"([nd])([r][aeêiîouû])"), r"\1i\2", x)

    def extra_add_rule_02(self, x):
        """
            adding bizroke "i"
            e.g. trîn --> tirîn
            """
        self.x = x
        return re.sub(re.compile(r"(t)(r)(î)(n)"), r"\1i\2\3\4", x)

    def bizroke(self, content):
        """
            Bizroke function will try to add or remove extra bizroke (i) to the needed places.
            Some of the rules borrowed from Pellk (http://chawg.org) but lots of modifications and addition rules have been provided.
            """
        self.content = content
        all_funcs = (
            Bizroke().add_rule_02,
            Bizroke().add_rule_01,
            Bizroke().add_rule_03,
            Bizroke().add_rule_04,
            Bizroke().add_rule_05,
            Bizroke().add_rule_06,
            Bizroke().re_rule_01,
            Bizroke().re_rule_02,
            Bizroke().rm_rule_01,
            Bizroke().rm_rule_02,
            Bizroke().extra_add_rule_01,
            Bizroke().rm_rule_03,
        )

        for func in all_funcs:
            content = func(content)
        return content

