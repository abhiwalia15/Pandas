#Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
#Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
import pandas as pd

df = pd.read_csv('googleplaystore.csv')
df.to_json('playstore_dataset.json')
df.to_clipboard()
#print(df)



SyntaxError: multiple statements found while compiling a single statement
>>> import pandas as pd
>>> import numpy as np
>>> df = pd.read_csv('googleplaystore.csv')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    df = pd.read_csv('googleplaystore.csv')
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'googleplaystore.csv' does not exist
>>> df = pd.read_csv('G:\github\Pandas\PlayStoreDataSet\googleplaystore.csv')
>>> df.head(2)
                                              App      ...        Android Ver
0  Photo Editor & Candy Camera & Grid & ScrapBook      ...       4.0.3 and up
1                             Coloring book moana      ...       4.0.3 and up

[2 rows x 13 columns]
>>> pd.DataFrame(np.random.rand(20,5))
           0         1         2         3         4
0   0.994515  0.581136  0.359067  0.716463  0.389477
1   0.701808  0.996018  0.658034  0.467356  0.804315
2   0.419829  0.000517  0.348329  0.892025  0.420687
3   0.537960  0.391826  0.081082  0.914899  0.173205
4   0.606052  0.679538  0.553614  0.789158  0.522167
5   0.648839  0.831325  0.650540  0.189396  0.009585
6   0.604320  0.415603  0.214971  0.102989  0.275095
7   0.057474  0.478830  0.952472  0.222832  0.507946
8   0.548819  0.940779  0.293432  0.962178  0.807841
9   0.241358  0.144870  0.515102  0.394562  0.313718
10  0.897249  0.965644  0.674586  0.227895  0.849130
11  0.928155  0.502270  0.560679  0.495492  0.119780
12  0.357660  0.619824  0.829273  0.691052  0.768145
13  0.955684  0.134764  0.915240  0.254802  0.753446
14  0.516245  0.757687  0.229120  0.254933  0.055824
15  0.353565  0.923462  0.656783  0.914736  0.244915
16  0.472701  0.635002  0.605568  0.636072  0.327238
17  0.782400  0.433083  0.223345  0.962104  0.622216
18  0.579434  0.148739  0.774600  0.379408  0.562751
19  0.437480  0.361416  0.005785  0.206339  0.814473
>>> pd.DataFrame(np.random.rand(20,5)*100)
            0          1          2          3          4
0   78.737845   8.491011  33.567554  45.621525  88.741521
1   68.278138  37.570353  24.731615  43.346832  44.409615
2   66.199947  42.077746  49.427907  98.828988  30.365201
3   51.753058  42.746018  71.448711  73.566545   6.831820
4   84.950373  79.086616   8.826354  14.146885  21.854067
5   74.281919  71.739396  61.354651  73.589183  73.429675
6   37.751269  84.132795  96.315562  92.806994  59.569558
7   94.657612  77.634792  98.510493  47.716379  46.909627
8   62.422479  59.846643  68.305258  75.212354  67.845539
9   70.735680  84.659460  75.412179  94.302594   5.511944
10  11.248462  44.378159  67.640956  15.522329   9.756589
11  75.326311   8.580533  22.688996  84.932842   0.246112
12   2.871342   8.755825  56.283719  68.993944  88.352974
13  46.790464  26.932179  10.516153  23.662471  37.469959
14  22.935959  22.521992  26.068053  83.528823  52.391219
15  13.653393  60.201438  21.933172  50.433781  92.229466
16  74.345487  33.462020  52.175864  91.859577  66.880752
17  63.311285   6.675821   6.523334  57.010625  81.859044
18  92.419174  29.533576  51.368655  19.900543  63.203689
19  22.194959  98.683240  82.888087   8.623504  88.059112
>>> pd.Series(df)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    pd.Series(df)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 277, in __init__
    data = SingleBlockManager(data, index, fastpath=True)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 4677, in __init__
    block = make_block(block, placement=slice(0, len(axis)), ndim=1)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 3205, in make_block
    return klass(values, ndim=ndim, placement=placement)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 2303, in __init__
    placement=placement)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 125, in __init__
    '{mgr}'.format(val=len(self.values), mgr=len(self.mgr_locs)))
ValueError: Wrong number of items passed 13, placement implies 10841
>>> for dfs in df:
	users

Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    users
NameError: name 'users' is not defined
>>> df.index = 'ORDER'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    df.index = 'ORDER'
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4389, in __setattr__
    return object.__setattr__(self, name, value)
  File "pandas\_libs\properties.pyx", line 69, in pandas._libs.properties.AxisProperty.__set__
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 646, in _set_axis
    self._data.set_axis(axis, labels)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 3316, in set_axis
    new_labels = _ensure_index(new_labels)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 4974, in _ensure_index
    return Index(index_like)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 437, in __new__
    cls._scalar_data_error(data)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 897, in _scalar_data_error
    repr(data)))
TypeError: Index(...) must be called with a collection of some kind, 'ORDER' was passed
>>> df
                                                     App         ...                 Android Ver
0         Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1                                    Coloring book moana         ...                4.0.3 and up
2      U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
3                                  Sketch - Draw & Paint         ...                  4.2 and up
4                  Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
5                             Paper flowers instructions         ...                  2.3 and up
6                Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
7                                       Infinite Painter         ...                  4.2 and up
8                                   Garden Coloring Book         ...                  3.0 and up
9                          Kids Paint Free - Drawing Fun         ...                4.0.3 and up
10                               Text on Photo - Fonteee         ...                  4.1 and up
11               Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
12                        Tattoo Name On My Photo Editor         ...                  4.1 and up
13                                 Mandala Coloring Book         ...                  4.4 and up
14       3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
15                       Learn To Draw Kawaii Characters         ...                  4.2 and up
16          Photo Designer - Write your name with shapes         ...                  4.1 and up
17                              350 Diy Room Decor Ideas         ...                  2.3 and up
18                         FlipaClip - Cartoon animation         ...                4.0.3 and up
19                                          ibis Paint X         ...                  4.1 and up
20                           Logo Maker - Small Business         ...                  4.1 and up
21             Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
22               Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
23                                Mcqueen Coloring pages         ...                  4.1 and up
24                           HD Mickey Minnie Wallpapers         ...                  4.1 and up
25                            Harley Quinn wallpapers HD         ...                  3.0 and up
26                         Colorfit - Drawing & Coloring         ...                4.0.3 and up
27                                 Animated Photo Editor         ...                4.0.3 and up
28                                 Pencil Sketch Drawing         ...                  2.3 and up
29                       Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                  ...         ...                         ...
10811                                        FR Plus 1.6         ...                 4.4W and up
10812                                      Fr Agnel Pune         ...                4.0.3 and up
10813                                     DICT.fr Mobile         ...                  4.1 and up
10814                               FR: My Secret Pets!          ...                  3.0 and up
10815                          Golden Dictionary (FR-AR)         ...                  4.2 and up
10816                                 FieldBi FR Offline         ...                  4.1 and up
10817                               HTC Sense Input - FR         ...                  5.0 and up
10818                               Gold Quote - Gold.fr         ...                  2.2 and up
10819                                          Fanfic-FR         ...                  4.1 and up
10820                                    Fr. Daoud Lamei         ...                  4.1 and up
10821                                            Poop FR         ...                4.0.3 and up
10822                                          PLMGSS FR         ...                  4.4 and up
10823                                       List iptv FR         ...                4.0.3 and up
10824                                          Cardio-FR         ...                  4.4 and up
10825                                 Naruto & Boruto FR         ...                  4.0 and up
10826          Frim: get new friends on local chat rooms         ...          Varies with device
10827                                 Fr Agnel Ambarnath         ...                4.0.3 and up
10828                            Manga-FR - Anime Vostfr         ...                  4.0 and up
10829                     Bulgarian French Dictionary Fr         ...                  4.1 and up
10830                                  News Minecraft.fr         ...                  1.6 and up
10831                           payermonstationnement.fr         ...                  4.0 and up
10832                                           FR Tides         ...                  2.1 and up
10833                                        Chemin (fr)         ...                  2.2 and up
10834                                      FR Calculator         ...                  4.1 and up
10835                                           FR Forms         ...                  4.0 and up
10836                                   Sya9a Maroc - FR         ...                  4.1 and up
10837                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
10838                             Parkinson Exercices FR         ...                  2.2 and up
10839                      The SCP Foundation DB fr nn5n         ...          Varies with device
10840      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df.set.index = 'NO.'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df.set.index = 'NO.'
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'set'
>>> df.set_index('NO.')
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'NO.'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df.set_index('NO.')
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 3909, in set_index
    level = frame[col]._values
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'NO.'
>>> df = df.set_index(('no.'))
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'no.'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df = df.set_index(('no.'))
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 3909, in set_index
    level = frame[col]._values
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'no.'
>>> df.index = pd.date_range('1900/1/30', periods=df.shape[0])
>>> df
                                                          App         ...                 Android Ver
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df.tail(2)
                                                      App         ...                 Android Ver
1929-10-04                  The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05  iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[2 rows x 13 columns]
>>> df.shape()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    df.shape()
TypeError: 'tuple' object is not callable
>>> df.shape()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    df.shape()
TypeError: 'tuple' object is not callable
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 10841 entries, 1900-01-30 to 1929-10-05
Freq: D
Data columns (total 13 columns):
App               10841 non-null object
Category          10841 non-null object
Rating            9367 non-null float64
Reviews           10841 non-null object
Size              10841 non-null object
Installs          10841 non-null object
Type              10840 non-null object
Price             10841 non-null object
Content Rating    10840 non-null object
Genres            10841 non-null object
Last Updated      10841 non-null object
Current Ver       10833 non-null object
Android Ver       10838 non-null object
dtypes: float64(1), object(12)
memory usage: 677.6+ KB
>>> df.describe()
            Rating
count  9367.000000
mean      4.193338
std       0.537431
min       1.000000
25%       4.000000
50%       4.300000
75%       4.500000
max      19.000000
>>> df.describe(1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    df.describe(1)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 8504, in describe
    percentiles = list(percentiles)
TypeError: 'int' object is not iterable
>>> df.describe(axis=0)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    df.describe(axis=0)
TypeError: describe() got an unexpected keyword argument 'axis'
>>> df.describe()
            Rating
count  9367.000000
mean      4.193338
std       0.537431
min       1.000000
25%       4.000000
50%       4.300000
75%       4.500000
max      19.000000
>>> s = np.arange(9)
>>> s
array([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> pd.Series(s)
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.value_counts(dropna=False)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.value_counts(dropna=False)
AttributeError: 'numpy.ndarray' object has no attribute 'value_counts'
>>> df.apply(pd.Series.value_counts)

Warning (from warnings module):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\api.py", line 107
    result = result.union(other)
RuntimeWarning: '<' not supported between instances of 'str' and 'float', sort order is undefined for incomparable objects
                                                    App     ...       Android Ver
"i DT" Fútbol. Todos Somos Técnicos.                1.0     ...               NaN
+Download 4 Instagram Twitter                       1.0     ...               NaN
- Free Comics - Comic Apps                          1.0     ...               NaN
.R                                                  1.0     ...               NaN
/u/app                                              1.0     ...               NaN
058.ba                                              1.0     ...               NaN
1. FC Köln App                                      1.0     ...               NaN
1.9                                                 NaN     ...               NaN
10 Best Foods for You                               2.0     ...               NaN
10 Minutes a Day Times Tables                       1.0     ...               NaN
10 WPM Amateur ham radio CW Morse code trainer      1.0     ...               NaN
10,000 Quotes DB (Premium)                          1.0     ...               NaN
100 Doors of Revenge                                1.0     ...               NaN
100+ C Programs                                     1.0     ...               NaN
100000+ Messages - DP, Status, Jokes & GIF 2018     1.0     ...               NaN
101 C Programming Problems                          1.0     ...               NaN
104 Looking for a job - looking for a job, look...  1.0     ...               NaN
11st                                                1.0     ...               NaN
12 Step Meditations & Sober Prayers AA NA AL-ANON   1.0     ...               NaN
14thStreetVet                                       1.0     ...               NaN
17th Edition Cable Sizer                            1.0     ...               NaN
1800 Contacts - Lens Store                          2.0     ...               NaN
1LINE – One Line with One Touch                     1.0     ...               NaN
1st Fed CI Mobile Banking                           1.0     ...               NaN
2 Amateur ham radio CW Morse code practice keys TX  1.0     ...               NaN
2-Player Co-op Zombie Shoot                         1.0     ...               NaN
20 Minuten (CH)                                     1.0     ...               NaN
20 minutes (CH)                                     1.0     ...               NaN
2000 AD Comics and Judge Dredd                      1.0     ...               NaN
2017 BN SM Sales Conference                         1.0     ...               NaN
...                                                 ...     ...               ...
4.0.3 and up                                        NaN     ...            1501.0
4.4 and up                                          NaN     ...             980.0
2.3 and up                                          NaN     ...             652.0
5.0 and up                                          NaN     ...             601.0
4.2 and up                                          NaN     ...             394.0
2.3.3 and up                                        NaN     ...             281.0
2.2 and up                                          NaN     ...             244.0
4.3 and up                                          NaN     ...             243.0
3.0 and up                                          NaN     ...             241.0
2.1 and up                                          NaN     ...             134.0
1.6 and up                                          NaN     ...             116.0
6.0 and up                                          NaN     ...              60.0
7.0 and up                                          NaN     ...              42.0
3.2 and up                                          NaN     ...              36.0
2.0 and up                                          NaN     ...              32.0
5.1 and up                                          NaN     ...              24.0
1.5 and up                                          NaN     ...              20.0
4.4W and up                                         NaN     ...              12.0
3.1 and up                                          NaN     ...              10.0
2.0.1 and up                                        NaN     ...               7.0
8.0 and up                                          NaN     ...               6.0
7.1 and up                                          NaN     ...               3.0
1.0 and up                                          NaN     ...               2.0
5.0 - 8.0                                           NaN     ...               2.0
4.0.3 - 7.1.1                                       NaN     ...               2.0
5.0 - 7.1.1                                         NaN     ...               1.0
2.2 - 7.1.1                                         NaN     ...               1.0
5.0 - 6.0                                           NaN     ...               1.0
7.0 - 7.1.1                                         NaN     ...               1.0
4.1 - 7.1.1                                         NaN     ...               1.0

[20621 rows x 13 columns]
>>> df[col]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    df[col]
NameError: name 'col' is not defined
>>> df
                                                          App         ...                 Android Ver
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df[columns]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    df[columns]
NameError: name 'columns' is not defined
>>> df.index.name = 'No.'
>>> df
                                                          App         ...                 Android Ver
No.                                                                   ...                            
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df.columns
Index(['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
       'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
       'Android Ver'],
      dtype='object')
>>> df[1,:]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    df[1,:]
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 2487, in _get_item_cache
    res = cache.get(item)
TypeError: unhashable type: 'slice'
>>> df.iloc[0,0]
'Photo Editor & Candy Camera & Grid & ScrapBook'
>>> df.iloc[0,:]
App               Photo Editor & Candy Camera & Grid & ScrapBook
Category                                          ART_AND_DESIGN
Rating                                                       4.1
Reviews                                                      159
Size                                                         19M
Installs                                                 10,000+
Type                                                        Free
Price                                                          0
Content Rating                                          Everyone
Genres                                              Art & Design
Last Updated                                     January 7, 2018
Current Ver                                                1.0.0
Android Ver                                         4.0.3 and up
Name: 1900-01-30 00:00:00, dtype: object
>>> s.iloc[0]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.iloc[0]
AttributeError: 'numpy.ndarray' object has no attribute 'iloc'
>>> s.loc[0]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.loc[0]
AttributeError: 'numpy.ndarray' object has no attribute 'loc'
>>> df
                                                          App         ...                 Android Ver
No.                                                                   ...                            
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> s.columns
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.columns
AttributeError: 'numpy.ndarray' object has no attribute 'columns'
>>> s
array([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> s = pd.Series(s)
>>> s
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.iloc[0]
0
>>> s.loc[0]
0
>>> s.columns
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s.columns
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4372, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'columns'
>>> s.columns = ['order
		 
SyntaxError: EOL while scanning string literal
>>> s.columns = ['order']
		 
>>> s
		 
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.index.name='series'
		 
>>> s
		 
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.isnull()
		 
series
0    False
1    False
2    False
3    False
4    False
5    False
6    False
7    False
8    False
dtype: bool
>>> s.notnull()
		 
series
0    True
1    True
2    True
3    True
4    True
5    True
6    True
7    True
8    True
dtype: bool
>>> s.columns=['a']
		 
>>> s
		 
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.dropna()
		 
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s
		 
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.isnull()
		 
series
0    False
1    False
2    False
3    False
4    False
5    False
6    False
7    False
8    False
dtype: bool
>>> s.dropna(axis=1)
		 
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.dropna(axis=1)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 3891, in dropna
    axis = self._get_axis_number(axis or 0)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 375, in _get_axis_number
    .format(axis, type(self)))
ValueError: No axis named 1 for object type <class 'pandas.core.series.Series'>
>>> s.columns.name = 'no.'
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.columns.name = 'no.'
AttributeError: 'list' object has no attribute 'name'
>>> s.columns
['a']
>>> s.columns = 'a'
>>> s
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.dropna(axis=a)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.dropna(axis=a)
NameError: name 'a' is not defined
>>> df.dropna(axis=1)
                                                          App         ...                Last Updated
No.                                                                   ...                            
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...             January 7, 2018
1900-01-31                                Coloring book moana         ...            January 15, 2018
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...              August 1, 2018
1900-02-02                              Sketch - Draw & Paint         ...                June 8, 2018
1900-02-03              Pixel Draw - Number Art Coloring Book         ...               June 20, 2018
1900-02-04                         Paper flowers instructions         ...              March 26, 2017
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...              April 26, 2018
1900-02-06                                   Infinite Painter         ...               June 14, 2018
1900-02-07                               Garden Coloring Book         ...          September 20, 2017
1900-02-08                      Kids Paint Free - Drawing Fun         ...                July 3, 2018
1900-02-09                            Text on Photo - Fonteee         ...            October 27, 2017
1900-02-10            Name Art Photo Editor - Focus n Filters         ...               July 31, 2018
1900-02-11                     Tattoo Name On My Photo Editor         ...               April 2, 2018
1900-02-12                              Mandala Coloring Book         ...               June 26, 2018
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...              August 3, 2018
1900-02-14                    Learn To Draw Kawaii Characters         ...                June 6, 2018
1900-02-15       Photo Designer - Write your name with shapes         ...               July 31, 2018
1900-02-16                           350 Diy Room Decor Ideas         ...            November 7, 2017
1900-02-17                      FlipaClip - Cartoon animation         ...              August 3, 2018
1900-02-18                                       ibis Paint X         ...               July 30, 2018
1900-02-19                        Logo Maker - Small Business         ...              April 20, 2018
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...              March 20, 2018
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...               July 12, 2018
1900-02-22                             Mcqueen Coloring pages         ...               March 7, 2018
1900-02-23                        HD Mickey Minnie Wallpapers         ...                July 7, 2018
1900-02-24                         Harley Quinn wallpapers HD         ...              April 25, 2018
1900-02-25                      Colorfit - Drawing & Coloring         ...            October 11, 2017
1900-02-26                              Animated Photo Editor         ...              March 21, 2018
1900-02-27                              Pencil Sketch Drawing         ...               July 12, 2018
1900-02-28                    Easy Realistic Drawing Tutorial         ...             August 22, 2017
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...               July 24, 2018
1929-09-07                                      Fr Agnel Pune         ...               June 13, 2018
1929-09-08                                     DICT.fr Mobile         ...               July 17, 2018
1929-09-09                               FR: My Secret Pets!          ...                June 3, 2015
1929-09-10                          Golden Dictionary (FR-AR)         ...               July 19, 2018
1929-09-11                                 FieldBi FR Offline         ...              August 6, 2018
1929-09-12                               HTC Sense Input - FR         ...            October 30, 2015
1929-09-13                               Gold Quote - Gold.fr         ...                May 19, 2016
1929-09-14                                          Fanfic-FR         ...              August 5, 2017
1929-09-15                                    Fr. Daoud Lamei         ...               June 27, 2018
1929-09-16                                            Poop FR         ...                May 29, 2018
1929-09-17                                          PLMGSS FR         ...            December 1, 2017
1929-09-18                                       List iptv FR         ...              April 22, 2018
1929-09-19                                          Cardio-FR         ...               July 31, 2018
1929-09-20                                 Naruto & Boruto FR         ...            February 2, 2018
1929-09-21          Frim: get new friends on local chat rooms         ...              March 23, 2018
1929-09-22                                 Fr Agnel Ambarnath         ...               June 13, 2018
1929-09-23                            Manga-FR - Anime Vostfr         ...                May 15, 2017
1929-09-24                     Bulgarian French Dictionary Fr         ...               June 19, 2016
1929-09-25                                  News Minecraft.fr         ...            January 20, 2014
1929-09-26                           payermonstationnement.fr         ...               June 13, 2018
1929-09-27                                           FR Tides         ...           February 16, 2014
1929-09-28                                        Chemin (fr)         ...              March 23, 2014
1929-09-29                                      FR Calculator         ...               June 18, 2017
1929-09-30                                           FR Forms         ...          September 29, 2016
1929-10-01                                   Sya9a Maroc - FR         ...               July 25, 2017
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                July 6, 2018
1929-10-03                             Parkinson Exercices FR         ...            January 20, 2017
1929-10-04                      The SCP Foundation DB fr nn5n         ...            January 19, 2015
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...               July 25, 2018

[10841 rows x 8 columns]
>>> s
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.fillna(s.mean())
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.astype()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s.astype()
  File "C:\python 3.6.5\lib\site-packages\pandas\util\_decorators.py", line 178, in wrapper
    return func(*args, **kwargs)
TypeError: astype() missing 1 required positional argument: 'dtype'
>>> s.dtype()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.dtype()
TypeError: 'numpy.dtype' object is not callable
>>> s.astype(int)
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s.astype(float)
series
0    0.0
1    1.0
2    2.0
3    3.0
4    4.0
5    5.0
6    6.0
7    7.0
8    8.0
dtype: float64
>>>  s.drop(1)
SyntaxError: unexpected indent
>>> s.replace(1, 'one')
series
0      0
1    one
2      2
3      3
4      4
5      5
6      6
7      7
8      8
dtype: object
>>> s.replace([1,2,4],[one,two,four])
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s.replace([1,2,4],[one,two,four])
NameError: name 'one' is not defined
>>> s.replace([1,2,4],['one','two','four'])
series
0       0
1     one
2     two
3       3
4    four
5       5
6       6
7       7
8       8
dtype: object
>>> df.rename(columns=lambda x:x+1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    df.rename(columns=lambda x:x+1)
  File "C:\python 3.6.5\lib\site-packages\pandas\util\_decorators.py", line 187, in wrapper
    return func(*args, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 3781, in rename
    return super(DataFrame, self).rename(**kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 974, in rename
    level=level)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 3340, in rename_axis
    obj.set_axis(axis, _transform_index(self.axes[axis], mapper, level))
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 5298, in _transform_index
    items = [func(x) for x in index]
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 5298, in <listcomp>
    items = [func(x) for x in index]
  File "<pyshell#81>", line 1, in <lambda>
    df.rename(columns=lambda x:x+1)
TypeError: must be str, not int
>>> df
                                                          App         ...                 Android Ver
No.                                                                   ...                            
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df.head(2)
                                                       App      ...        Android Ver
No.                                                             ...                   
1900-01-30  Photo Editor & Candy Camera & Grid & ScrapBook      ...       4.0.3 and up
1900-01-31                             Coloring book moana      ...       4.0.3 and up

[2 rows x 13 columns]
>>> df.rename(columns={'App':'Name_app'})
                                                     Name_app         ...                 Android Ver
No.                                                                   ...                            
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df
                                                          App         ...                 Android Ver
No.                                                                   ...                            
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df.set_index('lodaa')
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'lodaa'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    df.set_index('lodaa')
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 3909, in set_index
    level = frame[col]._values
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'lodaa'
>>> df[df[col]>1]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    df[df[col]>1]
NameError: name 'col' is not defined
>>> df.columns > 1
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    df.columns > 1
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 104, in cmp_method
    result = ops._comp_method_OBJECT_ARRAY(op, self.values, other)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\ops.py", line 1122, in _comp_method_OBJECT_ARRAY
    result = libops.scalar_compare(x, y, op)
  File "pandas\_libs\ops.pyx", line 98, in pandas._libs.ops.scalar_compare
TypeError: '>' not supported between instances of 'str' and 'int'
>>> df = df[df.columns > 1]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    df = df[df.columns > 1]
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexes\base.py", line 104, in cmp_method
    result = ops._comp_method_OBJECT_ARRAY(op, self.values, other)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\ops.py", line 1122, in _comp_method_OBJECT_ARRAY
    result = libops.scalar_compare(x, y, op)
  File "pandas\_libs\ops.pyx", line 98, in pandas._libs.ops.scalar_compare
TypeError: '>' not supported between instances of 'str' and 'int'
>>> df.sort_values(App)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    df.sort_values(App)
NameError: name 'App' is not defined
>>> s.sort_values()
series
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
dtype: int32
>>> s = np.random.rand(3,3)
>>> s
array([[0.17698636, 0.45284787, 0.69486291],
       [0.21071589, 0.83148044, 0.32854294],
       [0.20609306, 0.63443266, 0.80929276]])
>>> s = pd.Series(s)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s = pd.Series(s)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 275, in __init__
    raise_cast_failure=True)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 4165, in _sanitize_array
    raise Exception('Data must be 1-dimensional')
Exception: Data must be 1-dimensional
>>> s = np.random.rand(9)
>>> s
array([0.62034879, 0.27615638, 0.38797452, 0.47145871, 0.03084843,
       0.21677562, 0.10157528, 0.04989229, 0.74903156])
>>> s = pd.Series(s)
>>> s
0    0.620349
1    0.276156
2    0.387975
3    0.471459
4    0.030848
5    0.216776
6    0.101575
7    0.049892
8    0.749032
dtype: float64
>>> s
0    0.620349
1    0.276156
2    0.387975
3    0.471459
4    0.030848
5    0.216776
6    0.101575
7    0.049892
8    0.749032
dtype: float64
>>> s.sort_values()
4    0.030848
7    0.049892
6    0.101575
5    0.216776
1    0.276156
2    0.387975
3    0.471459
0    0.620349
8    0.749032
dtype: float64
>>> s.sort_values(ascending=Flase)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s.sort_values(ascending=Flase)
NameError: name 'Flase' is not defined
>>> s.sort_values(ascending=False)
8    0.749032
0    0.620349
3    0.471459
2    0.387975
1    0.276156
5    0.216776
6    0.101575
7    0.049892
4    0.030848
dtype: float64
>>> s.astype(int)
0    0
1    0
2    0
3    0
4    0
5    0
6    0
7    0
8    0
dtype: int32
>>> s.ceil()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s.ceil()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'ceil'
>>> s[s[col]>0.23]
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    s[s[col]>0.23]
NameError: name 'col' is not defined
>>> s = s.index.name('order')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    s = s.index.name('order')
TypeError: 'NoneType' object is not callable
>>> s.index.name('S')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    s.index.name('S')
TypeError: 'NoneType' object is not callable
>>> s.index.name = 'S'
>>> s
S
0    0.620349
1    0.276156
2    0.387975
3    0.471459
4    0.030848
5    0.216776
6    0.101575
7    0.049892
8    0.749032
dtype: float64
>>> s.columns
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    s.columns
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4372, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'columns'
>>> s.columns()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    s.columns()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4372, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'columns'
>>> s.columns = ['S','A']
>>> s
S
0    0.620349
1    0.276156
2    0.387975
3    0.471459
4    0.030848
5    0.216776
6    0.101575
7    0.049892
8    0.749032
dtype: float64
>>> s.columns()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    s.columns()
TypeError: 'list' object is not callable
>>> s.rename(columns={'A':'B'})
S
0    0.620349
1    0.276156
2    0.387975
3    0.471459
4    0.030848
5    0.216776
6    0.101575
7    0.049892
8    0.749032
dtype: float64
>>> df.groupby(col)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    df.groupby(col)
NameError: name 'col' is not defined
>>> df.groupby(App)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    df.groupby(App)
NameError: name 'App' is not defined
>>> df
                                                          App         ...                 Android Ver
No.                                                                   ...                            
1900-01-30     Photo Editor & Candy Camera & Grid & ScrapBook         ...                4.0.3 and up
1900-01-31                                Coloring book moana         ...                4.0.3 and up
1900-02-01  U Launcher Lite – FREE Live Cool Themes, Hide ...         ...                4.0.3 and up
1900-02-02                              Sketch - Draw & Paint         ...                  4.2 and up
1900-02-03              Pixel Draw - Number Art Coloring Book         ...                  4.4 and up
1900-02-04                         Paper flowers instructions         ...                  2.3 and up
1900-02-05            Smoke Effect Photo Maker - Smoke Editor         ...                4.0.3 and up
1900-02-06                                   Infinite Painter         ...                  4.2 and up
1900-02-07                               Garden Coloring Book         ...                  3.0 and up
1900-02-08                      Kids Paint Free - Drawing Fun         ...                4.0.3 and up
1900-02-09                            Text on Photo - Fonteee         ...                  4.1 and up
1900-02-10            Name Art Photo Editor - Focus n Filters         ...                  4.0 and up
1900-02-11                     Tattoo Name On My Photo Editor         ...                  4.1 and up
1900-02-12                              Mandala Coloring Book         ...                  4.4 and up
1900-02-13    3D Color Pixel by Number - Sandbox Art Coloring         ...                  2.3 and up
1900-02-14                    Learn To Draw Kawaii Characters         ...                  4.2 and up
1900-02-15       Photo Designer - Write your name with shapes         ...                  4.1 and up
1900-02-16                           350 Diy Room Decor Ideas         ...                  2.3 and up
1900-02-17                      FlipaClip - Cartoon animation         ...                4.0.3 and up
1900-02-18                                       ibis Paint X         ...                  4.1 and up
1900-02-19                        Logo Maker - Small Business         ...                  4.1 and up
1900-02-20          Boys Photo Editor - Six Pack & Men's Suit         ...                4.0.3 and up
1900-02-21            Superheroes Wallpapers | 4K Backgrounds         ...                4.0.3 and up
1900-02-22                             Mcqueen Coloring pages         ...                  4.1 and up
1900-02-23                        HD Mickey Minnie Wallpapers         ...                  4.1 and up
1900-02-24                         Harley Quinn wallpapers HD         ...                  3.0 and up
1900-02-25                      Colorfit - Drawing & Coloring         ...                4.0.3 and up
1900-02-26                              Animated Photo Editor         ...                4.0.3 and up
1900-02-27                              Pencil Sketch Drawing         ...                  2.3 and up
1900-02-28                    Easy Realistic Drawing Tutorial         ...                  2.3 and up
...                                                       ...         ...                         ...
1929-09-06                                        FR Plus 1.6         ...                 4.4W and up
1929-09-07                                      Fr Agnel Pune         ...                4.0.3 and up
1929-09-08                                     DICT.fr Mobile         ...                  4.1 and up
1929-09-09                               FR: My Secret Pets!          ...                  3.0 and up
1929-09-10                          Golden Dictionary (FR-AR)         ...                  4.2 and up
1929-09-11                                 FieldBi FR Offline         ...                  4.1 and up
1929-09-12                               HTC Sense Input - FR         ...                  5.0 and up
1929-09-13                               Gold Quote - Gold.fr         ...                  2.2 and up
1929-09-14                                          Fanfic-FR         ...                  4.1 and up
1929-09-15                                    Fr. Daoud Lamei         ...                  4.1 and up
1929-09-16                                            Poop FR         ...                4.0.3 and up
1929-09-17                                          PLMGSS FR         ...                  4.4 and up
1929-09-18                                       List iptv FR         ...                4.0.3 and up
1929-09-19                                          Cardio-FR         ...                  4.4 and up
1929-09-20                                 Naruto & Boruto FR         ...                  4.0 and up
1929-09-21          Frim: get new friends on local chat rooms         ...          Varies with device
1929-09-22                                 Fr Agnel Ambarnath         ...                4.0.3 and up
1929-09-23                            Manga-FR - Anime Vostfr         ...                  4.0 and up
1929-09-24                     Bulgarian French Dictionary Fr         ...                  4.1 and up
1929-09-25                                  News Minecraft.fr         ...                  1.6 and up
1929-09-26                           payermonstationnement.fr         ...                  4.0 and up
1929-09-27                                           FR Tides         ...                  2.1 and up
1929-09-28                                        Chemin (fr)         ...                  2.2 and up
1929-09-29                                      FR Calculator         ...                  4.1 and up
1929-09-30                                           FR Forms         ...                  4.0 and up
1929-10-01                                   Sya9a Maroc - FR         ...                  4.1 and up
1929-10-02                   Fr. Mike Schmitz Audio Teachings         ...                  4.1 and up
1929-10-03                             Parkinson Exercices FR         ...                  2.2 and up
1929-10-04                      The SCP Foundation DB fr nn5n         ...          Varies with device
1929-10-05      iHoroscope - 2018 Daily Horoscope & Astrology         ...          Varies with device

[10841 rows x 13 columns]
>>> df.apply(np.mean)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
ValueError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 825, in _ensure_numeric
    x = complex(x)
ValueError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 128, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 828, in _ensure_numeric
    .format(value=x))
TypeError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
ValueError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 825, in _ensure_numeric
    x = complex(x)
ValueError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\idlelib\run.py", line 474, in runcode
    exec(code, self.locals)
  File "<pyshell#119>", line 1, in <module>
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6014, in apply
    return op.get_result()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 318, in get_result
    return super(FrameRowApply, self).get_result()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 142, in get_result
    return self.apply_standard()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 248, in apply_standard
    self.apply_series_generator()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 277, in apply_series_generator
    results[i] = self.f(v)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\fromnumeric.py", line 2917, in mean
    return mean(axis=axis, dtype=dtype, out=out, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 9613, in stat_func
    numeric_only=numeric_only)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 3221, in _reduce
    return op(delegate, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 77, in _f
    return f(*args, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 131, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 828, in _ensure_numeric
    .format(value=x))
TypeError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\idlelib\run.py", line 144, in main
    ret = method(*args, **kwargs)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 486, in runcode
    print_exception()
  File "C:\python 3.6.5\lib\idlelib\run.py", line 234, in print_exception
    print_exc(typ, val, tb)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  [Previous line repeated 1 more times]
  File "C:\python 3.6.5\lib\idlelib\run.py", line 232, in print_exc
    print(line, end='', file=efile)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 604, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 216, in remotecall
    return self.asyncreturn(seq)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 247, in asyncreturn
    return self.decoderesponse(response)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 267, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 4243-4243: Non-BMP character not supported in Tk

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\idlelib\run.py", line 158, in main
    print_exception()
  File "C:\python 3.6.5\lib\idlelib\run.py", line 234, in print_exception
    print_exc(typ, val, tb)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  [Previous line repeated 2 more times]
  File "C:\python 3.6.5\lib\idlelib\run.py", line 232, in print_exc
    print(line, end='', file=efile)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 604, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 216, in remotecall
    return self.asyncreturn(seq)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 247, in asyncreturn
    return self.decoderesponse(response)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 267, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 4243-4243: Non-BMP character not supported in Tk

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "C:\python 3.6.5\lib\idlelib\run.py", line 162, in main
    traceback.print_exception(type, value, tb, file=sys.__stderr__)
  File "C:\python 3.6.5\lib\traceback.py", line 101, in print_exception
    print(line, file=file, end="")
  File "C:\python 3.6.5\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 604, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 216, in remotecall
    return self.asyncreturn(seq)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 247, in asyncreturn
    return self.decoderesponse(response)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 267, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 4243-4243: Non-BMP character not supported in Tk

=============================== RESTART: Shell ===============================
>>> df.apply(np.max)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    df.apply(np.max)
NameError: name 'df' is not defined
>>> import numpy as np
>>> import pandas as pd
>>> df = pd.read_csv('googleplaystore.csv')
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    df = pd.read_csv('googleplaystore.csv')
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\python 3.6.5\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'googleplaystore.csv' does not exist
>>> df = pd.read_csv('G:\github\Pandas\PlayStoreDataSet\googleplaystore.csv')
>>> df.apply(np.max)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 128, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 507, in reduction
    result = getattr(values, meth)(axis)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 28, in _amax
    return umr_maximum(a, axis, None, out, keepdims, initial)
TypeError: '>=' not supported between instances of 'str' and 'float'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    df.apply(np.max)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6014, in apply
    return op.get_result()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 318, in get_result
    return super(FrameRowApply, self).get_result()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 142, in get_result
    return self.apply_standard()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 248, in apply_standard
    self.apply_series_generator()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 277, in apply_series_generator
    results[i] = self.f(v)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\fromnumeric.py", line 2334, in amax
    initial=initial)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\fromnumeric.py", line 81, in _wrapreduction
    return reduction(axis=axis, out=out, **passkwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 9613, in stat_func
    numeric_only=numeric_only)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 3221, in _reduce
    return op(delegate, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 131, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 507, in reduction
    result = getattr(values, meth)(axis)
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 28, in _amax
    return umr_maximum(a, axis, None, out, keepdims, initial)
TypeError: ("'>=' not supported between instances of 'str' and 'float'", 'occurred at index Type')
>>> s = np.arange(19)
>>> s
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18])
>>> s = np.random.randn(25)*1.5
>>> s
array([-1.43517603,  1.7897998 , -0.57984145, -0.82848578, -1.81219931,
        2.15534924,  0.32526981, -0.0194522 , -0.25220568, -0.18690554,
       -0.62882016,  1.58809615,  0.94444034, -1.69209021, -0.0257866 ,
        0.84353198,  0.26171388, -0.91228429,  1.23743787, -0.93253005,
        1.75677506, -1.08509297, -0.18016359, -0.10346378,  0.94897029])
>>> s*
SyntaxError: invalid syntax
>>> s*0
array([-0.,  0., -0., -0., -0.,  0.,  0., -0., -0., -0., -0.,  0.,  0.,
       -0., -0.,  0.,  0., -0.,  0., -0.,  0., -0., -0., -0.,  0.])
>>> s
array([-1.43517603,  1.7897998 , -0.57984145, -0.82848578, -1.81219931,
        2.15534924,  0.32526981, -0.0194522 , -0.25220568, -0.18690554,
       -0.62882016,  1.58809615,  0.94444034, -1.69209021, -0.0257866 ,
        0.84353198,  0.26171388, -0.91228429,  1.23743787, -0.93253005,
        1.75677506, -1.08509297, -0.18016359, -0.10346378,  0.94897029])
>>> s = pd.series(s)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    s = pd.series(s)
AttributeError: module 'pandas' has no attribute 'series'
>>> s= pd.Series(s)
>>> s
0    -1.435176
1     1.789800
2    -0.579841
3    -0.828486
4    -1.812199
5     2.155349
6     0.325270
7    -0.019452
8    -0.252206
9    -0.186906
10   -0.628820
11    1.588096
12    0.944440
13   -1.692090
14   -0.025787
15    0.843532
16    0.261714
17   -0.912284
18    1.237438
19   -0.932530
20    1.756775
21   -1.085093
22   -0.180164
23   -0.103464
24    0.948970
dtype: float64
>>> s.apply(np.max())
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    s.apply(np.max())
TypeError: amax() missing 1 required positional argument: 'a'
>>> s.apply(np.max)
0    -1.435176
1     1.789800
2    -0.579841
3    -0.828486
4    -1.812199
5     2.155349
6     0.325270
7    -0.019452
8    -0.252206
9    -0.186906
10   -0.628820
11    1.588096
12    0.944440
13   -1.692090
14   -0.025787
15    0.843532
16    0.261714
17   -0.912284
18    1.237438
19   -0.932530
20    1.756775
21   -1.085093
22   -0.180164
23   -0.103464
24    0.948970
dtype: float64
>>> s.apply(np.mean)
0    -1.435176
1     1.789800
2    -0.579841
3    -0.828486
4    -1.812199
5     2.155349
6     0.325270
7    -0.019452
8    -0.252206
9    -0.186906
10   -0.628820
11    1.588096
12    0.944440
13   -1.692090
14   -0.025787
15    0.843532
16    0.261714
17   -0.912284
18    1.237438
19   -0.932530
20    1.756775
21   -1.085093
22   -0.180164
23   -0.103464
24    0.948970
dtype: float64
>>> s
0    -1.435176
1     1.789800
2    -0.579841
3    -0.828486
4    -1.812199
5     2.155349
6     0.325270
7    -0.019452
8    -0.252206
9    -0.186906
10   -0.628820
11    1.588096
12    0.944440
13   -1.692090
14   -0.025787
15    0.843532
16    0.261714
17   -0.912284
18    1.237438
19   -0.932530
20    1.756775
21   -1.085093
22   -0.180164
23   -0.103464
24    0.948970
dtype: float64
>>> s.apply(np.max, axis=0)
0    -1.435176
1     1.789800
2    -0.579841
3    -0.828486
4    -1.812199
5     2.155349
6     0.325270
7    -0.019452
8    -0.252206
9    -0.186906
10   -0.628820
11    1.588096
12    0.944440
13   -1.692090
14   -0.025787
15    0.843532
16    0.261714
17   -0.912284
18    1.237438
19   -0.932530
20    1.756775
21   -1.085093
22   -0.180164
23   -0.103464
24    0.948970
dtype: float64
>>> s.describe
<bound method NDFrame.describe of 0    -1.435176
1     1.789800
2    -0.579841
3    -0.828486
4    -1.812199
5     2.155349
6     0.325270
7    -0.019452
8    -0.252206
9    -0.186906
10   -0.628820
11    1.588096
12    0.944440
13   -1.692090
14   -0.025787
15    0.843532
16    0.261714
17   -0.912284
18    1.237438
19   -0.932530
20    1.756775
21   -1.085093
22   -0.180164
23   -0.103464
24    0.948970
dtype: float64>
>>> s.head()
0   -1.435176
1    1.789800
2   -0.579841
3   -0.828486
4   -1.812199
dtype: float64
>>> s.shape
(25,)
>>> s.describe
<bound method NDFrame.describe of 0    -1.435176
1     1.789800
2    -0.579841
3    -0.828486
4    -1.812199
5     2.155349
6     0.325270
7    -0.019452
8    -0.252206
9    -0.186906
10   -0.628820
11    1.588096
12    0.944440
13   -1.692090
14   -0.025787
15    0.843532
16    0.261714
17   -0.912284
18    1.237438
19   -0.932530
20    1.756775
21   -1.085093
22   -0.180164
23   -0.103464
24    0.948970
dtype: float64>
>>> s.info
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    s.info
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'info'
>>> s.info()
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    s.info()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'info'
>>> s.describe()
count    25.000000
mean      0.047075
std       1.122840
min      -1.812199
25%      -0.828486
50%      -0.103464
75%       0.944440
max       2.155349
dtype: float64
>>> s.value_counts(dropna=False)
 0.325270    1
-1.085093    1
-1.692090    1
-0.828486    1
 0.843532    1
-0.019452    1
 2.155349    1
-0.025787    1
-1.812199    1
 0.948970    1
-0.912284    1
-0.932530    1
 1.237438    1
 1.588096    1
-0.579841    1
-0.180164    1
-1.435176    1
 0.261714    1
-0.186906    1
-0.628820    1
-0.103464    1
 0.944440    1
 1.789800    1
-0.252206    1
 1.756775    1
dtype: int64
>>> s1 = np.arange(25)
>>> s1 = pd.Series(s1)
>>> s.append(s1)
0     -1.435176
1      1.789800
2     -0.579841
3     -0.828486
4     -1.812199
5      2.155349
6      0.325270
7     -0.019452
8     -0.252206
9     -0.186906
10    -0.628820
11     1.588096
12     0.944440
13    -1.692090
14    -0.025787
15     0.843532
16     0.261714
17    -0.912284
18     1.237438
19    -0.932530
20     1.756775
21    -1.085093
22    -0.180164
23    -0.103464
24     0.948970
0      0.000000
1      1.000000
2      2.000000
3      3.000000
4      4.000000
5      5.000000
6      6.000000
7      7.000000
8      8.000000
9      9.000000
10    10.000000
11    11.000000
12    12.000000
13    13.000000
14    14.000000
15    15.000000
16    16.000000
17    17.000000
18    18.000000
19    19.000000
20    20.000000
21    21.000000
22    22.000000
23    23.000000
24    24.000000
dtype: float64
>>> s1.dropna(axis=1)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    s1.dropna(axis=1)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 3891, in dropna
    axis = self._get_axis_number(axis or 0)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 375, in _get_axis_number
    .format(axis, type(self)))
ValueError: No axis named 1 for object type <class 'pandas.core.series.Series'>
>>> s1.dropna()
0      0
1      1
2      2
3      3
4      4
5      5
6      6
7      7
8      8
9      9
10    10
11    11
12    12
13    13
14    14
15    15
16    16
17    17
18    18
19    19
20    20
21    21
22    22
23    23
24    24
dtype: int32
>>> s.iloc[5,:]
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    s.iloc[5,:]
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexing.py", line 1472, in __getitem__
    return self._getitem_tuple(key)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexing.py", line 2013, in _getitem_tuple
    self._has_valid_tuple(tup)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\indexing.py", line 220, in _has_valid_tuple
    raise IndexingError('Too many indexers')
pandas.core.indexing.IndexingError: Too many indexers
>>> s.iloc[5]
2.1553492351614807
>>> s1.iloc[5]
5
>>> s1.iloc[5] +=5
>>> s1
0      0
1      1
2      2
3      3
4      4
5     10
6      6
7      7
8      8
9      9
10    10
11    11
12    12
13    13
14    14
15    15
16    16
17    17
18    18
19    19
20    20
21    21
22    22
23    23
24    24
dtype: int32
>>> s1
0      0
1      1
2      2
3      3
4      4
5     10
6      6
7      7
8      8
9      9
10    10
11    11
12    12
13    13
14    14
15    15
16    16
17    17
18    18
19    19
20    20
21    21
22    22
23    23
24    24
dtype: int32
>>> s.concat([s,  s1], axis=1)
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    s.concat([s,  s1], axis=1)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'concat'
>>> df.mean()
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 128, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6866, in _reduce
    result = f(values)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6857, in f
    return op(x, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 77, in _f
    return f(*args, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 131, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 128, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6866, in _reduce
    result = f(values)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6857, in f
    return op(x, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 77, in _f
    return f(*args, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 131, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 128, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6866, in _reduce
    result = f(values)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6857, in f
    return op(x, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 77, in _f
    return f(*args, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 131, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 128, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6866, in _reduce
    result = f(values)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6857, in f
    return op(x, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 77, in _f
    return f(*args, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 131, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\numpy\core\_methods.py", line 36, in _sum
    return umr_sum(a, axis, dtype, out, keepdims, initial)
TypeError: must be str, not int

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric
    x = float(x)
ValueError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 825, in _ensure_numeric
    x = complex(x)
ValueError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 128, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 355, in nanmean
    the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 828, in _ensure_numeric
    .format(value=x))
TypeError: 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\idlelib\run.py", line 474, in runcode
    exec(code, self.locals)
  File "<pyshell#161>", line 1, in <module>
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 9613, in stat_func
    numeric_only=numeric_only)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6893, in _reduce
    result = opa.get_result()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 318, in get_result
    return super(FrameRowApply, self).get_result()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 142, in get_result
    return self.apply_standard()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 248, in apply_standard
    self.apply_series_generator()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\apply.py", line 264, in apply_series_generator
    results[i] = self.f(v)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\frame.py", line 6857, in f
    return op(x, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 77, in _f
    return f(*args, **kwargs)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 131, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 345, in nanmean
    values, mask, dtype, dtype_max = _get_values(values, skipna, 0)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\nanops.py", line 208, in _get_values
    values = com._values_from_object(values)
  File "pandas\_libs\lib.pyx", line 47, in pandas._libs.lib.values_from_object
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 478, in get_values
    return self._data.get_values()
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\idlelib\run.py", line 144, in main
    ret = method(*args, **kwargs)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 486, in runcode
    print_exception()
  File "C:\python 3.6.5\lib\idlelib\run.py", line 234, in print_exception
    print_exc(typ, val, tb)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 232, in print_exc
    print(line, end='', file=efile)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 604, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 216, in remotecall
    return self.asyncreturn(seq)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 247, in asyncreturn
    return self.decoderesponse(response)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 267, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 4243-4243: Non-BMP character not supported in Tk

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\python 3.6.5\lib\idlelib\run.py", line 158, in main
    print_exception()
  File "C:\python 3.6.5\lib\idlelib\run.py", line 234, in print_exception
    print_exc(typ, val, tb)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 220, in print_exc
    print_exc(type(context), context, context.__traceback__)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 232, in print_exc
    print(line, end='', file=efile)
  File "C:\python 3.6.5\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 604, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 216, in remotecall
    return self.asyncreturn(seq)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 247, in asyncreturn
    return self.decoderesponse(response)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 267, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 4243-4243: Non-BMP character not supported in Tk

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "C:\python 3.6.5\lib\idlelib\run.py", line 162, in main
    traceback.print_exception(type, value, tb, file=sys.__stderr__)
  File "C:\python 3.6.5\lib\traceback.py", line 101, in print_exception
    print(line, file=file, end="")
  File "C:\python 3.6.5\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 604, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 216, in remotecall
    return self.asyncreturn(seq)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 247, in asyncreturn
    return self.decoderesponse(response)
  File "C:\python 3.6.5\lib\idlelib\rpc.py", line 267, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 4243-4243: Non-BMP character not supported in Tk

=============================== RESTART: Shell ===============================
>>> import np as np
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    import np as np
ModuleNotFoundError: No module named 'np'
>>> import numpy as np
>>> import pandas as pd
>>> s = np.random.rand(55)
>>> s=pd.Series(s)
>>> s
0     0.762796
1     0.374948
2     0.702472
3     0.629700
4     0.820217
5     0.981927
6     0.444456
7     0.016261
8     0.765236
9     0.988749
10    0.185646
11    0.644343
12    0.921011
13    0.423123
14    0.794909
15    0.622529
16    0.561595
17    0.780424
18    0.883266
19    0.786529
20    0.493607
21    0.419200
22    0.229732
23    0.244125
24    0.224923
25    0.344352
26    0.468797
27    0.280408
28    0.409025
29    0.026320
30    0.970004
31    0.816752
32    0.447021
33    0.258095
34    0.984517
35    0.791224
36    0.804341
37    0.707359
38    0.888883
39    0.490567
40    0.812171
41    0.185579
42    0.579655
43    0.854856
44    0.472045
45    0.391237
46    0.469752
47    0.366004
48    0.160473
49    0.016543
50    0.710767
51    0.399436
52    0.771521
53    0.244010
54    0.114868
dtype: float64
>>> s.mean()
0.5443328673556066
>>> s1=np.random.randint(5)
>>> s1
2
>>> s1=np.random.randint(5,size=3)
>>> s1
array([1, 0, 1])
>>>  s1=np.random.randint(5,size=5)
SyntaxError: unexpected indent
>>> s1=np.random.randint(5,size=5)
>>> s1
array([4, 3, 4, 2, 4])
>>> s1
array([4, 3, 4, 2, 4])
>>> s1.mean()
3.4
>>> s1=pd.Series(s1)
>>> s1
0    4
1    3
2    4
3    2
4    4
dtype: int32
>>> s1.mean()
3.4
>>> s1.max()
4
>>> s1.min()
2
>>> s1.corr()
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    s1.corr()
TypeError: corr() missing 1 required positional argument: 'other'
>>> s1.corr(other)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    s1.corr(other)
NameError: name 'other' is not defined
>>> s1.desscribe()
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    s1.desscribe()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'desscribe'
>>> s1.describe()
count    5.000000
mean     3.400000
std      0.894427
min      2.000000
25%      3.000000
50%      4.000000
75%      4.000000
max      4.000000
dtype: float64
>>> s1.count()
5
>>> s1.dropna()
0    4
1    3
2    4
3    2
4    4
dtype: int32
>>> s1.fillna(3)
0    4
1    3
2    4
3    2
4    4
dtype: int32
>>> s1.dropna(4)
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    s1.dropna(4)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\series.py", line 3891, in dropna
    axis = self._get_axis_number(axis or 0)
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 375, in _get_axis_number
    .format(axis, type(self)))
ValueError: No axis named 4 for object type <class 'pandas.core.series.Series'>
>>> s1.median()
4.0
>>> s1.std()
0.8944271909999159
>>> s1.var()
0.8
>>> s1.exit()
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    s1.exit()
  File "C:\python 3.6.5\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'exit'
>>> 
