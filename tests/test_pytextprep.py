from pytextprep import pytextprep
from pytextprep.extract_ngram import extract_ngram
from pytextprep.remove_punct import remove_punct
import numpy as np
import pandas as pd

import pytest

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
