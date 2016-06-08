# Python 2
#
#-------------------------------------------------------------------------------
# Name:        Christopher Martinez
# Date:        6/7/16
# Description:
#
# * The program should ask the user to choose rock, paper, or scissors. Then, it
# should repeat back to the user their choice, "reveal" its own choice, and
# report the results. See below for two possible example runs. The program can
# play fairly, can always win, or can always lose--it's up to you. The example
# below shows how it can always win! Briefly, in the game of rock-paper-scissors,
# rock defeats scissors, scissors defeat paper, and paper defeats rock.
#
# * You may assume that the user will input one of rock, paper, or scissors.
# Case matters! We'll stick with lowercase.
#
# You may write the dialog however you like--below is an example dialog if you'd
# like one to follow. We are 'positive' that you can improve on this interaction,
# however! Here are two distinct runs of the program:
#
# Choose your weapon: rock
# the user (you) chose rock
# the comp (I) chose paper
# Ha! I really chose paper -- I WIN!
#
# Choose your weapon: paper
# the user (you) chose paper
# the comp (I) chose dynamite
# I REALLY WIN!
#-------------------------------------------------------------------------------
import random

# Predefined output messages
TIE = "Nobody wins. It's a TIE!"
USER_WIN = 'You win...'
COMP_WIN = 'Ha! I WIN!'

# Get user's and computer's choice
user = raw_input('Choose your weapon: ')
comp = random.choice( ['rock', 'paper', 'scissors'])

# Determine and print the results
print 'the user (you) chose', user
print 'the comp (I) chose', comp

if comp == 'rock':
    if user == 'rock':
        print TIE
    elif user == 'paper':
        print USER_WIN
    else:
        print COMP_WIN
elif comp == 'paper':
    if user == 'rock':
        print COMP_WIN
    elif user == 'paper':
        print TIE
    else:
        print USER_WIN
# The else implies that the computer chose scissors
else:
    if user == 'rock':
        print USER_WIN
    elif user == 'paper':
        print COMP_WIN
    else:
        print TIE
