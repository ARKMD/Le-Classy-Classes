
import random #with class of course
import math #with even more class
import time #need I say it?
import os #alright, time for some math: os backwards is so, and a synonym for so is very.
#If you turn v on its side and round it, you get c. Then, if you curve in the bottom of the r, you get s. Duplicate that for cessy. Turn it into a d: dessy.
#Finally, flip the e upside down and flip it on its side to get a and separate the d into cl: classy!
G = 2 #G will be used in time.sleep(). It is being saved as a constant for simplicity.

class Class:
  def __init__(self, name, classiness=0, lifetime_classiness=0, rank="Commoners' Graduate", items=[]):
    self.name = name
    self.classiness = classiness #I wish I could type outputs in cursive for the *flair*
    self.lifetime_classiness = lifetime_classiness
    self.rank = rank
    self.items = items
  def sip_tea(self):
    print("You sip tea like a true man of class")
    time.sleep(G)
    print("You earned 5 class points.")
    self.get_class(5)
  def speak_fancily(self):
    text = str(input("Say something. ")) #May thou speakst o' th' somethingth?
    charlist = []
    for char in text: #Char is short for character. Yes, even the *classy* people take shortcuts.
      charlist.append(char)
    charpos = 0
    number_of_eths = 0
    for item in charlist:
      if item == ' ':
        charlist.insert(charpos, 'e')
        charlist.insert(charpos+1, 't')
        charlist.insert(charpos+2, 'h')
        charlist.pop(charpos+3)
        charlist.insert(charpos+3, '-')
        number_of_eths+=1
      charpos+=1
    time.sleep(G)
    for item in charlist:
      print(item, end='')

    self.classiness += number_of_eths
    print('\n')
    time.sleep(G)
    print(f"Your classiness has increased by {number_of_eths}")
    self.get_class(number_of_eths)


  def clean_mouth_with_high_quality_napkin(self):
    possible = ["Tissue", "Mitt", "Kitchen Roll"] #Silk Napkins were out of stock, sorry.
    print("Choose a napkin out of the following bunch. Like a true man of class, you will capitalize properly. Any misspell, accidental or not, will lead to a deduction of 15 class points.")
    print(possible)
    my_choice = str(input("Choose. "))
    if my_choice == "Tissue":
      print("You dabbed with a tissue. Could have been better. You earn 5 class points.")
      self.get_class(5)
    elif my_choice == "Mitt":
      print("Good choice. You earn 10 class points.")
      self.get_class(10)
    elif my_choice == "Kitchen Roll":
      print("That's quite painful. 5 class points off for you.")
      self.get_class(-5)
    else:
      print("Ew.") #Ew
      self.get_class(-15)

  def bloat(self): #My mom invented the wheel and my dad taught me the meaning of life.
    points = 0
    try:
      points = int(input("How many people did you bloat and gloat to today? "))
      if points < 25:
        pass
      elif points >= 25 and points < 1000:
        print("Hmm, that is a bit unbelievable...")
        if random.randint(1, 100) <= 63:
          time.sleep(G)
          print("You lose 10% of what you would get, rounded down, of course!")
          points = points - math.floor(points*0.1)
        else:
          time.sleep(G)
          print("...fine.")
      else:
        print("In no world.")
        points = 0
      if points != 0:
        time.sleep(G)
        print("Good job on boasting! You earn class points!")
      self.get_class(points)
    except:
      print("As a person of class, you are expected to give the formal, appropriate answers. You are losing 10 points.")
      self.get_class(-10)

  def speak_check(self):
    speak_points = 0
    my_text = str(input("Say something: "))
    time.sleep(G)
    print("Here's the procedure. A real classy person speaks with more vowels and less consonants, a.k.a. hard and rubbish spit-inducing sounds.")
    time.sleep(G)
    print("You will be graded on how many vowels vs consonants there were. +1 point for each vowel. -1 point for each consonant.")
    for character in my_text:
      if character.lower() in ['a', 'e', 'i', 'o', 'u', 'y']: #Yes, I'm counting y
        speak_points += 1
      else:
        speak_points -= 1
    time.sleep(G)
    print(f"The quality of your speech was... {speak_points} points.")
    self.get_class(speak_points)

  def auction(self):
    up_for_sale = ["Silk Napkin", "Monocle", "Flowered China"]
    try:
      bet = int(input("Approximately how many class points to you wish to spend? "))
      if bet > self.classiness:
        print("Too much!")
        return
      if bet <= 0:
        print("Too little!")
        return
      selling = up_for_sale[random.randint(0, 2)]
      print("The item up for sale is...")
      time.sleep(G)
      print(selling)
      price = random.randint(500, 1000)
      if price > bet:
        time.sleep(G)
        print(f"You bet {bet}")
        time.sleep(G)
        print(f"Someone else bets {price}")
        time.sleep(G)
        print("The two of you stare at each other.")
        time.sleep(G)
        try:
          bet = int(input("How much are you betting? "))
          price = random.randint(1000, 1250)
          if bet > self.classiness:
            print("Too much! They win!")
            return
          if bet <= 0:
            print("Too little! They win!")
            return
          if bet > price:
            print(f"You bet {bet}")
            time.sleep(G)
            print(f"They bet {price}")
            time.sleep(G)
            print("Yours is higher. The lady up front calls. 'Going once. Going twice. Sold!'")
            time.sleep(G)
            if selling in self.items:
              print("You already have it. But oh well, what's the harm in a double?")
            else:
              print("You got a new item!")
              self.items.append(selling)
              print(f"Your items: {self.items}")
              self.get_class(bet*-1)
              return
          elif bet == price:
            print("It's equal! The lady up front announces it's going to donations. No item for you. Sorry.")
          else:
            print(f'You bet {bet}')
            time.sleep(G)
            print(f'They bet {price}')
            time.sleep(G)
            print("They win! No item for you, sorry.")
            time.sleep(G)
        except ValueError:
            print("That isn't an integer! The other one gets the prize. Sorry.")

        else:
          time.sleep(G)
          print(f"Someone bets {price}")
          time.sleep(G)
          print(f"You retaliate by betting {bet}")
          time.sleep(G)
          print("You win!")
          time.sleep(G)
          print(f"You earn {selling}!")
          self.items.append(selling)
          print(f"Your items: {self.items}")
          self.get_class(bet*-1)
          return

    except ValueError:
      print("You can't spend that!")

  def Classy(self):
    if self.rank != "Classy. Congratulations.":
      print("You are not classy enough.")
      return
    else:
      print("You walk with so much classiness you turn even the most noisy of the street dogs into hounds of class.")
      time.sleep(G)
      print("You talk with so much classiness you turn even the most disgusting of the farm pigs into oinkers of class.")
      time.sleep(G)
      print("Your looks have so much class you turn even the most common of the common into humans of class.")
      time.sleep(G)
      print("As you walk, talk, and look, you think of your journey... how you started as the common man going for groceries and then were enlightened with the art of classiness.")
      time.sleep(G)
      print("You only hope that these commoners can do the same.")
      time.sleep(G)
      print("You are the child of Class himself.")
      time.sleep(G)

  def seat(self):
    try:
      print("You are at Fancypants Theater on Fancypants BLVD.")
      time.sleep(G)
      print("You must choose a seat.")
      seating = int(input("You enter the theater and are given a choice on where to sit. You have 3 choices. They are:\n  1.  The front\n  2.  The back\n  3.  The nosebleed\nType either 1, 2, or 3. "))
      if seating == 1:
        print("You sit in the front like a true classman. Gained 50 points")
        self.get_class(50)
      elif seating == 2:
        print("Yuck, sitting in the back like a dog? Lose 25 points")
        self.get_class(-25)
      elif seating == 3:
        print("Although it's the cheap section, you get to watch over everyone beneath you like you're a king watching over the peasents. Gain 25 points")
        self.get_class(25)
      else:
        print("That is not between 1 and 3. MATH, fool, MATH. -10 points.")
        self.get_class(-10)
    except:
      print("Goodness are you actually that dumb? Whatever, you lose points.")
      self.get_class(-25)

  def correct_or_not(self, ans, right):
    return ans == right

  def quiz(self):
    cheat_sheet = {
        "What is the best adjective? Hint: it's classy." : {"Right": "Mellifluous", "Message" : "You disappoint me."},
        "Anna vs Ava. Which name is more common?" : {"Right" : "Neither: Lucy", "Message" : "Don't you remember? Lucy was the infamous common lady who slurped her food *faint*!"},
        "Why is platinum better than gold?" : {"Right": "Wrong. Gold is better--it's the classic, after all!", "Message" : "Sorry, gamers."},
        "Why was 6 afraid of 7?" : {"Right":"Ew, I don't do childish humor.", "Message": "7 will eat your dignity if you ever crack a joke like this again."},
        "Meter or metre? Theater or theatre?" : {"Right": "Meter and theatre. Why is it different? Just because!", "Message" : "I refuse to elaborate."}
    }
    print("Welcome to the classiness quiz. Instructions? Answer these questions correctly, or, as a true classy person would say, righteously.")
    activate = input("First, just say something random: ")
    if activate.lower() == 'classy':
      print("You have activated the cheat sheet.")
      time.sleep(G)
      print("'Right' refers to the case-sensitive answer. 'Message' is simply the message that will output if you get the answer wrong. However, that shouldn't be the case for you (unless it is, in which case, I'll be too speechless to insult you).")
      time.sleep(G)
      print(cheat_sheet)
    score = 0
    for item in cheat_sheet.keys():
      print(item)
      ans = input("Answer: ")
      eval = self.correct_or_not(ans, cheat_sheet[item]["Right"])
      if eval:
        print("That is... righteous.")
        time.sleep(G)
        score+=10
      else:
        print("That is... wrong. The right answer is:")
        time.sleep(G)
        print(cheat_sheet[item]["Right"])
        time.sleep(G)
        print(cheat_sheet[item]["Message"])
        score -= 10

    self.get_class(score)
    return

  def get_class(self, how_much):
    time.sleep(G)
    self.classiness+=how_much #Good job!
    if how_much <= 0:
      pass
    else:
      self.lifetime_classiness+=how_much

    if self.lifetime_classiness >= 1000:
      self.rank = "Classy (Congratulations)." #Congratulations indeed good sir!
    elif self.lifetime_classiness >= 750:
      self.rank = "Tea Sipping Master"
    elif self.lifetime_classiness >= 500:
      self.rank = "Aristocrat"
    elif self.lifetime_classiness >= 400:
      self.rank = "Well Mannered"
    elif self.lifetime_classiness >= 300:
      self.rank = "Etiquette Master"
    elif self.lifetime_classiness >= 200:
      self.rank = "Tea Sipping Novice"
    elif self.lifetime_classiness >= 100:
      self.rank = "Fancyman"
    


    print(f"Your current classiness: {self.classiness}") #Feel proud! You've earned it :)
    print(f"Your lifetime classiness: {self.lifetime_classiness}")
    time.sleep(G)
    print(f"Your rank: {self.rank}")
    return
