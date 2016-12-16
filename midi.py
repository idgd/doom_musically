import random
import copy
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
	print track
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

newSong = Song("e1m1",90,songTracks)
markovChain = MarkovNoteChain()

for track in newSong.tracks:
	for index,note in enumerate(track.notes):
		if type(note) == type(exampleNote):
			markovChain.noteDict[note.pitch.midi] = []
		if type(note) == type(exampleRest):
			markovChain.noteDict[note.fullName] = []

for mark in markovChain.noteDict:
	for track in newSong.tracks:
		for index,note in enumerate(track.notes):
			if type(note) == type(exampleNote) and note.pitch.midi == mark and index < len(track.notes) - 1:
				markovChain.noteDict[mark].append(track.notes[index + 1])
			if type(note) == type(exampleRest) and note.fullName == mark and index < len(track.notes) - 1:
				markovChain.noteDict[mark].append(track.notes[index + 1])

#stream = midi.realtime.StreamPlayer(e1m1)
#stream.play()

newStream = stream.Stream()

def nextNote(note, n):
	while n > 0:
		if type(note) == type(exampleNote):
			nextnote = copy.copy(random.choice(markovChain.noteDict[note.pitch.midi]))
		if type(note) == type(exampleRest):
			nextnote = copy.copy(random.choice(markovChain.noteDict[note.fullName]))
		newStream.append(nextnote)
		return nextNote(nextnote, n - 1)

nextNote(exampleNote,500)
newStream.show('midi')
