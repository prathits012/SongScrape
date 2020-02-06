#!/usr/bin/python3
import sys

import lyricsgenius

genius = lyricsgenius.Genius("FWq-nqshdI4i_yjTbN4DytxK0ft4vDl4TqfQ2TL0634rZ_SYlcJO2qKZG4ujlcR_")
artist = genius.search_artist("Drake", max_songs=3, sort="popularity")
print(artist.songs)
for song in artist.songs:
    print(song.lyrics)


#song search

singleSearch = genius.search_song("Over",artist.name)
print(singleSearch.lyrics)