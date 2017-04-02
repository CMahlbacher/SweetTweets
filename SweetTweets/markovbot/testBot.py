import twitter
import os
import time
import sys
import copy
import pickle
from threading import Thread, Lock
from multiprocessing import Queue

from markovbot35 import MarkovBot
#from Code import Code
from random import randint
from Linked_List import Linked_List
#from Code import Code

class SweetTweet:
   class _Code:
    #self.nicePositiveList = Linked_List()
    #self.niceNegativeList = Linked_List()
      def __init__(self):
         self.goodList = Linked_List()
         self.badList = Linked_List()
         allPositives = open("happy.txt", "r")
         allNegatives = open("unhappy.txt", "r")
         self.niceNegativeList = Linked_List()
         self.nicePositiveList = Linked_List()
        
         for word in allPositives.readlines():
            self.goodList.append_element(word)
         for word in allNegatives.readlines():
            self.badList.append_element(word)
         allPositives.close()
         allNegatives.close()
        
        
        
         for i in self.badList:
            word = i[:len(i) - 2]
            self.niceNegativeList.append_element(word)
         for i in self.goodList:
            word = i[:len(i)-2]
            self.nicePositiveList.append_element(word)
        
        
         self.goodVerbs = Linked_List()
         self.goodNouns = Linked_List()
         self.goodAdjectives = Linked_List()
         self.goodAdverbs = Linked_List()
         self.goodPrepositions = Linked_List()
         self.badVerbs = Linked_List()
         self.badNouns = Linked_List()
         self.badAdjectives = Linked_List()
         self.badAdverbs = Linked_List()
         self.badPrepositions = Linked_List()
         for i in range(len(self.goodList)):
            word = self.goodList.get_element_at(i)
            type = word[len(word)-2:len(word)-1]
            part = word[:len(word)-2]
            if type == "A":
               self.goodAdjectives.append_element(part)
            elif type == "V":
               self.goodVerbs.append_element(part)
            elif type == "N":
               self.goodNouns.append_element(part)
            elif type == "B":
               self.goodAdverbs.append_element(part)
            elif type == "P":
               self.goodPrepositions.append_element(part)
         for i in range(len(self.badList)):
            word = self.badList.get_element_at(i)
            type = word[len(word)-2:len(word)-1]
            part = word[:len(word)-2]
            if type == "A":
               self.badAdjectives.append_element(part)
            elif type == "V":
               self.badVerbs.append_element(part)
            elif type == "N":
               self.badNouns.append_element(part)
            elif type == "B":
               self.badAdverbs.append_element(part)
            elif type == "P":
               self.badPrepositions.append_element(part)
                
         for i in range(len(self.badNouns)):
            word = self.badNouns.get_element_at(i)
            newWord = word + "s"
            self.badNouns.insert_element_at(newWord, i+1)
            
      def random(self, array):
         x = randint(0, len(array) - 1)
         return array.get_element_at(x)
        
                
      def stringSwitch(self, string):
         tweetWords = string.split()
         array = []
         for word in tweetWords:
            newWord = "".join(c for c in word if c not in ('!','.',':'))
            if self.binarySearch(newWord, self.badAdjectives):
               array.append(self.random(self.goodAdjectives))
            elif self.binarySearch(newWord, self.badNouns):
               array.append(self.random(self.goodNouns))
            elif self.binarySearch(newWord, self.badVerbs):
               array.append(self.random(self.goodVerbs))
            elif self.binarySearch(newWord, self.badAdverbs):
               array.append(self.random(self.goodAdverbs))
            elif self.binarySearch(newWord, self.badPrepositions):
               array.append(self.random(self.goodPrepositions))
            else:
               array.append(word)
         s = " "
         return s.join(array)
   
        
      def binarySearch(self, searchTerm, array):
         a = 0
         b = len(array) - 1
         while a <= b:
            m = ((a + b) // 2)
            if searchTerm.lower() < array.get_element_at(m).lower():
               b = m - 1
            if searchTerm.lower() > array.get_element_at(m).lower():
               a = m + 1
            if searchTerm.lower() == array.get_element_at(m).lower():
               return True
         return False
    
      def getGoodList(self):
         return str(self.goodList)
    
    
    
      def listToArray(self, list):
         array = []
         for i in list:
            array.append(i)
         return array
      def getNegativeList(self):
         return self.niceNegativeList
      def getPositiveList(self):
         return self.nicePositiveList
   code = _Code()
   badWords = code.getNegativeList()
   goodWords = code.getPositiveList()
# # # # #
# INITIALISE

# Initialise a MarkovBot instance
   tweetbot = MarkovBot()

# Get the current directory's path
   dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
   book = os.path.join(dirname, 'Freud_Dream_Psychology.txt')
# Make your bot read the book!
   tweetbot.read(book)


# # # # #
# TEXT GENERATION

# Generate text by using the generate_text method:
# 	The first argument is the length of your text, in number of words
# 	The 'seedword' argument allows you to feed the bot some words that it
# 	should attempt to use to start its text. It's nothing fancy: the bot will
# 	simply try the first, and move on to the next if he can't find something
# 	that works.
#my_first_text = tweetbot.generate_text(25, seedword=[u'dream', u'psychoanalysis'])

# Print your text to the console
#print(u'\ntweetbot says: "%s"' % (my_first_text))


# # # # #
# TWITTER

# The MarkovBot uses @sixohsix' Python Twitter Tools, which is a Python wrapper
# for the Twitter API. Find it on GitHub: https://github.com/sixohsix/twitter

# ALL YOUR SECRET STUFF!
# Make sure to replace the ''s below with your own values, or try to find
# a more secure way of dealing with your keys and access tokens. Be warned
# that it is NOT SAFE to put your keys and tokens in a plain-text script!

# Consumer Key (API Key)
   cons_key = 'S7mVdOfUIIa1FL6bdFgaTZXmh'
# Consumer Secret (API Secret)
   cons_secret = 'q8UFr4EQ2gnfGAp8wsaYpQfhBYkQK9xYREnW77W4Ej9X9rQfqM'
# Access Token
   access_token = '847998506312888321-bmPb5lgqL8xBOaK7QR7oUrSIEEM5IEv'
# Access Token Secret
   access_token_secret = 'uUgSMYTUS7cQegJGpiul2x2Rc6G4inDZsaWKpxqKKwQfd'
   
# Log in to Twitter
   tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
   print("Logged in")
# The target string is what the bot will reply to on Twitter. To learn more,
# read: https://dev.twitter.com/streaming/overview/request-parameters#track
   index = randint(0,len(badWords))
   targetstring = '@Dankpocalypse16'
   print(targetstring)
   
   iterator = tweetbot._ts.statuses.filter(track=tweetbot._targetstring)
   
   T = True
   #while T == True:
    #  for i in range(0,len(badWords)):
     #    if badWords.get_element_at(i) in tweet[u'text']:
      #      targetstring = badWords.get_element_at(i)
       #     T = False
        #    break
      #if targetstring == None:
       #  continue
   
# Keywords are words the bot will look for in tweets it'll reply to, and it
# will attempt to use them as seeds for the reply
   print(code.listToArray(code.getPositiveList()))
   keywords = code.listToArray(code.getNegativeList())
   print(keywords)
   replacementWords = [None]*len(keywords)
   for i in range(0,len(keywords)):
      replacementWords[i] = code.stringSwitch(keywords[i])
   print(replacementWords)
# The prefix will be added to the start of all outgoing tweets.
   prefix = None
# The suffix will be added to the end of all outgoing tweets.
   suffix = '#DiluteTheHate'
# The maxconvdepth is the maximum depth of the conversation that the bot will
# still reply to. This is relevant if you want to reply to all tweets directed
# at a certain user. You don't want to keep replying in the same conversation,
# because that would be very annoying. Be responsible, and allow your bot only
# a shallow conversation depth. For example, a value of 2 will allow the bot
# to only reply in conversations where there are two or less replies to the
# original tweet.
   maxconvdepth = 1

# Start auto-responding to tweets by calling twitter_autoreply_start
# This function operates in a Thread in the background, so your code will not
# block by calling it.
   tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
   #tw = tweetbot._tweets
# Start periodically tweeting. This will post a tweet every X days, hours, and
# minutes. (You're free to choose your own interval, but please don't use it to
# spam other people. Nobody likes spammers and trolls.)
# This function operates in a Thread in the background, so your code will not
# block by calling it.
#tweetbot.twitter_tweeting_start(days=0, hours=19, minutes=30, keywords=None, prefix=None, suffix='#BleepBloop')

# DO SOMETHING HERE TO ALLOW YOUR BOT TO BE ACTIVE IN THE BACKGROUND
# You could, for example, wait for a week:
   secsinweek = 7 * 24 * 60 * 60
   time.sleep(75)
 
# Use the following to stop auto-responding
# (Don't do this directly after starting it, or your bot will do nothing!)
   tweetbot.twitter_autoreply_stop()

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
#tweetbot.twitter_tweeting_stop()
if __name__ == "__main__":
   sweetTweet = SweetTweet()