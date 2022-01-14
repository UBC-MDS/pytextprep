def generate_cloud(tweets):
    """Creates a word cloud of the most frequently occurring
    words in a group of tweets
    
    Parameters
    ----------
    tweets : array_like
        List of tweets.

    Returns
    -------
    matplotlib.container.Container
        Word cloud of most frequently occurring words

    Examples
    --------
    >>> tweets = [
        "Make America Great Again! @DonaldTrump",
        "It's rocket-science tier investment~~ #LoveElonMusk"
    ]
    >>> generate_cloud(tweets)
    """