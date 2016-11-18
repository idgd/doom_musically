from music21 import *

class Song:
   name = ''
   tempo = 0.0
   tracks = []
   def __init__(self,name,tempo,tracks):
      self.name = name
      self.tempo = tempo
      self.tracks = tracks

class Track:
   name = ''
   notes = []
   def __init__(self, name, notes):
      self.name = name
      self.notes = notes

class MarkovNoteChain:
   noteDict = {}

newTracks = []

e1m1 = converter.parse("mid/d_e1m1.mid")
for addTrack in e1m1:
    newTrack = []
    for addNote in addTrack:
        if type(addNote) == note.Note:
           newTrack.append(note.Note(addNote.pitch))
        if type(addNote) == note.Rest:
           newTrack.append(addNote)

    newTracks.append(newTrack)
    newTrack = []

