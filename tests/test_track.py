from unittest.mock import Mock 
from lib.track import Track

def test_matches_true():
    track1 = Track("artist1","artist2")

    assert track1.matches("artist1") == True

def test_matches_false():
    track2 = Track("artist2","track2")

    assert track2.matches("Greetings") == False