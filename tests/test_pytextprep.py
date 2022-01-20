from pytextprep import pytextprep
from pytextprep.extract_ngram import extract_ngram
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