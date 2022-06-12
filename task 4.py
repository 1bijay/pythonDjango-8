# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 06:37:18 2022

@author: rauni
"""

from text_to_speech import speak

speak("Hello World", "en", save=True, file="Hello-World.mp3", speak=True)