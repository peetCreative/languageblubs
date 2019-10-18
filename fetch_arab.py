#!/usr/bin/env python

"""Foobar.py: Fetch arab from translation websites"""

__author__      = "Peter Klausing"
__copyright__   = "GPLv3"

# First aim make a interactive thing
# 1. user enters word
# 2. looksup on google a translation
# 3. 1 -> OK 2-> I want to give own translation
# 2.a) ask for word
# 2.b) ask pronounciation


from googletrans import Translator
import os

class chat_bot:
	def __init__(self):
		self.gtrans = Translator()

	def create_voc(self, voc_name):
		fname = voc_name + '.csv'
		if os.path.isfile(fname): 
			self.csv_file = open(fname, 'a')
		else:
			self.csv_file = open(fname, 'w')
			self.csv_file.write("TABLE\,//INFO,//START//\n%s,deutsch,arabisch\n"%(voc_name))

	def add_voc(self, word, translation, pronouciation):
		self.csv_file.write("%s,%s,%s,\n"%(word,translation,pronouciation))

	def lookup_arab_word(self, word):
		return self.gtrans.translate(word, dest='ar', src='de')

def main():
	bot = chat_bot()
	print("Gib den Namen deiner Vokabelliste")
	voc_name = input()
	bot.create_voc(voc_name)
	while True:
		word = input()
		if word.startswith('\end'):
			break
		trans = bot.lookup_arab_word(word)
		translation = trans.extra_data['translation'][0][0]
		pronouciation = trans.extra_data['translation'][1][2]
		print("Google übersetzt: %s %s\n a) korrekt b) Gib eigene Übersetzung"%(translation, pronouciation))
		while True :
			answer = input()
			if answer == 'a':
				bot.add_voc(word,translation,pronouciation)
				break
			if answer == 'b':
				print("Schreib deine Eigene Übersetzung")
				translation = input()
				print("Schreib deine Eigene Übersetzung")
				pronouciation = input()
				print("Deine Vokabel: %s %s\n a) korrekt b) Gib eigene Übersetzung"%(translation, pronouciation))
			else:
				print("I didn't got it. Nochmal! \n a) korrekt b) Gib eigene Übersetzung")
		print("%s,%s,%s hinzugefügt. Nächste"%(word,translation,pronouciation))


if __name__ == "__main__":
	print("Schreib ein Deutsches Wort.")
	main()
