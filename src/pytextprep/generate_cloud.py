def generate_cloud(tweets):
    """Creates a word cloud of the most frequently occurring
    words in a group of tweets
    
    Parameters
    ----------
    tweets : str
        Path to a text file containing tweets.

    Returns
    -------
    matplotlib.container.Container
        Word cloud of most frequently occurring words

    Examples
    --------
    >>> generate_cloud("tweets.txt")
    """