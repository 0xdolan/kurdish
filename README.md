# Kurdish

![Kurdish Language Library](https://user-images.githubusercontent.com/18519747/79156936-68a2d380-7ddc-11ea-8e1d-ad9f8ce2ed02.png)

Welcome to **Kurdish Language Library** - a **_Python_** library for transliteration from Arabic-based Kurdish to Latin one. It can also be used for converting characters and digits in Persian, English and Arabic to Kurdish and vice versa, and now
an easy GUI Application is ready to use for daily tasks for either 
[Windows](https://github.com/Azhy-Slemany/kurdish/releases/download/1.0.0/KurdishCharacterConvertor-Windows.zip) or 
[Mac](https://github.com/Azhy-Slemany/kurdish/releases/download/1.0.0/KurdishCharacterConvertor-Mac.zip) or 
[Others](https://github.com/Azhy-Slemany/kurdish/tree/master/GUI).

## NEW FEATURES
- **GUI** has been added for `Kurdish` :-)

## Installation

- GUI Application Installation

  Read the introduction [here](https://github.com/Azhy-Slemany/kurdish/tree/master/GUI) and then install the GUI application 
  for **Windows** [here](https://github.com/Azhy-Slemany/kurdish/releases/download/1.0.0/KurdishCharacterConvertor-Windows.zip) and for **macOS** [here](https://github.com/Azhy-Slemany/kurdish/releases/download/1.0.0/KurdishCharacterConvertor-Mac.zip) and for more visit [here](https://github.com/Azhy-Slemany/kurdish/tree/master/GUI).

- Python Library Installation

  How to install the module:

  `pip install Kurdish`

  for python 3 in Linux:

  `pip3 install Kurdish`

  - [How to install Python modules](https://docs.python.org/3.8/installing/index.html)

---

## Pellk vs. Kurdish

There are some small issues with **[Pellk](http://chawg.org/kurdi-nus/)** which in Kurdish tried to be fixed and provide much more appropriate transliterated text.

| Arabic-based Kurdish | Pellk Transliteration | Kurdish Transliteration |
| -------------------- | --------------------- | ----------------------- |
| نۆرمبێرگ             | Normibêrg             | Norimbêrg               |
| دەستگیر              | destigîr              | destgîr                 |
| رابردوو              | Rabridû               | Rabirdû                 |
| فەڕەنسیەکان          | Ferrenisyekan         | Feŕensyekan             |
| کورتترە              | kurtitre              | kurttre                 |
| پێکرد                | pêkrid                | pêkird                  |
| بە KNNی راگەیاند     | be KiNNî rageyand     | be KNNî ŕageyand        |
| بونیادنراوە          | bunyadinrawe          | bunyadnirawe            |

## How to use

### Transliteration Arabic-based Kurdish to Latin-based Kurdish

```python
from kurdish import ku
text = 'ئەسیری بسکی ئاڵۆزی کچە کوردێکی نەشمیلم، تەماشا کەن چ سەیرێکە بەدەستی دیلەوە دیلم. (هێمن موکریانی)'
print(ku.Hemwar().transliterate(text))

OUTPUT:
Esîrî biskî aĺozî kçe kurdêkî neşmîlm, temaşa ken çi seyrêke bedestî dîlewe dîlm. (hêmin mukiryanî)
```

### Converting Characters and Digits

- #### Converting English Characters to Arabic-based Kurdish Based on [KRG Unicode System](http://Unicode.ekrg.org/ku_Unicodes.html):
  The major difference with KRG System is ( ھ = U+06BE ARABIC LETTER HEH DOACHASHMEE ) letter which normally in Arabic-based writing system ( ه = U+0647 ARABIC LETTER HEH ) alternatively has been used. For making the exact shape, you can use ( ه = U+0647 ARABIC LETTER HEH ) + ( ـ = U+0640 ARABIC TATWEEL ). The result will be ( هـ ).

```python
from kurdish import ku
print('Convert English characters to Kurdish:')
print(ku.Hemwar().En_Char_to_Ku('bexSyn le gwnah w heLe CawpoSyne! \n to Con heReSet be uagry pRtyne? \n bmbexSy be nwYjanewe, kesman le kese \n be gwnahewe bmbexSe, delYm bexSyne'))

OUTPUT:
Convert English characters to Kurdish:
بەخشین لە گوناه و هەڵە چاوپۆشینە!
تۆ چۆن هەڕەشەت بە ئاگری پڕتینە؟
بمبەخشی بە نوێژانەوە، کەسمان لە کەسە،
بە گوناهەوە بمبەخشە، دەلێم بەخشینە
```

- #### Converting Arabic Characters to Kurdish:

```python
from kurdish import ku
print('Convert Arabic characters to Kurdish:')
print(ku.Hemwar().Ar_Char_to_Ku("ك، ي = كوردي  /  ك = كاف"))

OUTPUT:
Convert Arabic characters to Kurdish:
ک، ی = کوردی  /  ک = کاف
```

- #### Converting Arabic-based Kurdish Characters to English:

```python
from kurdish import ku
print('Convert Kurdish characters to English:')
print(ku.Hemwar().Ku_Char_to_En('\n بەخشین لە گوناه و هەڵە چاوپۆشینە! \nتۆ چۆن هەڕەشەت بە ئاگری پڕتینە?\n بمبەخشی بە نوێژانەوە, کەسمان لە کەسە\n بە گوناهەوە بمبەخشە, دەلێم بەخشینە'))

OUTPUT:
Convert Kurdish characters to English:
bexSyn le gwnah w heLe CawpoSyne!
to Con heReSet be uagry pRtyne?
bmbexSy be nwYjanewe, kesman le kese
be gwnahewe bmbexSe, delYm bexSyne
```

**Note:** _This function has been used in some of my personal projects but still for some people can be useful!_

- #### Getting Unicode code of any character or digit:

```python
from kurdish import ku
print('Getting Unicode code for instance: all Arabic specific characters\n')
print(ku.Hemwar().getUniNum(ku.Hemwar.Ar_Special_chars))

OUTPUT:
Getting Unicode code for instance: all Arabic specific characters
1. ص = U+0635 ARABIC LETTER SAD
2. ض = U+0636 ARABIC LETTER DAD
3. ط = U+0637 ARABIC LETTER TAH
4. ظ = U+0638 ARABIC LETTER ZAH
5. ذ = U+0630 ARABIC LETTER THAL
6. ي = U+064a ARABIC LETTER YEH
7. ة = U+0629 ARABIC LETTER TEH MARBUTA
8. ث = U+062b ARABIC LETTER THEH
9. ؤ = U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE
10. أ = U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE
11. إ = U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW
12. آ = U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE
13. ك = U+0643 ARABIC LETTER KAF
14. ۀ = U+06c0 ARABIC LETTER HEH WITH YEH ABOVE
15. ى = U+0649 ARABIC LETTER ALEF MAKSURA

Conversion has been completed successfully.
```

- #### Getting all Arabic-based Kurdish Alphabet in a list:

```python
from kurdish import ku
print('Arabic-based Kurdish Alphabet: ')
print(list(ku.Hemwar().ku_alphabet_Ar))

OUTPUT:
Arabic-based Kurdish Alphabet:
['ئ', 'ا', 'ب', 'پ', 'ت', 'ج', 'چ', 'ح', 'خ', 'د', 'ر', 'ڕ', 'ز', 'ژ', 'س', 'ش', 'ع', 'غ', 'ف', 'ڤ', 'ق', 'ک', 'گ', 'ل', 'ڵ', 'م', 'ن', 'ه', 'ە', 'و', 'ۆ', 'و', 'و', 'ی', 'ێ']
```

- #### Getting all Latin-based Kurdish Alphabet in a list:

```python
from kurdish import ku
print('Latin-based Kurdish Alphabet: ')
print(list(ku.Hemwar().ku_alphabet_La_uppercase))

OUTPUT:
Latin-based Kurdish Alphabet:
['A', 'B', 'C', 'Ç', 'D', 'E', 'Ê', 'F', 'G', 'H', 'Ĥ', 'I', 'Î', 'J', 'K', 'L', 'Ĺ', 'M', 'N', 'O', 'P', 'Q', 'R', 'Ŕ', 'S', 'Ş', 'T', 'U', 'Û', 'V', 'W', 'X', 'Ẍ', 'Y', 'Z']
```

- #### Getting all Latin-based and Arabic-based Kurdish vowels in a list:

```python
from kurdish import ku
print('All Latin-based and Arabic-based Kurdish vowels:')
print(list(ku.Hemwar().ku_all_V))

OUTPUT:
All Latin-based and Arabic-based Kurdish vowels:
['A', 'E', 'Ê', 'I', 'Î', 'O', 'U', 'Û', 'a', 'e', 'ê', 'i', 'î', 'o', 'u', 'û', 'ا', 'ە', 'و', 'ۆ', 'و', 'و', 'ی', 'ێ']
```

- #### Converting Persian (Farsi) Digits to Arabic-based Kurdish:

```python
from kurdish import ku
print('Convert Persian digits to Arabic-based Kurdish: ')
print(ku.Hemwar().Fa_Digit_to_Ku('٠١٢٣۴۵۶٧٨٩'))

OUTPUT:
Convert Persian digits to Arabic-based Kurdish:
٠١٢٣٤٥٦٧٨٩
```

- #### Converting Arabic-based Kurdish Digits to Persian (Farsi):

```python
from kurdish import ku
print('Convert Arabic-based Kurdish digits to Persian: ')
print(ku.Hemwar().Ku_Digit_to_Fa('٠١٢٣٤٥٦٧٨٩'))

OUTPUT:
Convert Arabic-based Kurdish digits to Persian:
۰۱۲۳۴۵۶۷۸۹
```

- #### Converting English Digits to Arabic-based Kurdish:

```python
from kurdish import ku
print('Convert English digits to Arabic-based Kurdish: ')
print(ku.Hemwar().En_Digit_to_Ku('0123456789'))

OUTPUT:
Convert English digits to Arabic-based Kurdish:
٠١٢٣٤٥٦٧٨٩
```

- #### Converting Arabic-based Kurdish Digits to English:

```python
from kurdish import ku
print('Convert Arabic-based Kurdish digits to English: ')
print(ku.Hemwar().Ku_Digit_to_En('٠١٢٣٤٥٦٧٨٩'))

OUTPUT:
Convert Arabic-based Kurdish digits to English:
0123456789
```

### Converting Ali-k style to unicode

```python
from kurdish import ku
text = 'طوماني تيَدا نيية لة هةر دوو دنيا دا ئةركة طشتيةكان دةبنة هؤى خؤشةويستي، هؤى ثةرِينةوة لة تةنطذةكان، هؤى دةرباز بوون لة تووشيان، هؤى ثاراستني سةلامةتي طيان و جةستة و لة وتةيةكدا هؤى لةخؤ رازيكردني خوا و خةلَكي خوا و دلَنيابوون لة داهاتوو'
print(ku.Hemwar().ali_k_to_uni(text))

OUTPUT:
گومانی تێدا نییە لە هەر دوو دنیا دا ئەرکە گشتیەکان دەبنە هۆی خۆشەویستی، هۆی پەڕینەوە لە تەنگژەکان، هۆی دەرباز بوون لە تووشیان، هۆی پاراستنی سەلامەتی گیان و جەستە و لە وتەیەکدا هۆی لەخۆ رازیکردنی خوا و خەڵکی خوا و دڵنیابوون لە داهاتوو
```

## Arabic-based Kurdish Characters along with their Unicode Equivalent

| Character | Unicode Code                                                                                                                                             |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ئ         | U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE                                                                                                                |
| ا         | U+0627 ARABIC LETTER ALEF                                                                                                                                |
| ب         | U+0628 ARABIC LETTER BEH                                                                                                                                 |
| پ         | U+067e ARABIC LETTER PEH                                                                                                                                 |
| ت         | U+062a ARABIC LETTER TEH                                                                                                                                 |
| ج         | U+062c ARABIC LETTER JEEM                                                                                                                                |
| چ         | U+0686 ARABIC LETTER TCHEH                                                                                                                               |
| ح         | U+062d ARABIC LETTER HAH                                                                                                                                 |
| خ         | U+062e ARABIC LETTER KHAH                                                                                                                                |
| د         | U+062f ARABIC LETTER DAL                                                                                                                                 |
| ر         | U+0631 ARABIC LETTER REH                                                                                                                                 |
| ڕ         | U+0695 ARABIC LETTER REH WITH SMALL V BELOW                                                                                                              |
| ز         | U+0632 ARABIC LETTER ZAIN                                                                                                                                |
| ژ         | U+0698 ARABIC LETTER JEH                                                                                                                                 |
| س         | U+0633 ARABIC LETTER SEEN                                                                                                                                |
| ش         | U+0634 ARABIC LETTER SHEEN                                                                                                                               |
| ع         | U+0639 ARABIC LETTER AIN                                                                                                                                 |
| غ         | U+063a ARABIC LETTER GHAIN                                                                                                                               |
| ف         | U+0641 ARABIC LETTER FEH                                                                                                                                 |
| ڤ         | U+06a4 ARABIC LETTER VEH                                                                                                                                 |
| ق         | U+0642 ARABIC LETTER QAF                                                                                                                                 |
| ک         | U+06a9 ARABIC LETTER KEHEH                                                                                                                               |
| گ         | U+06af ARABIC LETTER GAF                                                                                                                                 |
| ل         | U+0644 ARABIC LETTER LAM                                                                                                                                 |
| ڵ         | U+06b5 ARABIC LETTER LAM WITH SMALL V                                                                                                                    |
| م         | U+0645 ARABIC LETTER MEEM                                                                                                                                |
| ن         | U+0646 ARABIC LETTER NOON                                                                                                                                |
| ه         | U+0647 ARABIC LETTER HEH                                                                                                                                 |
| ە         | U+06d5 ARABIC LETTER AE                                                                                                                                  |
| و         | U+0648 ARABIC LETTER WAW                                                                                                                                 |
| ۆ         | U+06c6 ARABIC LETTER OE                                                                                                                                  |
| وو        | U+0648 ARABIC LETTER WAW (X2) Vowel version of the letter is not defined yet. The same shape but doubled and different Unicode code should be dedicated. |
| ی         | U+06cc ARABIC LETTER FARSI YEH                                                                                                                           |
| ێ         | U+06ce ARABIC LETTER YEH WITH SMALL V                                                                                                                    |
| و         | Consonant version of the letter is not defined yet. The same shape but different Unicode code should be dedicated.                                       |
| ی         | Consonant version of the letter is not defined yet. The same shape but different Unicode code should be dedicated.                                       |
| بزرۆکە    | Bizroke, Which won't be written in the Arabic-based Kurdish writing System.                                                                              |

## Arabic-based Kurdish Digits along with their Unicode Equivalent

| Digit | Unicode Code                    |
| ----- | ------------------------------- |
| ٠     | U+0660 ARABIC-INDIC DIGIT ZERO  |
| ١     | U+0661 ARABIC-INDIC DIGIT ONE   |
| ٢     | U+0662 ARABIC-INDIC DIGIT TWO   |
| ٣     | U+0663 ARABIC-INDIC DIGIT THREE |
| ٤     | U+0664 ARABIC-INDIC DIGIT FOUR  |
| ٥     | U+0665 ARABIC-INDIC DIGIT FIVE  |
| ٦     | U+0666 ARABIC-INDIC DIGIT SIX   |
| ٧     | U+0667 ARABIC-INDIC DIGIT SEVEN |
| ٨     | U+0668 ARABIC-INDIC DIGIT EIGHT |
| ٩     | U+0669 ARABIC-INDIC DIGIT NINE  |

## Latin-based Kurdish Characters along with Unicode Equivalent

| Character | Unicode Code                                                                                                                                                                                                                                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A         | U+0041 LATIN CAPITAL LETTER A                                                                                                                                                                                                                                                                                                                                      |
| B         | U+0042 LATIN CAPITAL LETTER B                                                                                                                                                                                                                                                                                                                                      |
| C         | U+0043 LATIN CAPITAL LETTER C                                                                                                                                                                                                                                                                                                                                      |
| Ç         | U+00c7 LATIN CAPITAL LETTER C WITH CEDILLA                                                                                                                                                                                                                                                                                                                         |
| D         | U+0044 LATIN CAPITAL LETTER D                                                                                                                                                                                                                                                                                                                                      |
| E         | U+0045 LATIN CAPITAL LETTER E                                                                                                                                                                                                                                                                                                                                      |
| Ê         | U+00ca LATIN CAPITAL LETTER E WITH CIRCUMFLEX                                                                                                                                                                                                                                                                                                                      |
| F         | U+0046 LATIN CAPITAL LETTER F                                                                                                                                                                                                                                                                                                                                      |
| G         | U+0047 LATIN CAPITAL LETTER G                                                                                                                                                                                                                                                                                                                                      |
| H         | U+0048 LATIN CAPITAL LETTER H                                                                                                                                                                                                                                                                                                                                      |
| I         | U+0049 LATIN CAPITAL LETTER I                                                                                                                                                                                                                                                                                                                                      |
| Î         | U+00ce LATIN CAPITAL LETTER I WITH CIRCUMFLEX                                                                                                                                                                                                                                                                                                                      |
| J         | U+004a LATIN CAPITAL LETTER J                                                                                                                                                                                                                                                                                                                                      |
| K         | U+004b LATIN CAPITAL LETTER K                                                                                                                                                                                                                                                                                                                                      |
| L         | U+004c LATIN CAPITAL LETTER L                                                                                                                                                                                                                                                                                                                                      |
| M         | U+004d LATIN CAPITAL LETTER M                                                                                                                                                                                                                                                                                                                                      |
| N         | U+004e LATIN CAPITAL LETTER N                                                                                                                                                                                                                                                                                                                                      |
| O         | U+004f LATIN CAPITAL LETTER O                                                                                                                                                                                                                                                                                                                                      |
| P         | U+0050 LATIN CAPITAL LETTER P                                                                                                                                                                                                                                                                                                                                      |
| Q         | U+0051 LATIN CAPITAL LETTER Q                                                                                                                                                                                                                                                                                                                                      |
| R         | U+0052 LATIN CAPITAL LETTER R                                                                                                                                                                                                                                                                                                                                      |
| S         | U+0053 LATIN CAPITAL LETTER S                                                                                                                                                                                                                                                                                                                                      |
| Ş         | U+015e LATIN CAPITAL LETTER S WITH CEDILLA                                                                                                                                                                                                                                                                                                                         |
| T         | U+0054 LATIN CAPITAL LETTER T                                                                                                                                                                                                                                                                                                                                      |
| U         | U+0055 LATIN CAPITAL LETTER U                                                                                                                                                                                                                                                                                                                                      |
| Û         | U+00db LATIN CAPITAL LETTER U WITH CIRCUMFLEX                                                                                                                                                                                                                                                                                                                      |
| V         | U+0056 LATIN CAPITAL LETTER V                                                                                                                                                                                                                                                                                                                                      |
| W         | U+0057 LATIN CAPITAL LETTER W                                                                                                                                                                                                                                                                                                                                      |
| X         | U+0058 LATIN CAPITAL LETTER X                                                                                                                                                                                                                                                                                                                                      |
| Y         | U+0059 LATIN CAPITAL LETTER Y                                                                                                                                                                                                                                                                                                                                      |
| Z         | U+005a LATIN CAPITAL LETTER Z                                                                                                                                                                                                                                                                                                                                      |
| Ĥ         | This letter should be defined as an equivalent for ( ح ).                                                                                                                                                                                                                                                                                                          |
| RR        | R̂ (R + ̂ = [U+0052 LATIN CAPITAL LETTER R + U+0302 COMBINING CIRCUMFLEX ACCENT] ). No unique character is defined yet. The shape should be like ( R̂ ) but there is no single defined Unicode code. Note that in this module as a temporary character, we have been allocated Unicode Character ( Ŕ = U+0154 / ŕ = U+0155) to prevent the misuse of two (RR / rr)).  |
| LL        | L̂ (L + ̂ = [U+004c LATIN CAPITAL LETTER L + U+0302 COMBINING CIRCUMFLEX ACCENT] ). No unique character is defined yet. The shape should be like ( L̂ ) but there is no single defined Unicode code. Note that in this module as a temporary character, we have been allocated Unicode Character ( Ĺ = U+0139 / ĺ = U+013A) to prevent the misuse of two (LL / ll)).  |
| XX        | X̂ (X + ̂ = [U+0058 LATIN CAPITAL LETTER X + U+0302 COMBINING CIRCUMFLEX ACCENT] ) . No unique character is defined yet. The shape should be like ( X̂ ) but there is no single defined Unicode code. Note that in this module as a temporary character, we have been allocated Unicode Character ( Ẍ = U+1E8C / ẍ = U+1E8D) to prevent the misuse of two (XX / xx)). |
| ع         | No letter is defined yet. No shape and no Unicode code. At the moment, we are using only [ ' ] an apostrophe-like.                                                                                                                                                                                                                                                 |
| ئ         | No letter is defined yet. No shape and no Unicode code. Tottally, in Latin-based Kurdish, it has been removed.                                                                                                                                                                                                                                                     |

## Latin-based Kurdish Digits along with their Unicode Equivalent (Same as English)

| Digit | Unicode Code       |
| ----- | ------------------ |
| 0     | U+0030 DIGIT ZERO  |
| 1     | U+0031 DIGIT ONE   |
| 2     | U+0032 DIGIT TWO   |
| 3     | U+0033 DIGIT THREE |
| 4     | U+0034 DIGIT FOUR  |
| 5     | U+0035 DIGIT FIVE  |
| 6     | U+0036 DIGIT SIX   |
| 7     | U+0037 DIGIT SEVEN |
| 8     | U+0038 DIGIT EIGHT |
| 9     | U+0039 DIGIT NINE  |

## Arabic-based Persian Digits along with their Unicode Equivalent

Arabic-based Persian Unicode Digits (Completely different Unicode codes with Arabic-based Kurdish but some of them are the same as Arabic-based Persian **ONLY** in shape. (۴۵۶) are different in shape and Unicode code, but the others (٠١٢٣٧٨٩) are the same ONLY in shape).

| Digit | Unicode Code                             |
| ----- | ---------------------------------------- |
| ۰     | U+06f0 EXTENDED ARABIC-INDIC DIGIT ZERO  |
| ۱     | U+06f1 EXTENDED ARABIC-INDIC DIGIT ONE   |
| ۲     | U+06f2 EXTENDED ARABIC-INDIC DIGIT TWO   |
| ۳     | U+06f3 EXTENDED ARABIC-INDIC DIGIT THREE |
| ۴     | U+06f4 EXTENDED ARABIC-INDIC DIGIT FOUR  |
| ۵     | U+06f5 EXTENDED ARABIC-INDIC DIGIT FIVE  |
| ۶     | U+06f6 EXTENDED ARABIC-INDIC DIGIT SIX   |
| ۷     | U+06f7 EXTENDED ARABIC-INDIC DIGIT SEVEN |
| ۸     | U+06f8 EXTENDED ARABIC-INDIC DIGIT EIGHT |
| ۹     | U+06f9 EXTENDED ARABIC-INDIC DIGIT NINE  |

## Extra Arabic Characters

Extra Arabic characters which are **NOT** used in Arabic-based Kurdish but will be used in Arabic-based Persian.

| Character | Unicode Code                               |
| --------- | ------------------------------------------ |
| ص         | U+0635 ARABIC LETTER SAD                   |
| ض         | U+0636 ARABIC LETTER DAD                   |
| ط         | U+0637 ARABIC LETTER TAH                   |
| ظ         | U+0638 ARABIC LETTER ZAH                   |
| ذ         | U+0630 ARABIC LETTER THAL                  |
| ي         | U+064a ARABIC LETTER YEH                   |
| ة         | U+0629 ARABIC LETTER TEH MARBUTA           |
| ث         | U+062b ARABIC LETTER THEH                  |
| ؤ         | U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE  |
| أ         | U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE |
| إ         | U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW |
| آ         | U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE |
| ك         | U+0643 ARABIC LETTER KAF                   |
| ۀ         | U+06c0 ARABIC LETTER HEH WITH YEH ABOVE    |
| ى         | U+0649 ARABIC LETTER ALEF MAKSURA          |

---

## To-DO List

- Currecting issues with transliterated Latin-based version
- Capitalizing names such as persons, cities, countries, etc. in Latin-based version with providing a list of names
- Providing Latin-based to Arabic-based transliteration

---

## Getting help

If you have questions about the python library **Kurdish** module, or run into problems, or if you want to contribute in any way, feel free to reach out to me via below links:

- **[GitHub](https://github.com/dolanskurd)**
- **[PyPI](https://pypi.org/project/kurdish/)**
- **[Twitter](http://www.twitter.com/dolanskurd)**
- **E-mail: [dolanskurd@mail.com](mailto:dolanskurd@mail.com)**

And for problems in the GUI you can mail to **[KDoblaj@gmail.com](mailto:KDoblaj@gmail.com)**.

## License

Kurdish Language Library is available under the **MIT license**.
