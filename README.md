# Information Retrieval Lab

## Lab 1: The Inverted Index

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
<Index documents=303290 words=83225120>
...
```

### Using a pre-built index

Since indexing documents can take a lot of time, here are some already indexed files which can be renamed to `index.bin` and used directly -

| Name | Link | Size | Comments |
|------|------|------|----------|
| `index.bin` | [LINK](https://drive.google.com/open?id=0BxDMRh_L_8pOT055OVJZdXlUSjA) | 374 MB | Full indexed corpus, 303k documents |
| `index.bin.bak` | [LINK](https://drive.google.com/open?id=0BxDMRh_L_8pOYmRKU0I5MWJhbG8) | 36 MB | 25.8k documents |
