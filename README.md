[![ci-cd](https://github.com/UBC-MDS/pytextprep/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/pytextprep/actions/workflows/ci-cd.yml)
# pytextprep

This is a Python package that offers additional text preprocessing functionality specifically designed for tweets. The package bundles functions to help with cleaning and gaining insight into tweet data, providing additional resources for EDA or enabling feature engineering.


The main functions of this package are:

- `remove_punct` : Removes punctuation from a list of tweets
    
- `extract_ngram`: Extracts n-grams from a list of tweets
    
- `extract_hashtags`: Creates a list of hashtags from a list of tweets
    
- `generate_cloud`: Creates a word cloud of the most frequent words from a list of tweets


In the Python ecosystem the only popular package focused on tweet data is [tweet-preprocessor](https://pypi.org/project/tweet-preprocessor/). Even though this package is also customized specifically for dealing with Tweeter data its scope is solely oriented to tokenizing and cleaning the tweets. In contrast, our package can be leveraged to extract new features out of tweets.

## Installation

Install using pip: 

```bash
$ pip install pytextprep
```

Install from source:

```bash
$ git clone git@github.com:UBC-MDS/pytextprep.git
cd pytextprep
git checkout main #latest release
pip install .
```

## Usage

[Documentation](https://pytextprep.readthedocs.io/en/latest/index.html)

```python
from pytextprep.extract_ngram import extract_ngram
from pytextprep.extract_hashtags import extract_hashtags
from pytextprep.remove_punct import remove_punct
from pytextprep.generate_cloud import generate_cloud
import matplotlib.pyplot as plt

tweets_list = ["Make America Great Again! @DonalTrump", "It's a new day in #America"]
extract_ngram(tweets_list, n=3)
```

```
['Make America Great', 'America Great Again!', 'Great Again! @DonalTrump', "Again! @DonalTrump It's", "@DonalTrump It's a", "It's a new", 'a new day', 'new day in', 'day in #America']
```

```python
extract_hashtags(tweets_list)
```

```
['America']
```

```python
remove_punct(tweets_list, skip=["'", "@", "#", '-'])
```

```
['Make America Great Again @DonalTrump', "It's a new day in #America"]
```

```python
fig, wc = generate_cloud(tweets_list)
plt.show()
```

![word_cloud](https://github.com/UBC-MDS/pytextprep/blob/main/docs/word_cloud.png)

## Contributing

Contributors: Arijeet Chatterjee, Joshua Sia, Melisa Maidana, Philson Chan (DSCI_524_GROUP21).

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/pytextprep/blob/main/CONTRIBUTING.md). 

Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pytextprep` was created by Arijeet Chatterjee, Joshua Sia, Melisa Maidana, Philson Chan (DSCI_524_GROUP21). 

It is licensed under the terms of the MIT license.

## Credits

`pytextprep` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
