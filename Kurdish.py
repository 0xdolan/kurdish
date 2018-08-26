# encoding='utf-8'

"""
Kurdish Language Library for converting characters and digits in Persian, English and Arabic to Kurdish and vice versa.
Copyright (C) 2018
Dolan Hêriş (dolanskurd@mail.com)
Kurdish Language Library is available under the MIT license. 
https://github.com/dolanskurd/Kurdish

"""

import re

'''
Replacing code
'''
def multiReplace(adjustingRule, content):
	pattern = '|'.join(map(re.escape, adjustingRule.keys()))
	return re.sub(pattern, lambda u: adjustingRule[u.group()], str(content))

'''
Converting English digits to Kurdish digits
'''
def convert_En_Dig_to_Ku(userText):
    adjustingRule = {
        '0': '٠', # It changes \u0030 to \u0660
        '1': '١', # It changes \u0031 to \u0661
        '2': '٢', # It changes \u0032 to \u0662
        '3': '٣', # It changes \u0033 to \u0663
        '4': '٤', # It changes \u0034 to \u0664
        '5': '٥', # It changes \u0035 to \u0665
        '6': '٦', # It changes \u0036 to \u0666
        '7': '٧', # It changes \u0037 to \u0667
        '8': '٨', # It changes \u0038 to \u0668
        '9': '٩', # It changes \u0039 to \u0669
        '.': '.', # It changes \u002E to \u002E
    }
    return multiReplace(adjustingRule, userText)

'''
Converting Kurdish digits to English digits
'''
def convert_Ku_Dig_to_En(userText):
    adjustingRule = {
    	'٠': '0', # It changes \u0660 to \u0030
    	'١': '1', # It changes \u0661 to \u0031
    	'٢': '2', # It changes \u0662 to \u0032
    	'٣': '3', # It changes \u0663 to \u0033
    	'٤': '4', # It changes \u0664 to \u0034
    	'٥': '5', # It changes \u0665 to \u0035
    	'٦': '6', # It changes \u0666 to \u0036
    	'٧': '7', # It changes \u0667 to \u0037
    	'٨': '8', # It changes \u0668 to \u0038
    	'٩': '9', # It changes \u0669 to \u0039
    	'.': '.', # It changes \u002E to \u002E
    }
    return multiReplace(adjustingRule, userText)

'''
Converting English characters to Kurdish
(Based on KRG Unicode System (http://unicode.ekrg.org/ku_unicodes.html))
'''
def convert_En_Char_to_Ku(userText):
	adjustingRule = {
		'u': 'ئ', # It changes \u0075 to \u0626
		'a': 'ا', # It changes \u0061 to \u0627
		'b': 'ب', # It changes \u0062 to \u0628
		'p': 'پ', # It changes \u0070 to \u067E
		't': 'ت', # It changes \u0074 to \u062A
		'c': 'ج', # It changes \u0063 to \u062C
		'C': 'چ', # It changes \u0043 to \0686
		'I': 'ح', # It changes \u0049 to \062D
		'x': 'خ', # It changes \u0078 to \062E
		'd': 'د', # It changes \u0064 to \u062F
		'r': 'ر', # It changes \u0072 to \u0631
		'R': 'ڕ', # It changes \u0052 to \u0695
		'z': 'ز', # It changes \u007A to \u0632
		'j': 'ژ', # It changes \u006A to \u0698
		's': 'س', # It changes \u0073 to \u0633
		'S': 'ش', # It changes \u0053 to \u0634
		'i': 'ع', # It changes \u0069 to \u0639
		'G': 'غ', # It changes \u0047 to \u063A
		'f': 'ف', # It changes \u0066 to \u0641
		'v': 'ڤ', # It changes \u0076 to \u06A4
		'q': 'ق', # It changes \u0071 to \u0642
		'k': 'ک', # It changes \u006B to \u06A9
		'g': 'گ', # It changes \u0067 to \u06AF
		'l': 'ل', # It changes \u006C to \u0644
		'L': 'ڵ', # It changes \u004C to \u06B5
		'm': 'م', # It changes \u006D to \u0645
		'n': 'ن', # It changes \u006E to \u0646
		'w': 'و', # It changes \u006F to \u0648
		'o': 'ۆ', # It changes \u006F to \u06C6
		'h': 'ه', # It changes \u0068 to \u0647
		'e': 'ە', # It changes \u0065 to \u06D5
		'y': 'ی', # It changes \u0079 to \06CC
		'Y': 'ێ', # It changes \u0059 to \u06CE
		',': '،' # It changes \u002C to \u060C
		}
	return multiReplace(adjustingRule, userText)

'''
Converting Kurdish characters to English
'''
def convert_Ku_Char_to_En(userText):
	adjustingRule = {
		'ئ': 'u', # It changes \u0626 to \u0075
		'ا': 'a', # It changes \u0627 to \u0061
		'ب': 'b', # It changes \u0628 to \u0062
		'پ': 'p', # It changes \u067E to \u0070
		'ت': 't', # It changes \u062A to \u0074
		'ج': 'c', # It changes \u062C to \u0063
		'چ': 'C', # It changes \0686 to \u0043
		'ح': 'I', # It changes \062D to \u0049
		'خ': 'x', # It changes \062E to \u0078
		'د': 'd', # It changes \u062F to \u0064
		'ر': 'r', # It changes \u0631 to \u0072
		'ڕ': 'R', # It changes \u0695 to \u0052
		'ز': 'z', # It changes \u0632 to \u007A
		'ژ': 'j', # It changes \u0698 to \u006A
		'س': 's', # It changes \u0633 to \u0073
		'ش': 'S', # It changes \u0634 to \u0053
		'ع': 'i', # It changes \u0639 to \u0069
		'غ': 'G', # It changes \u063A to \u0047
		'ف': 'f', # It changes \u0641 to \u0066
		'ڤ': 'v', # It changes \u06A4 to \u0076
		'ق': 'q', # It changes \u0642 to \u0071
		'ک': 'k', # It changes \u06A9 to \u006B
		'گ': 'g', # It changes \u06AF to \u0067
		'ل': 'l', # It changes \u0644 to \u006C
		'ڵ': 'L', # It changes \u06B5 to \u004C
		'م': 'm', # It changes \u0645 to \u006D
		'ن': 'n', # It changes \u0646 to \u006E
		'و': 'w', # It changes \u0648 to \u006F
		'ۆ': 'o', # It changes \u06C6 to \u006F
		'ه': 'h', # It changes \u0647 to \u0068
		'ە': 'e', # It changes \u06D5 to \u0065
		'ی': 'y', # It changes \06CC to \u0079
		'ێ': 'Y', # It changes \u06CE to \u0059
		'،': ',' # It changes \u060C to \u002C
		}
	return multiReplace(adjustingRule, userText)

'''
Converting Persian (Farsi) digits to Kurdish digits
'''
def convert_Fa_Dig_to_Ku(userText):
    adjustingRule = {
        '٠': '٠', # It changes \u06F0 to \u0660
        '١': '١', # It changes \u06F1 to \u0661
        '٢': '٢', # It changes \u06F2 to \u0662
        '٣': '٣', # It changes \u06F3 to \u0663
        '۴': '٤', # It changes \u06F4 to \u0664
        '۵': '٥', # It changes \u06F5 to \u0665
        '۶': '٦', # It changes \u06F6 to \u0666
        '٧': '٧', # It changes \u06F7 to \u0667
        '٨': '٨', # It changes \u06F8 to \u0668
        '٩': '٩', # It changes \u06F9 to \u0669
        '.': '.', # It changes \u002E to \u002E
    }
    return multiReplace(adjustingRule, userText)

'''
Converting Kurdish digits to Persian (Farsi) digits
'''
def convert_Ku_Dig_to_Fa(userText):
    adjustingRule = {
        '٠': '٠', # It changes \u0660 to \u06F0
        '١': '١', # It changes \u0661 to \u06F1
        '٢': '٢', # It changes \u0662 to \u06F2
        '٣': '٣', # It changes \u0663 to \u06F3
        '٤': '۴', # It changes \u0664 to \u06F4
        '٥': '۵', # It changes \u0665 to \u06F5
        '٦': '۶', # It changes \u0666 to \u06F6
        '٧': '٧', # It changes \u0667 to \u06F7
        '٨': '٨', # It changes \u0668 to \u06F8
        '٩': '٩', # It changes \u0669 to \u06F9
        '.': '.', # It changes \u002E to \u002E
    }
    return multiReplace(adjustingRule, userText)
	
'''
Converting Arabic characters to Kurdish
(Based on KRG Unicode System (http://unicode.ekrg.org/ku_unicodes.html))
'''
def convert_Ar_Char_to_Ku(userText):
    adjustingRule = {
        'ك': 'ک', # It changes \u0643 to \u06A9
		'ڪ': 'ک', # It changes \u06AA to \u06A9
        'ي': 'ی', # It changes \064A to \u06CC
		'ى': 'ی', # It changes \u0649 to \u06CC
        'ے': 'ی', # It changes \u06D2 to \u06CC
        'ة': 'ە', # It changes \u0629 to \u06D5
		'ۂ': 'ە', # It changes \u06C2 to \u06D5
        'ۀ': 'ە', # It changes \u06C0 to \u06D5
        'ؤ': 'و', # It changes \u0624 to \u0648
    }
    return multiReplace(adjustingRule, userText)

		