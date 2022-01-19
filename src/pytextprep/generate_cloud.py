import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords

def generate_cloud(tweets, type="words"):
    """Creates a word cloud of the most frequently occurring
    words in a group of tweets
    
    Parameters
    ----------
    tweets : list
        List of tweets.
    type : {"words", "hashtag", "stopwords"}, default="words"
        Type of content to show in wordcloud. "words" shows all words,
        "hashtag" only shows hashtags, and "stopwords" does not show
        common English words.

    Returns
    -------
    matplotlib.figure.Figure
        Word cloud of most frequently occurring words

    Examples
    --------
    >>> from pytextprep.generate_cloud import generate_cloud
    >>> import matplotlib.pyplot as plt
    >>> tweets = [
        "Make America Great Again! @DonaldTrump",
        "It's rocket-science tier investment~~ #LoveElonMusk"
    ]
    >>> tweets = ["their your down to America"]
    >>> fig = generate_cloud(tweets)
    >>> plt.show()
    """

    nltk.download("stopwords")

    # Check input argument tweets
    if not isinstance(tweets, list):
        raise TypeError("Argument tweets should be of type list.")

    # Check input argument type
    if type not in {"words", "hashtag", "stopwords"}:
        raise ValueError("Make sure the argument type is one of the accepted values")

    # Remove punctuation
    # tweets = remove_punct(tweets)

    # Convert list to string
    if type == "words":
        text = (" ".join(tweets)).lower()
    elif type == "hashtag":
        # tweets = extract_hashtags(tweets)
        text = (" ".join(tweets)).lower()
    elif type == "stopwords":
        text = (" ".join(tweets)).lower()
        text = " ".join([_ for _ in text.split() if _ not in stopwords.words("english")])

    # Generate word cloud
    wordcloud = WordCloud(max_words=50, background_color="white").generate(text)

    # Plot word cloud
    fig = plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    return fig