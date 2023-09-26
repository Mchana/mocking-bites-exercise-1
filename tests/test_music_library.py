from unittest.mock import Mock
from lib.music_library import MusicLibrary

def test_tracks():
    pass

def test_add():
    # track = Track()
    # fake_artist = Mock()
    # fake_artist.add.return_value = "Queen"
    # fake_title = Mock()
    # fake_title.add.return_value = "Bohemian Rhapsody"
    pass

def test_search_by_keyword_matches():
    library = MusicLibrary()
    fake_match1 = Mock()
    fake_match1.matches.return_values = True
    library.add(fake_match1)

    assert library.search("Hello") == [fake_match1]

def test_search_by_keyword_not_matches():
    library = MusicLibrary()
    fake_match2 = Mock()
    fake_match2.matches.return_values = False
    library.add(fake_match2)

    assert library.search("hi") == [fake_match2]

