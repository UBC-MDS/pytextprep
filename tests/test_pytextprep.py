from pytextprep import pytextprep
from pytextprep.generate_cloud import generate_cloud
from pytextprep.extract_ngram import extract_ngram
from pytextprep.remove_punct import remove_punct
import matplotlib
import numpy as np
import pandas as pd

import pytest

def test_generate_cloud():
    """Test plotting of word cloud"""
    tweets = [
        "Make America Great Again! @DonaldTrump #America",
        "It's rocket-science tier investment~~ #LoveElonMusk",
        "America America America #USA #USA"
    ]

    expected_words = {
        'america': 1.0, 'usa': 0.4, 'make': 0.2,
        'great': 0.2, 'again': 0.2, 'donaldtrump': 0.2,
        'it': 0.2, 'rocket': 0.2, 'science': 0.2,
        'tier': 0.2, 'investment': 0.2, 'loveelonmusk': 0.2}

    expected_stopwords = {
        'america': 1.0, 'usa': 0.4, 'make': 0.2,
        'great': 0.2, 'donaldtrump': 0.2, 'rocket': 0.2,
        'science': 0.2, 'tier': 0.2, 'investment': 0.2,
        'loveelonmusk': 0.2}

    expected_hashtag = {
        'usa': 1.0, 'america': 0.5, 'loveelonmusk': 0.5}

    fig_words, wc_words = generate_cloud(tweets, type="words")
    fig_stop, wc_stop = generate_cloud(tweets, type="stopwords")
    fig_ht, wc_ht = generate_cloud(tweets, type="hashtag")

    with pytest.raises(ValueError):
        generate_cloud(tweets, type="incorrect-type")

    with pytest.raises(ValueError):
        generate_cloud([])

    with pytest.raises(ValueError):
        generate_cloud(["vaild", 3, "valid"])

    assert isinstance(fig_words, matplotlib.figure.Figure), \
        "Wrong output type"

    assert isinstance(fig_stop, matplotlib.figure.Figure), \
        "Wrong output type"

    assert isinstance(fig_ht, matplotlib.figure.Figure), \
        "Wrong output type"
    
    assert wc_words.words_ == expected_words, "Wordcloud shows words with wrong proportions"
    
    assert wc_stop.words_ == expected_stopwords, "Wordcloud (type=stopwords) shows words with wrong proportions"

    assert wc_ht.words_ == expected_hashtag, "Wordcloud (type=hashtag) shows words with wrong proportions"
    
@pytest.mark.parametrize(
    "incorrect_inputs_cloud",
    [
        1.234,
        "tweets.txt",
        dict()
    ]
)

def test_generate_cloud_error(incorrect_inputs_cloud):
    """Check TypeError raised when input argument is not a list"""
    with pytest.raises(TypeError):
        generate_cloud(incorrect_inputs_cloud)

tweets_list =["Make America Great Again DonaldTrump"]

expected_ngrams = [
    ['Make', 'America', 'Great', 'Again', 'DonaldTrump'],
    ['Make America Great', 'America Great Again', 'Great Again DonaldTrump'],
    ['Make America Great Again DonaldTrump']
]

def test_extract_ngram():
    """ Test generated ngrams from the ngram extraction function """

    actual_ngrams_1 = extract_ngram(tweets=tweets_list, n=1)
    assert actual_ngrams_1 == expected_ngrams[0], "Generated ngrams is incorrect"
    
    actual_ngrams_3 = extract_ngram(tweets=tweets_list, n=3)
    assert actual_ngrams_3 == expected_ngrams[1], "Generated ngrams is incorrect"

    actual_ngrams_5 = extract_ngram(tweets=tweets_list, n=5)
    assert actual_ngrams_5 == expected_ngrams[2], "Generated ngrams is incorrect"

@pytest.mark.parametrize(
    "incorrect_inputs_ngram",
    [
        1.234,
        "tweets.txt",
        dict()
    ]
)

def test_extract_ngram_error(incorrect_inputs_ngram):
    """ Check TypeError when input provided for extract_ngram is not of type list """
    with pytest.raises(TypeError):
        extract_ngram(tweets=incorrect_inputs_ngram, n=4)

def test_remove_punct():
    """ Test the behaviour of remove_punct function"""
    tweets_list = [
        "Make America Great Again! @DonaldTrump",
        "It's rocket-science tier investment~~ #LoveElonMusk"
    ]
    exp_out1 = [
        "Make America Great Again DonaldTrump",
        "Its rocketscience tier investment LoveElonMusk"
    ]
    exp_out2 = [
        "Make America Great Again @DonaldTrump",
        "It's rocket-science tier investment #LoveElonMusk"
    ]
    assert remove_punct(tweets_list) == exp_out1, "Punctuation not properly removed"
    assert remove_punct(tweets_list, skip=["'", "@", "#", '-']) == exp_out2, "Punctuation not properly removed"
    assert remove_punct([]) == [], "Empty lists are not handled"

    # Support numpy.ndarray & pandas.Series
    numpy_tweets = np.array(tweets_list)
    assert (remove_punct(numpy_tweets) == np.array(exp_out1)).all(), "Does not support numpy.array"
    assert (remove_punct(numpy_tweets, skip=["'", "@", "#", '-']) == np.array(exp_out2)).all(), "Does not support numpy.array"

    pd_tweets = pd.Series(tweets_list)
    assert (remove_punct(pd_tweets) == pd.Series(exp_out1)).all(), "Does not support pandas.Series"
    assert (remove_punct(pd_tweets, skip=["'", "@", "#", '-']) == pd.Series(exp_out2)).all(), "Does not support pandas.Series"
    
    # Check if supports n-dimensional array
    new_tweet_list = [
        "I'd like a cookie cutter!",
        "Tiktok harm your mind~ #SayNoToTiktok"
    ] + tweets_list
    nd_tweets = np.array(new_tweet_list).reshape(2,2)
    
    nd_exp = np.array([
        "Id like a cookie cutter",
        "Tiktok harm your mind SayNoToTiktok"
    ] + exp_out1).reshape(-1,2)
    assert (remove_punct(nd_tweets) == nd_exp).all(), "Does not support multi-dimensional array"
    
    # Check non-string list
    illegal_tweets = [
        dict(), 123.0, "string :DD"
    ]
    with pytest.raises(TypeError):
        remove_punct(illegal_tweets)