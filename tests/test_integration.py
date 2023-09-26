from unittest.mock import Mock
from lib.music_library import MusicLibrary
from lib.track import Track

def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track1 = Track("title1","artist1")
    track2 = Track("title2", "artist2")
    library.add(track1)
    library.add(track2)

    assert library.tracks == [track1,track2]

def test_add_and_search_track_list():
    library = MusicLibrary()
    track1 = Track("title1","artist1")
    track2 = Track("title2", "artist2")
    library.add(track1)
    library.add(track2)

    assert library.search("title1") == [track1]

    #yo