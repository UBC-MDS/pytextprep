from pytextprep import pytextprep
from pytextprep.extract_hashtags import extract_hashtags
import pytest
import re

tweets_list =[
"If only Bradley's arm was longer. Best photo ever. #oscars",
"hello literally everyone",
"Congratulations to the Astronauts that left Earth today. Good choice",
"We LOVE this idea, Happy  100th Birthday Betty! #BettyWhiteChallenge #HappyBirthdayBettyWhite #MondayMotivation",
"“When You're Accustomed to Privilege, Equality Feels Like Oppression.” #DjokovicOut #Djokovic #Djocovid #djokovicgohome  #AusOpen #AO2022"
]

expected_htags = [
    "oscars",
    "BettyWhiteChallenge", 
    "HappyBirthdayBettyWhite",
    "MondayMotivation",
    "DjokovicOut",
    "Djokovic",
    "Djocovid",
    "djokovicgohome",  
    "AusOpen", 
    "AO2022"
]

def test_extract_hashtags():
    """ Test generated hashtags list from extract_hashtags function """
 
    actual_htags = extract_hashtags(tweets=tweets_list)
    assert isinstance(actual_htags, list), \
           "Wrong output type"
    assert len(actual_htags) == 10, \
           "Incorrect number of hashtags identified"
    assert actual_htags == expected_htags, \
            "Content of hashtags list is incorrect"

def test_hashtags_input_error():
    """Check TypeError raised when list is not used."""
    with pytest.raises(TypeError):
        extract_hashtags(1)
    
