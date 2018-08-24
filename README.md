# Kurdish 

Welcome to `Kurdish Language Library` - a Python Library for converting characters and numbers in Persian, English and also Arabic to Kurdish and vice versa.



## Installation

Installing the module:

`
pip install Kurdish
`

* [Installing Python modules](https://docs.python.org/3/installing/index.html "Installing Python modules")

------------

## How to use the module


* Converting English Characters to Kurdish Based on KRG Unicode System (http://unicode.ekrg.org/ku_unicodes.html):
```python
print('Kurdish.convert_En_Char_to_Ku', Kurdish.convert_En_Char_to_Ku('bexSyn le gwnah w heLe CawpoSyne! \n to Con heReSet be uagry pRtyne? \n bmbexSy be nwYjanewe, kesman le kese \n be gwnahewe bmbexSe, delYm bexSyne'))
```


* Converting Arabic Characters to Kurdish:
```python
print('Kurdish.convert_Ar_Char_to_Ku', Kurdish.convert_Ar_Char_to_Ku('“يقول نيتشه: "الدين ثورة العبيد". ويقول ماركس: "الدين أفيون الشعوب". وفي الحقيقة إنّ الدين ثورة وأفيون في آن واحد. فهو عند المترفين أفيون وعند الأنبياء ثورة. وكل دين يبدأ على يد النبي ثورة ثم يستحوذ المترفون عليه بعد ذلك فيحولونه إلى أفيون. وعندئذ يظهر نبي جديد فيعيدها شعواء مرة أخرى.”― علي الوردي, مهزلة العقل البشري '))
```


* Converting Kurdish Characters to English:
```python
print('Kurdish.convert_Ku_Char_to_En', Kurdish.convert_Ku_Char_to_En('بەخشین لە گوناه و هەڵە چاوپۆشینە! \n  \nتۆ چۆن هەڕەشەت بە ئاگری پڕتینە?\n بمبەخشی بە نوێژانەوە, کەسمان لە کەسە\n بە گوناهەوە بمبەخشە, دەلێم بەخشینە'))
```


* Converting Persian (Farsi) Numbers to Kurdish:
```python
print('Kurdish.convert_Fa_Num_to_Ku', Kurdish.convert_Fa_Num_to_Ku('٠١٢٣۴۵۶٧٨٩'))
```


* Converting Kurdish Numbers to Persian (Farsi):
```python
print('Kurdish.convert_Ku_Num_to_Fa', Kurdish.convert_Ku_Num_to_Fa('٠١٢٣٤٥٦٧٨٩'))
```


* Converting English Numbers to Kurdish:
```python
print('Kurdish.convert_En_Num_to_Ku', Kurdish.convert_En_Num_to_Ku('0123456789'))
```


* Converting Kurdish Numbers to English:
```python
print('Kurdish.convert_Ku_Num_to_En', Kurdish.convert_Ku_Num_to_En('٠١٢٣٤٥٦٧٨٩'))
```

## Kurdish Unicode Characters

 Basic Latin|پیت|یونیکۆد
----|-------|-----
u	|	ئ	|	U+0626
a	|	ا	|	U+0627
b	|	ب	|	U+0628
p	|	پ	|	U+067E
t	|	ت	|	U+062A
c	|	ج	|	U+062C
C	|	چ	|	U+0686
I	|	ح	|	U+062D
x	|	خ	|	U+062E
d	|	د	|	U+062F
r	|	ر	|	U+0631
R	|	ڕ	|	U+0695
z	|	ز	|	U+0632
j	|	ژ	|	U+0698
s	|	س	|	U+0633
S	|	ش	|	U+0634
i	|	ع	|	U+0639
G	|	غ	|	U+063A
f	|	ف	|	U+0641
v	|	ڤ	|	U+06A4
q	|	ق	|	U+0642
k	|	ک	|	U+06A9
g	|	گ	|	U+06AF
l	|	ل	|	U+0644
L	|	ڵ	|	U+06B5
m	|	م	|	U+0645
n	|	ن	|	U+0646
w	|	و	|	U+0648
o	|	ۆ	|	U+06C6
h	|	ھ	|	U+0647
e	|	ە	|	U+06D5
y	|	ی	|	U+06CC
Y	|	ێ	|	U+06CE

## Kurdish Unicode Numbers

ژمارە	|	یونیکۆد	|	ژمارە	|	یونیکۆد
----------|	----------|	----------|	------------ 
0	|	U+0660	|	5	|	U+0665
1	|	U+0661	|	6	|	U+0666
2	|	U+0662	|	7	|	U+0667
3	|	U+0663	|	8	|	U+0668
4	|	U+0664	|	9	|	U+0669


## Contact me

I hope you like this library. Feel free to reach out if you have questions or if
you want to contribute in any way:

* E-mail: [dolanskurd@mail.com](mailto:dolanskurd@mail.com)
* Twitter: [@dolanskurd](http://www.twitter.com/dolanskurd)


## License

Kurdish is available under the MIT license. See LICENSE file for more info.
