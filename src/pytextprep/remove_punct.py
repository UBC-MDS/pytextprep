def remove_punct(tweets, skip=None):
    """Remove all punctuation and special characters from the
    input tweets data

    Parameters
    ----------
    tweets : str
        Path to a text file containing tweets

    skip : array_like or None, optional
        The set of characters that do not have to be removed.
        Default is None. If None, all characters except alphabets,
        numbers and space would be removed.

    Returns
    -------
    list
        list of tweets without special characters

    Examples
    --------
    # Sample contents in tweets.txt:
    #
    # Make America Great Again! @DonaldTrump
    # It's rocket-science tier investment~~ #LoveElonMusk

    >>> remove_punct("tweets.txt")
    [
        "Make America Great Again DonaldTrump",
        "Its rocketscience tier investment LoveElonMusk"
    ]   

    >>> remove_punct("tweets.txt", skip=["'", "@", "#", '-'])
    [
        "Make America Great Again @DonaldTrump",
        "It's rocket-science tier investment #LoveElonMusk"
    ]

    """