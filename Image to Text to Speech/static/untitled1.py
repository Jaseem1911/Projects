# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:58:35 2023

@author: jasee
"""

from translate import Translator
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


translator= Translator(to_lang="Hindi")
translation = translator.translate("Good Morning!")
print(translation)
speaker.Speak(translation)