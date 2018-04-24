# Index Search Query

Inverted Index, Query Formulation and Ranking from Scratch in Python.

> Part of Information Retrieval Lab (Autumn 2017-18)

## Part 1: The Inverted Index

### Dataset

The dataset used for this purpose is taken from the `FIRE 2011` corpus. It can be downloaded from [here](http://www.isical.ac.in/~fire/data/docs/adhoc/en.docs.2011.tar.gpg). It contains articles from two different magazines. The methods for handling these files are present in the [`magazine_index`](magazine_index) package.

### Usage

If you wish to index all the files recursively from a directory, use the following command -

```bash
$ python lab1.py path/to/files
```

This will create an inverted index and save it to a file called `index.bin`. You can directly use this file if created already by not passing any argument to the script -

```bash
$ python lab1.py
Loading index from "index.bin"
<Index documents=392577 words=105314026>
...
```

### Using a pre-built index

Since indexing documents can take a lot of time, here are some already indexed files which can be renamed to `index.bin` and used directly -

| Name | Link | Size | Comments |
|------|------|------|----------|
| `index.bin` | [LINK](https://drive.google.com/open?id=0BxDMRh_L_8pOUzlZQ0JJMUtYd1E) | 478 MB | Full index, 392k documents |
| `index.bin.bak1` | [LINK](https://drive.google.com/file/d/0BxDMRh_L_8pObWU0ZkE1NHBTUUU/view?usp=sharing) | 374 MB | 303k documents |
| `index.bin.bak` | [LINK](https://drive.google.com/file/d/0BxDMRh_L_8pOYmRKU0I5MWJhbG8/view?usp=sharing) | 36 MB | 25.8k documents |

### Example

```bash
$ python lab_1.py
Loading index from "index.bin"
<Index documents=303290 words=83225120>
Please start entering words to get top 5 documents containing them (CTRL+C to exit) -
Enter word: market
[('1100110_calcutta_story_11965855.utf8', 58), ('1070603_calcutta_story_7858507.utf8', 31), ('1100326_opinion_story_12251777.utf8', 30), ('1050912_frontpage_story_5227346.utf8', 30), ('1040406_opinion_story_2948544.utf8', 29)]
Enter word: delhi
[('1080422_sports_ipl.utf8', 30), ('1031223_opinion_story_2710457.utf8', 28), ('1090225_sports_story_10587273.utf8', 22), ('1090812_sports_story_11351508.utf8', 21), ('1100223_sports_story_12140507.utf8', 21)]
Enter word: messi
[('1100612_sports_story_12557276.utf8', 27), ('1100527_sports_story_12492679.utf8', 17), ('1100619_sports_story_12582889.utf8', 17), ('1090529_calcutta_story_11031479.utf8', 16), ('1100613_frontpage_story_12560387.utf8', 12)]
```



## Part 2: Ranking of Documents

### Usage

You can use the pre-built index here.

```bash
$ python lab_2.py index.bin
Loading index from index.bin
Enter query: programming
en.15.66.21.2008.5.9 : 97.3490637742472
en.3.347.409.2010.2.2 : 79.64923399711134
en.3.373.142.2007.6.8 : 53.09948933140756
en.3.406.410.2007.11.18 : 48.6745318871236
en.2.296.350.2010.1.20 : 48.6745318871236
en.3.393.372.2007.9.23 : 44.24957444283963
en.3.321.344.2009.7.31 : 44.24957444283963
en.3.373.299.2007.6.11 : 44.24957444283963
en.15.109.486.2009.4.1 : 44.24957444283963
en.3.393.75.2007.9.24 : 44.24957444283963
```


---

## Development

`pipenv` is used for this project - 

```bash
$ sudo -H pip install pipenv
```

To install dependencies, simply

```bash
$ pipenv install
```

To enter a virtualenv shell

```bash
$ pipenv shell
```

This will spawn a new shell where all dependencies will be present.
