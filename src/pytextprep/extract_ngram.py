def extract_ngram(filepath, n):
    """Extracts n-grams from the input tweet data
    
    Parameters
    ----------
    filepath : str
        Path to a text file containing tweets data.
    n : int
        Number of n-grams to be created

    Returns
    -------
    list
        List of n-grams generated

    Examples
    --------
    >>> extract_ngram("tweets.txt", 4)
    """