import os
import time
from Code import Code

from markovbot35 import MarkovBot
from Linked_List import Linked_List
from random import randint
class Code:

    def __init__(self):
        self.goodList = Linked_List()
        self.badList = Linked_List()
        allPositives = open("happy.txt", "r")
        allNegatives = open("unhappy.txt", "r")
        
        
        
        for word in allPositives.readlines():
            self.goodList.append_element(word)
        for word in allNegatives.readlines():
            self.badList.append_element(word)
        allPositives.close()
        allNegatives.close()
        
        self.niceNegativeList = Linked_List()
        self.nicePositiveList = Linked_List()
        for i in self.badList:
            word = i[:len(i) - 2]
            self.niceNegativeList.append_element(word)
        for i in self.goodList:
            word = i[:len(i) - 2]
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
        return self.goodList
    
    def getNegativeList(self):
        return self.niceNegativeList
    
    def listToArray(self, list):
        array = [None]*len(list)
        for i in range(len(list)):
            array[i] = list.get_element_at(i)
        return array
       
sweetTweets = MarkovBot()


#thefile = open('replies.txt', 'w')
#for item in keywords:
  #thefile.write("%s\n" % item)
# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'timemachine.txt')
# Make your bot read the book!
sweetTweets.read(book)


#my_first_text = sweetTweets.generate_text(25, seedword=keywords)
#print("Sweet Tweets says:")
#print(my_first_text)

# Consumer Key (API Key)
cons_key = 'S7mVdOfUIIa1FL6bdFgaTZXmh'
# Consumer Secret (API Secret)
cons_secret = 'q8UFr4EQ2gnfGAp8wsaYpQfhBYkQK9xYREnW77W4Ej9X9rQfqM'
# Access Token
access_token = '847998506312888321-bmPb5lgqL8xBOaK7QR7oUrSIEEM5IEv'
# Access Token Secret
access_token_secret = 'uUgSMYTUS7cQegJGpiul2x2Rc6G4inDZsaWKpxqKKwQfd'


# Log in to Twitter
sweetTweets.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
print('Logged In!')

# Set some parameters for your bot
#prefix = code.stringSwitch("a dead failure")
#targetstring = prefix

targetstring = 'ugly'
prefix = 'Hey, we should try to be nicer on the internet. Have a good day, friend! Next time, try a message like this: '#code.stringSwitch(targetstring)
print(prefix)
code = Code()
goodList = code.getGoodList()
keywords = code.nicePositiveList#code.listToArray(goodList)
#suffix = '#DiluteTheHate'
suffix = '#DiluteTheHate'
maxconvdepth = 2

# Start auto-responding to tweets

sweetTweets.twitter_autoreply_start(targetstring, database=u'auto-language', keywords=keywords, 
   prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)

#sweetTweets.twitter_tweeting_start(days=0, hours=0, minutes=1, #keywords=code.stringSwitch("a stupid ugly face"),
#prefix=code.stringSwitch("a stupid ugly face"), suffix='#DiluteTheHate')

time.sleep(60)

sweetTweets.twitter_autoreply_stop()

#sweetTweets.twitter_tweeting_stop()
