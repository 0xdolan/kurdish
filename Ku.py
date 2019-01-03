import re 
import unicodedata

class Hemwar:
	"""
	Kurdish Language Library for converting characters and digits in Persian, English and Arabic to Kurdish and vice versa.
	Copyright (C) 2018
	Dolan Hêriş (dolanskurd@mail.com)
	Kurdish Language Library is available under the MIT license. 
	https://github.com/dolanskurd/Kurdish
	"""
	KuAlphabet_Ar = 'ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنهەوۆوویێ'
	KuAlphabet_Ar_C = 'ئبپتجچحخدرڕزژسشعغفڤقکگلڵمنه'
	KuAlphabet_Ar_V = 'اەوۆوویێ'
	KuAlphabet_Ar_Digit = '٠١٢٣٤٥٦٧٨٩'
	KuAlphabet_La = 'ABCÇDEÊFGHIÎJKLMNOPQRSŞTUÛVWXYZabcçdeêfghiîjklmnopqrsştuûvwxyz'
	KuAlphabet_La_C = 'BCÇDFGHJKLMNPQRSŞTVWXYZbcçdfghjklmnpqrsştvwxyz'
	KuAlphabet_La_V = 'AEÊIÎOUÛaeêiîouû'
	KuAlphabet_La_Digit = '0123456789'
	KuAll_V = 'AEÊIÎOUÛaeêiîouûاەوۆوویێ'
	Persian_Digit = '۰۱۲۳۴۵۶۷۸۹'
	Ar_Special_chars = 'صضطظذيةثؤأإآكۀى'


	def multiReplace(self, adjustingRule, content):
		"""Replacing code"""
		self.adjustingRule = adjustingRule
		self.content = content

		pattern = '|'.join(map(re.escape, adjustingRule.keys()))
		return re.sub(pattern, lambda u: adjustingRule[u.group()], str(content))

	def En_Digit_to_Ku(self, userText):
		"""Converting English digits to Kurdish digits"""
		self.userText = userText

		adjustingRule = {
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
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def Ku_Digit_to_En(self, userText):
		"""Converting Kurdish digits to English digits"""
		self.userText = userText
		adjustingRule = {
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
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def Fa_Digit_to_Ku(self, userText):
		"""Converting the Persian (Farsi) digits to the Kurdish digits
		It is also converting the Persian (Farsi) digits to the Arabic digits as the Kurdish and the Arabic digits are the same.
		"""
		self.userText = userText
		adjustingRule = {
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
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def Ku_Digit_to_Fa(self, userText):
		"""Converting the Kurdish digits to the Persian (Farsi) digits
		It is also converting the Arabic digits to the Persian (Farsi) digits as the Kurdish and the Arabic digits are the same.
		"""
		self.userText = userText
		adjustingRule = {
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
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def En_Digit_to_Fa(self, userText):
		"""Converting English digits to Persian (Farsi) digits"""
		self.userText = userText

		adjustingRule = {
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
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def Fa_Digit_to_En(self, userText):
		"""Converting Persian (Farsi) digits to English digits"""
		self.userText = userText
		adjustingRule = {
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
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def En_Char_to_Ku(self, userText):
		"""Converting the English characters to the Kurdish characters, based on KurdITGroup Keyboard (https://www.kurditgroup.org/)
		there is some minor changes which is described across each of them.
		"""
		self.userText = userText
		adjustingRule = {
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
			',': '،' # It changes U+002C to U+060C
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def Ku_Char_to_En(self, userText):
		"""Converting Kurdish characters to English characters, , based on KurdITGroup Keyboard (https://www.kurditgroup.org/)"""
		self.userText = userText
		adjustingRule = {
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
			'ه': 'h', # It changes U+0647  (NOT U+06BE 'ھ') to U+0068
			'ە': 'e', # It changes U+06D5 to U+0065
			'ی': 'y', # It changes U+06CC to U+0079
			'ێ': 'Y', # It changes U+06CE to U+0059
			'،': ',' # It changes U+060C to U+002C
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def Ar_Char_to_Ku(self, userText):
		"""Converting Arabic characters to Kurdish characters
		It is also Converting Arabic characters to Persian (Farsi) characters as Ku and Fa versions are the same
		"""
		self.userText = userText
		adjustingRule = {
			'ك': 'ک', # It changes U+0643 to U+06A9
			'ڪ': 'ک', # It changes U+06AA to U+06A9
			'ي': 'ی', # It changes U+064A to U+06CC
			'ى': 'ی', # It changes U+0649 to U+06CC
			'ے': 'ی', # It changes U+06D2 to U+06CC
			'ة': 'ە', # It changes U+0629 to U+06D5
			'ۂ': 'ە', # It changes U+06C2 to U+06D5
			'ۀ': 'ە', # It changes U+06C0 to U+06D5
			'‌ه': 'ە', # It changes U+0647 + U+200C to U+06D5
			'‌ە': 'ە', # It changes U+06D5 + U+200C to U+06D5
			'ؤ': 'و', # It changes U+0624 to U+0648
			'ٶ': 'و', # It changes U+0676 to U+0648
			'ۊ': 'و', # It changes U+06CA to U+0648
			'أ': 'ا', # It changes U+0623 to U+0627
			'ﺃ': 'ا', # It changes U+FE83 to U+0627
			'إ': 'ا', # It changes U+0625 to U+0627
			'ﺇ': 'ا' # It changes U+FE87 to U+0627
			
		}
		return Hemwar().multiReplace(adjustingRule, userText)

	def getUniNum(self, x):
		"""Get the Unicode details of the character or digit"""
		self.x = x

		for i, char in enumerate(x, start = 1):
			print(str(i)+'.', char, '= U+%04x' % ord(char), unicodedata.name(char))
		return "\nConversion has been completed successfully.\n"
			
	def V_or_C(self, x):
		"""Checking the Kurdish letters if it is vowel and consonant"""
		self.x = x

		for index, i in enumerate(x, start = 1):
			if i.isdigit():
				print(str(index) + ".", str("\" " + i + " \""), "is a digit not character.")
			elif not i.isalpha() and  i == " ":
				print(str(index) + "." + str("\"" + i + "\"") + ", Select a valuable character. Spaces are not valid also!")
			elif i == "و" or i == "ی":
				print(str(index) + ".", "If the word started with " + str("\" " + i + " \"") + " so it is Consonant otherwise it is Vowel.")
			elif i in Hemwar.KuAll_V:
				print(str(index) + ".","The letter " + str("\" " + i + " \"") + " is a Vowel.")
			else:
				print(str(index) + ".","The letter " + str("\" " + i + " \"") + " is a Consonant.")
		return "\nFinished.\n"

