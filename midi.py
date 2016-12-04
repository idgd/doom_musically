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

exampleNote = note.Note("E2")
exampleRest = note.Rest()

newTracks = []

e1m1 = converter.parse("mid/d_e1m1.mid")

for track in e1m1:
    
    newNotes = []
    
    for note in track:
        newNotes.append(note)
    
    newTracks.append(newNotes)
    newNotes = []

iterator = 0
songTracks = []
for track in newTracks:
    foo = Track("T%s" % iterator, track)
    songTracks.append(foo)
    iterator += 1

print e1m1.tempo

#for track in newTracks:
#   for note in track:
#      noteArr = []
#      for nextNote in track:
#          if type(note) == type(exampleNote):
#             print "1"
#             print note.pitch
#             print exampleNote.pitch
#             if note.pitch == exampleNote.pitch:
#                print "2"
#                if iterator < len(track) - 1:
#                   print "3"
#          iterator += 1
#      iterator = 0
#      if type(note) == type(exampleNote):
#         newDict[note.midi] = noteArr
#      elif type(note) == type(exampleRest):
#         newDict[note] = noteArr
#      noteArr = []

#for f in newTracks:
#   for g in f:
#      newDict[g] = []
#   noteArr = []
#   for n in newDict:
#      for o in f:
#         if n == o and iterator < len(f):
#            noteArr.append(o)
#   newDict[n] = noteArr

#print(newDict)
