# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:55:27 2021

@author: Alex
"""

import random

disc = ['putter', 'midrange', 'fairway driver', 'distance driver'];
angle = ['hyzer', 'flat', 'anhyzer'] ;
throw = ['backhand', 'forehand'];

prescription = [random.choice(disc), random.choice(angle), random.choice(throw)];

print('I recommond throwing a ' + prescription[0] + ' on ' + prescription[1] + ' with a ' + prescription[2] + '.')