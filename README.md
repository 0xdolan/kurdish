# Kurdish 

Welcome to **Kurdish Language Library** - a ***Python*** Library for converting characters and digits in Persian, English and Arabic to Kurdish and vice versa.

## Installation

How to install the module:

`
pip install Kurdish
`

* [How to install Python modules](https://docs.python.org/3/installing/index.html "How to install Python modules")

------------

## How to use

### Converting Characters and Digits


* #### Converting English Characters to Kurdish Based on KRG Unicode System (http://unicode.ekrg.org/ku_unicodes.html):
  The major difference with KRG System is ( ھ = U+06BE ARABIC LETTER HEH DOACHASHMEE ) letter which normally in Arabic-based writing system ( ه = U+0647 ARABIC LETTER HEH ) alternatively has been used. For making the exact shape, you can use ( ه = U+0647 ARABIC LETTER HEH ) + ( ـ = U+0640 ARABIC TATWEEL ). The result will be ( هـ ).
```python
import ku
print('Convert English characters to Kurdish:')
print(ku.Hemwar().En_Char_to_Ku('bexSyn le gwnah w heLe CawpoSyne! \n to Con heReSet be uagry pRtyne? \n bmbexSy be nwYjanewe, kesman le kese \n be gwnahewe bmbexSe, delYm bexSyne'))
```


* #### Converting Arabic Characters to Kurdish:
```python
import ku
print('Convert Arabic characters to Kurdish:')
print(ku.Hemwar().Ar_Char_to_Ku('“يقول نيتشه: "الدين ثورة العبيد". ويقول ماركس: "الدين أفيون الشعوب". وفي الحقيقة إنّ الدين ثورة وأفيون في آن واحد. فهو عند المترفين أفيون وعند الأنبياء ثورة. وكل دين يبدأ على يد النبي ثورة ثم يستحوذ المترفون عليه بعد ذلك فيحولونه إلى أفيون. وعندئذ يظهر نبي جديد فيعيدها شعواء مرة أخرى.”― علي الوردي, مهزلة العقل البشري '))
```


* #### Converting Kurdish Characters to English:
```python
import ku
print('Convert Kurdish characters to English:')
print(ku.Hemwar().Ku_Char_to_En('\n بەخشین لە گوناه و هەڵە چاوپۆشینە! \nتۆ چۆن هەڕەشەت بە ئاگری پڕتینە?\n بمبەخشی بە نوێژانەوە, کەسمان لە کەسە\n بە گوناهەوە بمبەخشە, دەلێم بەخشینە'))
```
* #### Getting Unicode code of any character or digit:
```python
import ku
print('Getting Unicode code for instance: all Arabic specific characters\n')
print(ku.Hemwar().getUniNum(ku.Hemwar.Ar_Special_chars))
```

* #### Getting all Arabic-based of Kurdish Alphabet in a list:
```python
import ku
print('Arabic-based of Kurdish Alphabet:\n')
print(list(ku.Hemwar().KuAlphabet_Ar))
```

* #### Getting all Latin-based of Kurdish Alphabet in a list:
```python
import ku
print('Latin-based of Kurdish Alphabet:\n')
print(list(ku.Hemwar().KuAlphabet_La))
```

* #### Getting all Latin-based and Arabic-based Kurdish vowels in a list:
```python
import ku
print('All Latin-based and Arabic-based Kurdish vowels:\n')
print(list(ku.Hemwar().KuAll_V))
```

* #### Converting Persian (Farsi) Digits to Kurdish:
```python
import ku
print('Convert Persian digits to Kurdish:')
print(ku.Hemwar().Fa_Digit_to_Ku('٠١٢٣۴۵۶٧٨٩'))
```

* #### Converting Kurdish Digits to Persian (Farsi):
```python
import ku
print('Convert Kurdish digits to Persian:')
print(ku.Hemwar().Ku_Digit_to_Fa('٠١٢٣٤٥٦٧٨٩'))
```

* #### Converting English Digits to Kurdish:
```python
import ku
print('Convert English digits to Kurdish:')
print(ku.Hemwar().En_Digit_to_Ku('0123456789'))
```

* #### Converting Kurdish Digits to English:
```python
import ku
print('Convert Kurdish digits to English:')
print(ku.Hemwar().Ku_Digit_to_En('٠١٢٣٤٥٦٧٨٩'))
```

## Arabic-based Kurdish Unicode Characters

Character | Unicode Code
--------- | ------------
ئ         | U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE
ا         | U+0627 ARABIC LETTER ALEF
ب         | U+0628 ARABIC LETTER BEH
پ         | U+067e ARABIC LETTER PEH
ت         | U+062a ARABIC LETTER TEH
ج         | U+062c ARABIC LETTER JEEM
چ         | U+0686 ARABIC LETTER TCHEH
ح         | U+062d ARABIC LETTER HAH
خ         | U+062e ARABIC LETTER KHAH
د         | U+062f ARABIC LETTER DAL
ر         | U+0631 ARABIC LETTER REH
ڕ         | U+0695 ARABIC LETTER REH WITH SMALL V BELOW
ز         | U+0632 ARABIC LETTER ZAIN
ژ         | U+0698 ARABIC LETTER JEH
س         | U+0633 ARABIC LETTER SEEN
ش         | U+0634 ARABIC LETTER SHEEN
ع         | U+0639 ARABIC LETTER AIN
غ         | U+063a ARABIC LETTER GHAIN
ف         | U+0641 ARABIC LETTER FEH
ڤ         | U+06a4 ARABIC LETTER VEH
ق         | U+0642 ARABIC LETTER QAF
ک         | U+06a9 ARABIC LETTER KEHEH
گ         | U+06af ARABIC LETTER GAF
ل         | U+0644 ARABIC LETTER LAM
ڵ         | U+06b5 ARABIC LETTER LAM WITH SMALL V
م         | U+0645 ARABIC LETTER MEEM
ن         | U+0646 ARABIC LETTER NOON
ه         | U+0647 ARABIC LETTER HEH
ە         | U+06d5 ARABIC LETTER AE
و         | U+0648 ARABIC LETTER WAW
ۆ         | U+06c6 ARABIC LETTER OE
وو         | U+0648 ARABIC LETTER WAW (X2) Vowel version of the letter is not defined yet. The same shape but different unicode code should be dedicated. This should be count as ONE individual character.
ی         | U+06cc ARABIC LETTER FARSI YEH
ێ         | U+06ce ARABIC LETTER YEH WITH SMALL V
و         | Consonant version of the letter is not defined yet. The same shape but different unicode code should be dedicated.
ی         | Consonant version of the letter is not defined yet. The same shape but different unicode code should be dedicated.
بزرۆکە   | Bizroke, Which won't be written in the Arabic-based writing System.
    
## Arabic-based Kurdish Unicode Digits

Digit | Unicode Code
----- | ------------
٠     | U+0660 ARABIC-INDIC DIGIT ZERO
١     | U+0661 ARABIC-INDIC DIGIT ONE
٢     | U+0662 ARABIC-INDIC DIGIT TWO
٣     | U+0663 ARABIC-INDIC DIGIT THREE
٤     | U+0664 ARABIC-INDIC DIGIT FOUR
٥     | U+0665 ARABIC-INDIC DIGIT FIVE
٦     | U+0666 ARABIC-INDIC DIGIT SIX
٧     | U+0667 ARABIC-INDIC DIGIT SEVEN
٨     | U+0668 ARABIC-INDIC DIGIT EIGHT
٩     | U+0669 ARABIC-INDIC DIGIT NINE


## Latin-based Kurdish Unicode Characters

Character | Unicode Code
--------- | ------------
A         | U+0041 LATIN CAPITAL LETTER A
B         | U+0042 LATIN CAPITAL LETTER B
C         | U+0043 LATIN CAPITAL LETTER C
Ç         | U+00c7 LATIN CAPITAL LETTER C WITH CEDILLA
D         | U+0044 LATIN CAPITAL LETTER D
E         | U+0045 LATIN CAPITAL LETTER E
Ê         | U+00ca LATIN CAPITAL LETTER E WITH CIRCUMFLEX
F         | U+0046 LATIN CAPITAL LETTER F
G         | U+0047 LATIN CAPITAL LETTER G
H         | U+0048 LATIN CAPITAL LETTER H
I         | U+0049 LATIN CAPITAL LETTER I
Î         | U+00ce LATIN CAPITAL LETTER I WITH CIRCUMFLEX
J         | U+004a LATIN CAPITAL LETTER J
K         | U+004b LATIN CAPITAL LETTER K
L         | U+004c LATIN CAPITAL LETTER L
M         | U+004d LATIN CAPITAL LETTER M
N         | U+004e LATIN CAPITAL LETTER N
O         | U+004f LATIN CAPITAL LETTER O
P         | U+0050 LATIN CAPITAL LETTER P
Q         | U+0051 LATIN CAPITAL LETTER Q
R         | U+0052 LATIN CAPITAL LETTER R
S         | U+0053 LATIN CAPITAL LETTER S
Ş         | U+015e LATIN CAPITAL LETTER S WITH CEDILLA
T         | U+0054 LATIN CAPITAL LETTER T
U         | U+0055 LATIN CAPITAL LETTER U
Û         | U+00db LATIN CAPITAL LETTER U WITH CIRCUMFLEX
V         | U+0056 LATIN CAPITAL LETTER V
W         | U+0057 LATIN CAPITAL LETTER W
X         | U+0058 LATIN CAPITAL LETTER X
Y         | U+0059 LATIN CAPITAL LETTER Y
Z         | U+005a LATIN CAPITAL LETTER Z
Ĥ         | U+0124 LATIN CAPITAL LETTER H WITH CIRCUMFLEX. This letter should be defined as an equivalent for ( ح = U+062d ARABIC LETTER HAH ). No unique letter is defined yet.
RR         | R̂ (R + ̂  = [U+0052 LATIN CAPITAL LETTER R + U+0302 COMBINING CIRCUMFLEX ACCENT] ). No unique letter is defined yet. The shape should be like ( R̂ ) but there is no defined unicode code.
LL         | L̂ (L + ̂  = [U+004c LATIN CAPITAL LETTER L + U+0302 COMBINING CIRCUMFLEX ACCENT] ). No unique letter is defined yet. The shape should be like ( L̂ ) but there is no defined unicode code.
XX         | X̂ (X + ̂  = [U+0058 LATIN CAPITAL LETTER X + U+0302 COMBINING CIRCUMFLEX ACCENT] ) . No unique letter is defined yet. The shape should be like ( X̂ ) but there is no defined unicode code.
ع         | No letter is defined yet. No shape and no unicode code.
ئ         | No letter is defined yet. No shape and no unicode code.

## Latin-based Kurdish Unicode Digits (Same as English)

Digit | Unicode Code
----- | ------------
0     | U+0030 DIGIT ZERO
1     | U+0031 DIGIT ONE
2     | U+0032 DIGIT TWO
3     | U+0033 DIGIT THREE
4     | U+0034 DIGIT FOUR
5     | U+0035 DIGIT FIVE
6     | U+0036 DIGIT SIX
7     | U+0037 DIGIT SEVEN
8     | U+0038 DIGIT EIGHT
9     | U+0039 DIGIT NINE

## Arabic-based Persian Unicode Digits
Arabic-based Persian Unicode Digits (Completely different unicode codes with Arabic-based Kurdish but some of them only in shape are the same as Arabic-based Persian. (۴۵۶) are different, the others (٠١٢٣٧٨٩) are the same).

Digit | Unicode Code
----- | ------------
۰     | U+06f0 EXTENDED ARABIC-INDIC DIGIT ZERO
۱     | U+06f1 EXTENDED ARABIC-INDIC DIGIT ONE
۲     | U+06f2 EXTENDED ARABIC-INDIC DIGIT TWO
۳     | U+06f3 EXTENDED ARABIC-INDIC DIGIT THREE
۴     | U+06f4 EXTENDED ARABIC-INDIC DIGIT FOUR
۵     | U+06f5 EXTENDED ARABIC-INDIC DIGIT FIVE
۶     | U+06f6 EXTENDED ARABIC-INDIC DIGIT SIX
۷     | U+06f7 EXTENDED ARABIC-INDIC DIGIT SEVEN
۸     | U+06f8 EXTENDED ARABIC-INDIC DIGIT EIGHT
۹     | U+06f9 EXTENDED ARABIC-INDIC DIGIT NINE

## Extra Arabic Characters
Extra Arabic characters which are NOT used in Kurdish but will be used in Persian.

Character | Unicode Code
--------- | ------------
ص         | U+0635 ARABIC LETTER SAD
ض         | U+0636 ARABIC LETTER DAD
ط         | U+0637 ARABIC LETTER TAH
ظ         | U+0638 ARABIC LETTER ZAH
ذ         | U+0630 ARABIC LETTER THAL
ي         | U+064a ARABIC LETTER YEH
ة         | U+0629 ARABIC LETTER TEH MARBUTA
ث         | U+062b ARABIC LETTER THEH
ؤ         | U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE
أ         | U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE
إ         | U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW
آ         | U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE
ك         | U+0643 ARABIC LETTER KAF
ۀ         | U+06c0 ARABIC LETTER HEH WITH YEH ABOVE
ى         | U+0649 ARABIC LETTER ALEF MAKSURA

## Contact Me

I hope you like this library. Feel free to reach out if you have questions or if you want to contribute in any way:

* **[GitHub](https://github.com/dolanskurd)**
* **[PyPI](https://pypi.org/project/Kurdish/)**
* **[Twitter](http://www.twitter.com/dolanskurd)**
* **E-mail: [dolanskurd@mail.com](mailto:dolanskurd@mail.com)**

## Donate

If you think it deserves, **Buy Me A Coffee**:
* **[IDPay (آیدی پی)](https://idpay.ir/dolanskurd)**
* **[iTunes Gift Cards via PayPal (Email-Delivery)](https://www.paypal.com/us/gifts/brands/itunes)** to my Apple ID: **dolanskurd@gmail.com**

## License

Kurdish Language Library is available under the **MIT license**.
