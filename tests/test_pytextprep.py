from pytextprep import pytextprep
from pytextprep.generate_cloud import generate_cloud
import pytest
import matplotlib

def test_generate_cloud():
    """Test plotting of word cloud"""
    tweets = [
        "Make America Great Again! @DonaldTrump #America",
        "It's rocket-science tier investment~~ #LoveElonMusk",
        "America America America"
    ]

    expected_words = {
        'america': 1.0, 'make': 0.2, 'great': 0.2,
        'again': 0.2, 'donaldtrump': 0.2, 'it': 0.2,
        'rocket': 0.2, 'science': 0.2, 'tier': 0.2,
        'investment': 0.2, 'loveelonmusk': 0.2}

    expected_stopwords = {
        'america': 1.0, 'make': 0.2, 'great': 0.2,
        'donaldtrump': 0.2, 'rocket': 0.2, 'science': 0.2,
        'tier': 0.2, 'investment': 0.2, 'loveelonmusk': 0.2}

    fig_words, wc_words = generate_cloud(tweets, type="words")
    fig_stop, wc_stop = generate_cloud(tweets, type="stopwords")

    with pytest.raises(ValueError):
        generate_cloud(tweets, type="incorrect-type")

    with pytest.raises(ValueError):
        generate_cloud([])

    assert isinstance(fig_words, matplotlib.figure.Figure), \
        "Wrong output type"

    assert isinstance(fig_stop, matplotlib.figure.Figure), \
        "Wrong output type"
    
    assert wc_words.words_ == expected_words, "Wordcloud shows words with wrong proportions"
    
    assert wc_stop.words_ == expected_stopwords, "Wordcloud shows words with wrong proportions"
    
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