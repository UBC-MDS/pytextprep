# pytextprep

This is a Python package that offers additional text preprocessing functionality specifically designed for tweets. The package bundles functions to help with cleaning and gaining insight into tweet data, providing additional resources for EDA or enabling feature engineering.

The main functions of this package are:
    1. `remove_punctuation`: Removes punctuation in a file with tweets
    2. `extract_ngram`: Extracts n-grams from a file with tweets
    3. `extract_hashtags`: Creates a list of hashtags from a file with tweets
    4. `generate_cloud`: Creates a word cloud of the most frequent words in a file with tweets

In the Python ecosystem the only popular package focused on tweet data is [tweet-preprocessor](https://pypi.org/project/tweet-preprocessor/). Even though this package is also customized specifically for dealing with Tweeter data its scope is solely oriented to tokenizing and cleaning the tweets. In contrast, our package can be leveraged to extract new features out of tweets.

## Installation

```bash
$ pip install pytextprep
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/pytextprep/blob/main/CONTRIBUTING.md). 

Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pytextprep` was created by Arijeet Chatterjee, Joshua Sia, Melisa Maidana, Philson Chan (DSCI_524_GROUP21). 

It is licensed under the terms of the MIT license.

## Credits

`pytextprep` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
