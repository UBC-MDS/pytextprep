def extract_hashtags(tweets):
    """Extracts all hashtags included in the input tweet data file
    
    Parameters
    ----------
    tweets : array_like
        List of tweets

    Returns
    -------
    list
        List of hashtags included in the tweets list
    Examples
    --------
    >>>tweets_list = [
        "Make America Great Again! @DonaldTrump",
        "It's rocket-science tier investment~~ #LoveElonMusk"
    ]
    >>>extract_hashtags(tweets_list)
    [
        "LoveElonMusk"
    ]
    """