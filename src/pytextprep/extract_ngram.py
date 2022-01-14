def extract_ngram(tweets, n):
    """Extracts n-grams from the input tweet data
    
    Parameters
    ----------
    tweets : array_like
        List of tweets
    n : int
        Length of n-grams to be created

    Returns
    -------
    list
        List of n-grams generated

    Examples
    --------
    >>> tweets_list =[
        "Make America Great Again DonaldTrump",
    ]  
    >>> extract_ngram(tweets=tweets_list, n=3)
    [
        "Make America Great",
        "America Great Again",
        "Great Again DonaldTrump"
    ]
    """