import re
from unicodedata import name

import bizrokeRules
import punctuation
import vowelIssues


class Hemwar:
    """
    Kurdish Language Library for transliteration from Arabic-based Kurdish
    to Latin one. It can also be used for converting characters
    and digits in Persian, English and Arabic to Kurdish and vice versa.
    Latest update: May 2019
    Dolan Hêriş (dolanskurd@mail.com)
    Kurdish Language Library is available under the MIT license
    GitHub: https://github.com/dolanskurd/Kurdish
    """

    """A collection of both, Arabic-based Kurdish and Latin-based Kurdish, alphabets in string.

    ku_alphabet_Ar_C -- a string containing all Arabic-based Kurdish consonants
    ku_alphabet_Ar_V -- a string containing all Arabic-based Kurdish vowels
    ku_alphabet_Ar_Digits -- a string containing all Arabic-based Kurdish digits
    ku_alphabet_La_C -- a string containing all Latin-based Kurdish consonants
    ku_alphabet_La_V -- a string containing all Latin-based Kurdish vowels
    ku_alphabet_La_all -- a string containing all Latin-based Kurdish consonants and vowels
    ku_all_Va -- string containing all Latin-based Kurdish and Arabic-based Kurdish vowels
    Persian_Digits -- a string containing all Arabic-based Persian digits
    Ar_Special_chars -- a string containing all special Arabic characters (NOT be used in Arabic-based Kurdish)
    
    ku_alphabet_Ar_C = "ئبپتجچحخدرڕزژسشعغفڤقکگلڵمنه"
    ku_alphabet_Ar_V = "اەوۆوویێ"
    ku_alphabet_Ar_Digits = "٠١٢٣٤٥٦٧٨٩"
    ku_alphabet_La_uppercase = "ABCÇDEÊFGHĤIÎJKLĹMNOPQRŔSŞTUÛVWXẌYZ"
    ku_alphabet_La_lowercase = "abcçdeêfghĥiîjklĺmnopqrŕsştuûvwxẍyz"
    ku_alphabet_La_C = "BCÇDFGHĤJKLĹMNPQRŔSŞTVWXẌYZbcçdfghĥjklĺmnpqrŕsştvwxẍyz"
    ku_alphabet_La_V = "AEÊIÎOUÛaeêiîouû"
    ku_alphabet_La_Digits = "0123456789"
    ku_all_V = "AEÊIÎOUÛaeêiîouûاەوۆوویێ"
    Persian_Digits = "۰۱۲۳۴۵۶۷۸۹"
    Ar_Special_chars = "صضطظذيةثؤأإآكۀى"
    
    """
    ku_alphabet_Ar_C = "ئبپتجچحخدرڕزژسشعغفڤقکگلڵمنه"
    ku_alphabet_Ar_V = "اەوۆوویێ"
    ku_alphabet_Ar = ku_alphabet_Ar_C + ku_alphabet_Ar_V
    ku_alphabet_Ar_Digits = "٠١٢٣٤٥٦٧٨٩"
    ku_alphabet_La_uppercase = "ABCÇDEÊFGHĤIÎJKLĹMNOPQRŔSŞTUÛVWXẌYZ"
    ku_alphabet_La_lowercase = "abcçdeêfghĥiîjklĺmnopqrŕsştuûvwxẍyz"
    ku_alphabet_La_C = "BCÇDFGHĤJKLĹMNPQRŔSŞTVWXẌYZbcçdfghĥjklĺmnpqrŕsştvwxẍyz"
    ku_alphabet_La_V = "AEÊIÎOUÛaeêiîouû"
    ku_alphabet_La_all = ku_alphabet_La_C + ku_alphabet_La_V
    ku_alphabet_La_Digits = "0123456789"
    ku_all_V = "AEÊIÎOUÛaeêiîouûاەوۆوویێ"
    Persian_Digits = "۰۱۲۳۴۵۶۷۸۹"
    Ar_Special_chars = "صضطظذيةثؤأإآكۀى"

    def replace_func(self, mapping, content):
        """Replacing code in converting alphabet characters"""
        self.mapping = mapping
        self.content = content

        pattern = "|".join(map(re.escape, mapping.keys()))
        return re.sub(pattern, lambda uni: mapping[uni.group()], str(content))

    def En_Digit_to_Ku(self, textContent):
        """Converting English digits to Kurdish digits
        '0': '٠', # It changes U+0030 to U+0660
        '1': '١', # It changes U+0031 to U+0661
        '2': '٢', # It changes U+0032 to U+0662
        '3': '٣', # It changes U+0033 to U+0663
        '4': '٤', # It changes U+0034 to U+0664
        '5': '٥', # It changes U+0035 to U+0665
        '6': '٦', # It changes U+0036 to U+0666
        '7': '٧', # It changes U+0037 to U+0667
        '8': '٨', # It changes U+0038 to U+0668
        '9': '٩', # It changes U+0039 to U+0669
        """
        self.textContent = textContent

        mapping = {
            "0": "٠",  # It changes U+0030 to U+0660
            "1": "١",  # It changes U+0031 to U+0661
            "2": "٢",  # It changes U+0032 to U+0662
            "3": "٣",  # It changes U+0033 to U+0663
            "4": "٤",  # It changes U+0034 to U+0664
            "5": "٥",  # It changes U+0035 to U+0665
            "6": "٦",  # It changes U+0036 to U+0666
            "7": "٧",  # It changes U+0037 to U+0667
            "8": "٨",  # It changes U+0038 to U+0668
            "9": "٩",  # It changes U+0039 to U+0669
        }
        return Hemwar().replace_func(mapping, textContent)

    def Ku_Digit_to_En(self, textContent):
        """Converting Kurdish digits to English digits
        '٠': '0', # It changes U+0660 to U+0030
        '١': '1', # It changes U+0661 to U+0031
        '٢': '2', # It changes U+0662 to U+0032
        '٣': '3', # It changes U+0663 to U+0033
        '٤': '4', # It changes U+0664 to U+0034
        '٥': '5', # It changes U+0665 to U+0035
        '٦': '6', # It changes U+0666 to U+0036
        '٧': '7', # It changes U+0667 to U+0037
        '٨': '8', # It changes U+0668 to U+0038
        '٩': '9', # It changes U+0669 to U+0039
        """
        self.textContent = textContent
        mapping = {
            "٠": "0",  # It changes U+0660 to U+0030
            "١": "1",  # It changes U+0661 to U+0031
            "٢": "2",  # It changes U+0662 to U+0032
            "٣": "3",  # It changes U+0663 to U+0033
            "٤": "4",  # It changes U+0664 to U+0034
            "٥": "5",  # It changes U+0665 to U+0035
            "٦": "6",  # It changes U+0666 to U+0036
            "٧": "7",  # It changes U+0667 to U+0037
            "٨": "8",  # It changes U+0668 to U+0038
            "٩": "9",  # It changes U+0669 to U+0039
        }
        return Hemwar().replace_func(mapping, textContent)

    def Fa_Digit_to_Ku(self, textContent):
        """Converting the Persian (Farsi) digits to the Arabic-based Kurdish digits.
        It is also converting the Persian (Farsi) digits to the Arabic digits
        as the Arabic-based Kurdish and the Arabic digits are the same.
        "۰": "٠", # It changes U+06F0 to U+0660
        "۱": "١", # It changes U+06F1 to U+0661
        "۲": "٢", # It changes U+06F2 to U+0662
        "۳": "٣", # It changes U+06F3 to U+0663
        "۴": "٤", # It changes U+06F4 to U+0664
        "۵": "٥", # It changes U+06F5 to U+0665
        "۶": "٦", # It changes U+06F6 to U+0666
        "۷": "٧", # It changes U+06F7 to U+0667
        "۸": "٨", # It changes U+06F8 to U+0668
        "۹": "٩"  # It changes U+06F9 to U+0669
        """
        self.textContent = textContent
        mapping = {
            "۰": "٠",  # It changes U+06F0 to U+0660
            "۱": "١",  # It changes U+06F1 to U+0661
            "۲": "٢",  # It changes U+06F2 to U+0662
            "۳": "٣",  # It changes U+06F3 to U+0663
            "۴": "٤",  # It changes U+06F4 to U+0664
            "۵": "٥",  # It changes U+06F5 to U+0665
            "۶": "٦",  # It changes U+06F6 to U+0666
            "۷": "٧",  # It changes U+06F7 to U+0667
            "۸": "٨",  # It changes U+06F8 to U+0668
            "۹": "٩",  # It changes U+06F9 to U+0669
        }
        return Hemwar().replace_func(mapping, textContent)

    def Ku_Digit_to_Fa(self, textContent):
        """Converting the Arabic-based Kurdish digits to the Persian (Farsi) digits.
        It is also converting the Arabic digits to the Persian (Farsi) digits
        as the Arabic-based Kurdish and the Arabic digits are the same.
        "٠": "۰", # It changes U+0660 to U+06F0
        "١": "۱", # It changes U+0661 to U+06F1
        "٢": "۲", # It changes U+0662 to U+06F2
        "٣": "۳", # It changes U+0663 to U+06F3
        "٤": "۴", # It changes U+0664 to U+06F4
        "٥": "۵", # It changes U+0665 to U+06F5
        "٦": "۶", # It changes U+0666 to U+06F6
        "٧": "۷", # It changes U+0667 to U+06F7
        "٨": "۸", # It changes U+0668 to U+06F8
        "٩": "۹" # It changes U+0669 to U+06F9
        """
        self.textContent = textContent
        mapping = {
            "٠": "۰",  # It changes U+0660 to U+06F0
            "١": "۱",  # It changes U+0661 to U+06F1
            "٢": "۲",  # It changes U+0662 to U+06F2
            "٣": "۳",  # It changes U+0663 to U+06F3
            "٤": "۴",  # It changes U+0664 to U+06F4
            "٥": "۵",  # It changes U+0665 to U+06F5
            "٦": "۶",  # It changes U+0666 to U+06F6
            "٧": "۷",  # It changes U+0667 to U+06F7
            "٨": "۸",  # It changes U+0668 to U+06F8
            "٩": "۹",  # It changes U+0669 to U+06F9
        }
        return Hemwar().replace_func(mapping, textContent)

    def En_Digit_to_Fa(self, textContent):
        """Converting English digits to Persian (Farsi) digits
        '0': '۰', # It changes U+0030 to U+06F0
        '1': '۱', # It changes U+0031 to U+06F1
        '2': '۲', # It changes U+0032 to U+06F2
        '3': '۳', # It changes U+0033 to U+06F3
        '4': '۴', # It changes U+0034 to U+06F4
        '5': '۵', # It changes U+0035 to U+06F5
        '6': '۶', # It changes U+0036 to U+06F6
        '7': '۷', # It changes U+0037 to U+06F7
        '8': '۸', # It changes U+0038 to U+06F8
        '9': '۹', # It changes U+0039 to U+06F9
        """
        self.textContent = textContent

        mapping = {
            "0": "۰",  # It changes U+0030 to U+06F0
            "1": "۱",  # It changes U+0031 to U+06F1
            "2": "۲",  # It changes U+0032 to U+06F2
            "3": "۳",  # It changes U+0033 to U+06F3
            "4": "۴",  # It changes U+0034 to U+06F4
            "5": "۵",  # It changes U+0035 to U+06F5
            "6": "۶",  # It changes U+0036 to U+06F6
            "7": "۷",  # It changes U+0037 to U+06F7
            "8": "۸",  # It changes U+0038 to U+06F8
            "9": "۹",  # It changes U+0039 to U+06F9
        }
        return Hemwar().replace_func(mapping, textContent)

    def Fa_Digit_to_En(self, textContent):
        """Converting Persian (Farsi) digits to English digits
        '۰': '0', # It changes U+06F0 to U+0030
        '۱': '1', # It changes U+06F1 to U+0031
        '۲': '2', # It changes U+06F2 to U+0032
        '۳': '3', # It changes U+06F3 to U+0033
        '۴': '4', # It changes U+06F4 to U+0034
        '۵': '5', # It changes U+06F5 to U+0035
        '۶': '6', # It changes U+06F6 to U+0036
        '۷': '7', # It changes U+06F7 to U+0037
        '۸': '8', # It changes U+06F8 to U+0038
        '۹': '9', # It changes U+06F9 to U+0039
        """
        self.textContent = textContent
        mapping = {
            "۰": "0",  # It changes U+06F0 to U+0030
            "۱": "1",  # It changes U+06F1 to U+0031
            "۲": "2",  # It changes U+06F2 to U+0032
            "۳": "3",  # It changes U+06F3 to U+0033
            "۴": "4",  # It changes U+06F4 to U+0034
            "۵": "5",  # It changes U+06F5 to U+0035
            "۶": "6",  # It changes U+06F6 to U+0036
            "۷": "7",  # It changes U+06F7 to U+0037
            "۸": "8",  # It changes U+06F8 to U+0038
            "۹": "9",  # It changes U+06F9 to U+0039
        }
        return Hemwar().replace_func(mapping, textContent)

    def En_Char_to_Ku(self, textContent):
        """Converting the English characters to the Arabic-based Kurdish characters, based
        on KurdITGroup Keyboard System (https://www.kurditgroup.org/).
        there is some minor changes which is described across each of them.
        'u': 'ئ', # It changes U+0075 to U+0626
        'a': 'ا', # It changes U+0061 to U+0627
        'b': 'ب', # It changes U+0062 to U+0628
        'p': 'پ', # It changes U+0070 to U+067E
        't': 'ت', # It changes U+0074 to U+062A
        'c': 'ج', # It changes U+0063 to U+062C
        'C': 'چ', # It changes U+0043 to U+0686
        'I': 'ح', # It changes U+0049 to U+062D
        'x': 'خ', # It changes U+0078 to U+062E
        'd': 'د', # It changes U+0064 to U+062F
        'r': 'ر', # It changes U+0072 to U+0631
        'R': 'ڕ', # It changes U+0052 to U+0695
        'z': 'ز', # It changes U+007A to U+0632
        'j': 'ژ', # It changes U+006A to U+0698
        's': 'س', # It changes U+0073 to U+0633
        'S': 'ش', # It changes U+0053 to U+0634
        'i': 'ع', # It changes U+0069 to U+0639
        'G': 'غ', # It changes U+0047 to U+063A
        'f': 'ف', # It changes U+0066 to U+0641
        'v': 'ڤ', # It changes U+0076 to U+06A4
        'q': 'ق', # It changes U+0071 to U+0642
        'k': 'ک', # It changes U+006B to U+06A9
        'g': 'گ', # It changes U+0067 to U+06AF
        'l': 'ل', # It changes U+006C to U+0644
        'L': 'ڵ', # It changes U+004C to U+06B5
        'm': 'م', # It changes U+006D to U+0645
        'n': 'ن', # It changes U+006E to U+0646
        'w': 'و', # It changes U+0077 to U+0648
        'o': 'ۆ', # It changes U+006F to U+06C6
        'h': 'ه', # It changes U+0068 to U+0647 (NOT U+06BE 'ھ')
        'e': 'ە', # It changes U+0065 to U+06D5
        'y': 'ی', # It changes U+0079 to U+06CC
        'Y': 'ێ', # It changes U+0059 to U+06CE
        ',': '،', # It changes U+002C to U+060C
        '?': '؟', # It changes U+003F to U+061F
        ';': '؛', # It changes U+003B to U+061B
        '(': '(', # It changes U+0028 to U+0028
        ')': ')', # It changes U+0029 to U+0029
        '[': '[', # It changes U+005B to U+005B
        ']': ']', # It changes U+005D to U+005D
        '{': '{', # It changes U+007B to U+007B
        '}': '}' # It changes U+007D to U+007D
        """
        self.textContent = textContent
        mapping = {
            "u": "ئ",  # It changes U+0075 to U+0626
            "a": "ا",  # It changes U+0061 to U+0627
            "b": "ب",  # It changes U+0062 to U+0628
            "p": "پ",  # It changes U+0070 to U+067E
            "t": "ت",  # It changes U+0074 to U+062A
            "c": "ج",  # It changes U+0063 to U+062C
            "C": "چ",  # It changes U+0043 to U+0686
            "I": "ح",  # It changes U+0049 to U+062D
            "x": "خ",  # It changes U+0078 to U+062E
            "d": "د",  # It changes U+0064 to U+062F
            "r": "ر",  # It changes U+0072 to U+0631
            "R": "ڕ",  # It changes U+0052 to U+0695
            "z": "ز",  # It changes U+007A to U+0632
            "j": "ژ",  # It changes U+006A to U+0698
            "s": "س",  # It changes U+0073 to U+0633
            "S": "ش",  # It changes U+0053 to U+0634
            "i": "ع",  # It changes U+0069 to U+0639
            "G": "غ",  # It changes U+0047 to U+063A
            "f": "ف",  # It changes U+0066 to U+0641
            "v": "ڤ",  # It changes U+0076 to U+06A4
            "q": "ق",  # It changes U+0071 to U+0642
            "k": "ک",  # It changes U+006B to U+06A9
            "g": "گ",  # It changes U+0067 to U+06AF
            "l": "ل",  # It changes U+006C to U+0644
            "L": "ڵ",  # It changes U+004C to U+06B5
            "m": "م",  # It changes U+006D to U+0645
            "n": "ن",  # It changes U+006E to U+0646
            "w": "و",  # It changes U+0077 to U+0648
            "o": "ۆ",  # It changes U+006F to U+06C6
            "h": "ه",  # It changes U+0068 to U+0647 (NOT U+06BE 'ھ')
            "e": "ە",  # It changes U+0065 to U+06D5
            "y": "ی",  # It changes U+0079 to U+06CC
            "Y": "ێ",  # It changes U+0059 to U+06CE
            ",": "،",  # It changes U+002C to U+060C
            "?": "؟",  # It changes U+003F to U+061F
            ";": "؛",  # It changes U+003B to U+061B
            "(": "(",  # It changes U+0028 to U+0028
            ")": ")",  # It changes U+0029 to U+0029
            "[": "[",  # It changes U+005B to U+005B
            "]": "]",  # It changes U+005D to U+005D
            "{": "{",  # It changes U+007B to U+007B
            "}": "}",  # It changes U+007D to U+007D
        }
        return Hemwar().replace_func(mapping, textContent)

    def Ku_Char_to_En(self, textContent):
        """Converting Arabic-based Kurdish characters to English characters, based on
        KurdITGroup Keyboard System (https://www.kurditgroup.org/)
        'ئ': 'u', # It changes U+0626 to U+0075
        'ا': 'a', # It changes U+0627 to U+0061
        'ب': 'b', # It changes U+0628 to U+0062
        'پ': 'p', # It changes U+067E to U+0070
        'ت': 't', # It changes U+062A to U+0074
        'ج': 'c', # It changes U+062C to U+0063
        'چ': 'C', # It changes U+0686 to U+0043
        'ح': 'I', # It changes U+062D to U+0049
        'خ': 'x', # It changes U+062E to U+0078
        'د': 'd', # It changes U+062F to U+0064
        'ر': 'r', # It changes U+0631 to U+0072
        'ڕ': 'R', # It changes U+0695 to U+0052
        'ز': 'z', # It changes U+0632 to U+007A
        'ژ': 'j', # It changes U+0698 to U+006A
        'س': 's', # It changes U+0633 to U+0073
        'ش': 'S', # It changes U+0634 to U+0053
        'ع': 'i', # It changes U+0639 to U+0069
        'غ': 'G', # It changes U+063A to U+0047
        'ف': 'f', # It changes U+0641 to U+0066
        'ڤ': 'v', # It changes U+06A4 to U+0076
        'ق': 'q', # It changes U+0642 to U+0071
        'ک': 'k', # It changes U+06A9 to U+006B
        'گ': 'g', # It changes U+06AF to U+0067
        'ل': 'l', # It changes U+0644 to U+006C
        'ڵ': 'L', # It changes U+06B5 to U+004C
        'م': 'm', # It changes U+0645 to U+006D
        'ن': 'n', # It changes U+0646 to U+006E
        'و': 'w', # It changes U+0648 to U+0077
        'ۆ': 'o', # It changes U+06C6 to U+006F
        'ه': 'h', # It changes U+0647 to U+0068 (NOT U+06BE 'ھ')
        'ە': 'e', # It changes U+06D5 to U+0065
        'ی': 'y', # It changes U+06CC to U+0079
        'ێ': 'Y', # It changes U+06CE to U+0059
        '،': ',' # It changes U+060C to U+002C
        '؟': '?', # It changes to U+061F to U+003F
        '؛': ';', # It changes to U+061B to U+003B
        '(': '(', # It changes to U+0028 to U+0028
        ')': ')', # It changes to U+0029 to U+0029
        '[': '[', # It changes to U+005B to U+005B
        ']': ']', # It changes to U+005D to U+005D
        '{': '{', # It changes to U+007B to U+007B
        '}': '}', # It changes to U+007D to U+007D
        """
        self.textContent = textContent
        mapping = {
            "ئ": "u",  # It changes U+0626 to U+0075
            "ا": "a",  # It changes U+0627 to U+0061
            "ب": "b",  # It changes U+0628 to U+0062
            "پ": "p",  # It changes U+067E to U+0070
            "ت": "t",  # It changes U+062A to U+0074
            "ج": "c",  # It changes U+062C to U+0063
            "چ": "C",  # It changes U+0686 to U+0043
            "ح": "I",  # It changes U+062D to U+0049
            "خ": "x",  # It changes U+062E to U+0078
            "د": "d",  # It changes U+062F to U+0064
            "ر": "r",  # It changes U+0631 to U+0072
            "ڕ": "R",  # It changes U+0695 to U+0052
            "ز": "z",  # It changes U+0632 to U+007A
            "ژ": "j",  # It changes U+0698 to U+006A
            "س": "s",  # It changes U+0633 to U+0073
            "ش": "S",  # It changes U+0634 to U+0053
            "ع": "i",  # It changes U+0639 to U+0069
            "غ": "G",  # It changes U+063A to U+0047
            "ف": "f",  # It changes U+0641 to U+0066
            "ڤ": "v",  # It changes U+06A4 to U+0076
            "ق": "q",  # It changes U+0642 to U+0071
            "ک": "k",  # It changes U+06A9 to U+006B
            "گ": "g",  # It changes U+06AF to U+0067
            "ل": "l",  # It changes U+0644 to U+006C
            "ڵ": "L",  # It changes U+06B5 to U+004C
            "م": "m",  # It changes U+0645 to U+006D
            "ن": "n",  # It changes U+0646 to U+006E
            "و": "w",  # It changes U+0648 to U+0077
            "ۆ": "o",  # It changes U+06C6 to U+006F
            "ه": "h",  # It changes U+0647 to U+0068 (NOT U+06BE 'ھ')
            "ە": "e",  # It changes U+06D5 to U+0065
            "ی": "y",  # It changes U+06CC to U+0079
            "ێ": "Y",  # It changes U+06CE to U+0059
            "،": ",",  # It changes U+060C to U+002C
            "؟": "?",  # It changes to U+061F to U+003F
            "؛": ";",  # It changes to U+061B to U+003B
            "(": "(",  # It changes to U+0028 to U+0028
            ")": ")",  # It changes to U+0029 to U+0029
            "[": "[",  # It changes to U+005B to U+005B
            "]": "]",  # It changes to U+005D to U+005D
            "{": "{",  # It changes to U+007B to U+007B
            "}": "}",  # It changes to U+007D to U+007D
        }
        return Hemwar().replace_func(mapping, textContent)

    def Ar_Char_to_Ku(self, textContent):
        """Converting Arabic characters to Arabic-based Kurdish characters.
        It is also Converting Arabic characters to Persian (Farsi) characters
        as Arabic-based Kurdish and Persian (Farsi) versions are the same.
        'ك': 'ک', # It changes U+0643 to U+06A9
        'ڪ': 'ک', # It changes U+06AA to U+06A9
        'ي': 'ی', # It changes U+064A to U+06CC
        'ى': 'ی', # It changes U+0649 to U+06CC
        'ے': 'ی', # It changes U+06D2 to U+06CC
        'ة': 'ە', # It changes U+0629 to U+06D5
        'ۂ': 'ە', # It changes U+06C2 to U+06D5
        'ۀ': 'ە', # It changes U+06C0 to U+06D5
        '‌ه': 'ە', # It changes (U+0647 + U+200C) to U+06D5 --> two characters to one
        '‌ە': 'ە', # It changes (U+06D5 + U+200C) to U+06D5 --> two characters to one
        'ؤ': 'و', # It changes U+0624 to U+0648
        'ٶ': 'و', # It changes U+0676 to U+0648
        'ۊ': 'و', # It changes U+06CA to U+0648
        'أ': 'ا', # It changes U+0623 to U+0627
        'ﺃ': 'ا', # It changes U+FE83 to U+0627
        'إ': 'ا', # It changes U+0625 to U+0627
        'ﺇ': 'ا' # It changes U+FE87 to U+0627
        """
        self.textContent = textContent
        mapping = {
            "ك": "ک",  # It changes U+0643 to U+06A9
            "ڪ": "ک",  # It changes U+06AA to U+06A9
            "ي": "ی",  # It changes U+064A to U+06CC
            "ى": "ی",  # It changes U+0649 to U+06CC
            "ے": "ی",  # It changes U+06D2 to U+06CC
            "ة": "ە",  # It changes U+0629 to U+06D5
            "ۂ": "ە",  # It changes U+06C2 to U+06D5
            "ۀ": "ە",  # It changes U+06C0 to U+06D5
            "‌ه": "ە",  # It changes (U+0647 + U+200C) to U+06D5 --> two characters to one
            "‌ە": "ە",  # It changes (U+06D5 + U+200C) to U+06D5 --> two characters to one
            "ؤ": "و",  # It changes U+0624 to U+0648
            "ٶ": "و",  # It changes U+0676 to U+0648
            "ۊ": "و",  # It changes U+06CA to U+0648
            "أ": "ا",  # It changes U+0623 to U+0627
            "ﺃ": "ا",  # It changes U+FE83 to U+0627
            "إ": "ا",  # It changes U+0625 to U+0627
            "ﺇ": "ا",  # It changes U+FE87 to U+0627
        }
        return Hemwar().replace_func(mapping, textContent)

    def getUniNum(self, x):
        """Get the Unicode details of the character or digit"""
        self.x = x

        for i, char in enumerate(x, start=1):
            print(str(i) + ".", char, "= U+%04x" % ord(char), name(char))
        return "\nConversion has been completed successfully.\n"

    def V_or_C(self, x):
        """ Under Progress !!!
            Checking the Arabic-based and Latin-based Kurdish characters if it is vowel or consonant"""
        self.x = x

        for index, i in enumerate(x, start=1):
            if i.isdigit():
                print(str(index) + ".", str('" ' + i + ' "'), "is a digit.")
            elif not i.isalpha() and i == " ":
                print(
                    str(index)
                    + "."
                    + str('"' + i + '"')
                    + ", Select a valuable character. Space is not valid!"
                )
            elif i == "و" or i == "ی":
                print(
                    str(index) + ".",
                    "If the word started with "
                    + str('" ' + i + ' "')
                    + " so it is Consonant otherwise it is Vowel.",
                )
            elif i in Hemwar.ku_all_V:
                print(
                    str(index) + ".",
                    "The character " + str('" ' + i + ' "') + " is a Vowel.",
                )
            else:
                print(
                    str(index) + ".",
                    "The character " + str('" ' + i + ' "') + " is a Consonant.",
                )
        return "\nFinished.\n"

    def ar_to_la(self, textContent):
        """Under Progress !!!
        Converting Arabic-based Kurdish to Latin-based Kurdish
        'ێ ی': 'êy', # It changes ( U+06CE + U+0020 + U+06CC ) to ( U+00ea + U+0079 ) as a typo in Arabic-based Kurdish
        # 'ئو': 'u', # It changes (ئ = U+0626) + (و = U+0648) to U+0075
        'ئ': '', # It changes U+0626 to NONE
        'ٸ': '', # It changes U+0678 to NONE
        'ا': 'a', # It changes U+0627 to U+0061
        'ب': 'b', # It changes U+0628 to U+0062
        'پ': 'p', # It changes U+067E to U+0070
        'ت': 't', # It changes U+062A to U+0074
        'ج': 'c', # It changes U+062C to U+0063
        'چ': 'ç', # It changes U+0686 to U+00E7
        'ح': 'ĥ', # It changes U+062D to U+0125
        'خ': 'x', # It changes U+062E to U+0078
        'د': 'd', # It changes U+062F to U+0064
        'ر': 'r', # It changes U+0631 to U+0072
        # 'ڕ': 'r\u0302', # It changes U+0695 to ( U+0072 + U+0302 = r̂ )
        'ڕ': 'ŕ', # It changes U+0695 to U+0155 --> Temporarily selected till the formal one will be dedicated.
        'ز': 'z', # It changes U+0632 to U+007A
        'ژ': 'j', # It changes U+0698 to U+006A
        'س': 's', # It changes U+0633 to U+0073
        'ش': 'ş', # It changes U+0634 to U+015F
        'ع': '\'', # It changes U+0639 to U+0027 --> Temporarily selected till the formal one will be dedicated.
        # 'غ': 'x\u0302', # It changes U+063A to ( U+0078 + U+0302 = x̂ )
        'غ': 'ẍ', # It changes U+063A to U+1E8D --> Temporarily selected till the formal one will be dedicated.
        'ف': 'f', # It changes U+0641 to U+0066
        'ڤ': 'v', # It changes U+06A4 to U+0076
        'ق': 'q', # It changes U+0642 to U+0071
        'ک': 'k', # It changes U+06A9 to U+006B
        'ك': 'k', # It changes U+0643 to U+006B
        'ڪ': 'k', # It changes U+06AA to U+006B
        'گ': 'g', # It changes U+06AF to U+0067
        'ل': 'l', # It changes U+0644 to U+006C
        'ڵ': 'ĺ', # It changes U+06B5 to U+013A --> Temporarily selected till the formal one will be dedicated.
        'ڵ': 'ĺ', # It changes U+06B5 to U+004C --> Temporarily selected till the formal one will be dedicated.
        'م': 'm', # It changes U+0645 to U+006D
        'ن': 'n', # It changes U+0646 to U+006E
        'وو': 'û', # It changes (U+0648 + U+0648) to U+00FB
        'و': 'w', # It changes U+0648 to U+0077
        'ۆ': 'o', # It changes U+06C6 to U+006F
        '\u200cه': 'e', # It changes ( U+200C + U+0647 ) to 0065
        'ه\u200c': 'e', # It changes ( U+0647 + U+200C ) to 0065
        'ه': 'h', # It changes U+0647 to U+0068
        'ھ': 'h', # It changes U+06BE to U+0068
        'ە': 'e', # It changes U+06D5 to U+0065
        'یی': 'îy', # It changes ( U+06cc + U+06cc ) to ( U+00ee + U+0079 )
        'ی': 'y', # It changes U+06CC to U+0079
        'ي': 'y', # It changes U+064A to U+0079
        'ى': 'y', # It changes U+0649 to U+0079
        'ێ': 'ê', # It changes U+06CE to U+00EA
        '،': ',', # It changes U+060C to U+002C
        '؛': ';', # It changes U+061B to U+003B
        '‌': '', # removing U+200C to NONE(Zero Width Non-Joiner (ZWNJ)) in Latin text (NOTE: It is not space character (U+0020))
        'ـ': '', # (U+0640) TO BE REMOVED in Latin-based Kurdish
        '؟': '?', # It changes U+061F to U+003F
        '۰': '0', # It changes U+06F0 to U+0030
        '۱': '1', # It changes U+06F1 to U+0031
        '۲': '2', # It changes U+06F2 to U+0032
        '۳': '3', # It changes U+06F3 to U+0033
        '۴': '4', # It changes U+06F4 to U+0034
        '۵': '5', # It changes U+06F5 to U+0035
        '۶': '6', # It changes U+06F6 to U+0036
        '۷': '7', # It changes U+06F7 to U+0037
        '۸': '8', # It changes U+06F8 to U+0038
        '۹': '9', # It changes U+06F9 to U+0039
        '٠': '0', # It changes U+0660 to U+0030
        '١': '1', # It changes U+0661 to U+0031
        '٢': '2', # It changes U+0662 to U+0032
        '٣': '3', # It changes U+0663 to U+0033
        '٤': '4', # It changes U+0664 to U+0034
        '٥': '5', # It changes U+0665 to U+0035
        '٦': '6', # It changes U+0666 to U+0036
        '٧': '7', # It changes U+0667 to U+0037
        '٨': '8', # It changes U+0668 to U+0038
        '٩': '9', # It changes U+0669 to U+0039
        '(': '(', # It changes U+0028 to U+0028
        ')': ')', # It changes U+0029 to U+0029
        '[': '[', # It changes U+005B to U+005B
        ']': ']', # It changes U+005D to U+005D
        '{': '{', # It changes U+007B to U+007B
        '}': '}' # It changes U+007D to U+007D
        """
        self.textContent = textContent
        mapping = {
            # "ێ ی": "êy",  # It changes ( U+06CE + U+0020 + U+06CC ) to ( U+00ea + U+0079 ) as a typo in Arabic-based Kurdish
            #'ئە': 'e',
            # 'ئو': 'u', # It changes (ئ = U+0626) + (و = U+0648) to U+0075
            # "ئ": "",  # It changes U+0626 to NONE
            # "ٸ": "",  # It changes U+0678 to NONE
            "ا": "a",  # It changes U+0627 to U+0061
            "ب": "b",  # It changes U+0628 to U+0062
            "پ": "p",  # It changes U+067E to U+0070
            "ت": "t",  # It changes U+062A to U+0074
            "ج": "c",  # It changes U+062C to U+0063
            "چ": "ç",  # It changes U+0686 to U+00E7
            "ح": "ĥ",  # It changes U+062D to U+0125
            "خ": "x",  # It changes U+062E to U+0078
            "د": "d",  # It changes U+062F to U+0064
            "ر": "r",  # It changes U+0631 to U+0072
            # 'ڕ': 'r\u0302', # It changes U+0695 to ( U+0072 + U+0302 = r̂ )
            "ڕ": "ŕ",  # It changes U+0695 to U+0155 --> Temporarily selected till the formal one will be dedicated.
            "ز": "z",  # It changes U+0632 to U+007A
            "ژ": "j",  # It changes U+0698 to U+006A
            "س": "s",  # It changes U+0633 to U+0073
            "ش": "ş",  # It changes U+0634 to U+015F
            # "ع": "'",  # It changes U+0639 to U+0027 --> Temporarily selected till the formal one will be dedicated.
            # 'غ': 'x\u0302', # It changes U+063A to ( U+0078 + U+0302 = x̂ )
            "غ": "ẍ",  # It changes U+063A to U+1E8D --> Temporarily selected till the formal one will be dedicated.
            "ف": "f",  # It changes U+0641 to U+0066
            "ڤ": "v",  # It changes U+06A4 to U+0076
            "ق": "q",  # It changes U+0642 to U+0071
            "ک": "k",  # It changes U+06A9 to U+006B
            "ك": "k",  # It changes U+0643 to U+006B
            "ڪ": "k",  # It changes U+06AA to U+006B
            "گ": "g",  # It changes U+06AF to U+0067
            "ل": "l",  # It changes U+0644 to U+006C
            # 'ڵ': 'l\u0302', # It changes U+06B5 to ( U+006C + U+0302 = l̂ )
            "ڵ": "ĺ",  # It changes U+06B5 to U+013A --> Temporarily selected till the formal one will be dedicated.
            "م": "m",  # It changes U+0645 to U+006D
            "ن": "n",  # It changes U+0646 to U+006E
            # "وو": "û",  # It changes (U+0648 + U+0648) to U+00FB
            # "و": "w",  # It changes U+0648 to U+0077
            "ۆ": "o",  # It changes U+06C6 to U+006F
            "\u200cه": "e",  # It changes ( U+200C + U+0647 ) to 0065
            "ه\u200c": "e",  # It changes ( U+0647 + U+200C ) to 0065
            "ه": "h",  # It changes U+0647 to U+0068
            "ھ": "h",  # It changes U+06BE to U+0068
            "ە": "e",  # It changes U+06D5 to U+0065
            "یی": "îy",  # It changes ( U+06cc + U+06cc ) to ( U+00ee + U+0079 )
            # "ی": "y",  # It changes U+06CC to U+0079
            # "ي": "y",  # It changes U+064A to U+0079
            # "ى": "y",  # It changes U+0649 to U+0079
            "ێ": "ê",  # It changes U+06CE to U+00EA
            "،": ",",  # It changes U+060C to U+002C
            "؛": ";",  # It changes U+061B to U+003B
            "‌": "",  # removing U+200C to NONE(Zero Width Non-Joiner (ZWNJ)) in Latin text (NOTE: It is not space character (U+0020))
            "ـ": "",  # (U+0640) TO BE REMOVED in Latin-based Kurdish
            "؟": "?",  # It changes U+061F to U+003F
            "۰": "0",  # It changes U+06F0 to U+0030
            "۱": "1",  # It changes U+06F1 to U+0031
            "۲": "2",  # It changes U+06F2 to U+0032
            "۳": "3",  # It changes U+06F3 to U+0033
            "۴": "4",  # It changes U+06F4 to U+0034
            "۵": "5",  # It changes U+06F5 to U+0035
            "۶": "6",  # It changes U+06F6 to U+0036
            "۷": "7",  # It changes U+06F7 to U+0037
            "۸": "8",  # It changes U+06F8 to U+0038
            "۹": "9",  # It changes U+06F9 to U+0039
            "٠": "0",  # It changes U+0660 to U+0030
            "١": "1",  # It changes U+0661 to U+0031
            "٢": "2",  # It changes U+0662 to U+0032
            "٣": "3",  # It changes U+0663 to U+0033
            "٤": "4",  # It changes U+0664 to U+0034
            "٥": "5",  # It changes U+0665 to U+0035
            "٦": "6",  # It changes U+0666 to U+0036
            "٧": "7",  # It changes U+0667 to U+0037
            "٨": "8",  # It changes U+0668 to U+0038
            "٩": "9",  # It changes U+0669 to U+0039
            "(": "(",  # It changes U+0028 to U+0028
            ")": ")",  # It changes U+0029 to U+0029
            "[": "[",  # It changes U+005B to U+005B
            "]": "]",  # It changes U+005D to U+005D
            "{": "{",  # It changes U+007B to U+007B
            "}": "}",  # It changes U+007D to U+007D
        }
        return Hemwar().replace_func(mapping, textContent)

    def capitalize(self, word):
        """
        Capitalizing each word at the starting place.
        This function will be used also to capitalizing the names
        in Latin-based Kurdish language which is in the plan of the To-Dos.
        """
        self.word = word
        return re.sub(
            r"(\n|^|^\s|^\n|\.\s|\.|\?|\?\s)(\S)",
            lambda x: x.group(1) + x.group(2).upper(),
            word,
        )

    # def missing_chars(self, textContent):

    #     """Under Progress !!!,
    #     Converting temporary characters which are not specified in Latin-based Kurdish ([r\u0302, x\u0302, l\u0302]) """
    #     self.textContent = textContent
    #     mapping = {
    #             # 'ڕ': 'r\u0302', # It changes U+0695 to ( U+0072 + U+0302 = r̂ )
    #             'ŕ': 'r\u0302', # It changes U+0155 to ( U+0072 + U+0302 = r̂ )
    #             # 'ع': '\'', # It changes U+0639 to U+0027 --> Temporarily selected till the formal one will be dedicated.
    #             # 'غ': 'x\u0302', # It changes U+063A to ( U+0078 + U+0302 = x̂ )
    #             'ẍ': 'x\u0302', # It changes U+1E8D to ( U+0078 + U+0302 = x̂ )
    #             # 'ڵ': 'l\u0302', # It changes U+06B5 to ( U+006C + U+0302 = l̂ )
    #             'ĺ': 'l\u0302', # It changes U+013A to ( U+006C + U+0302 = l̂ )
    #             }
    #     return Hemwar().replace_func(mapping, textContent)

    def transliterate(self, word):
        """Transliteration from Arabic-based Kurdish to Latin-based Kurdish"""
        self.word = word
        conv = Hemwar().ar_to_la(word)
        all_rules = (
            vowelIssues.Vowel().vowel_rules,
            bizrokeRules.Bizroke().bizroke,
            Hemwar().capitalize,
            punctuation.Punctuation().puncsIssues,
        )
        for rules in all_rules:
            conv = rules(conv)
        return conv
