#!/usr/bin/env python3
import re

class MyString:
  value = ''
  def __init__(self,value):
    self.value = value
    if type(value) == str:
      return self.value
    else:
      raise TypeError('Value must be a string')
  


  def is_sentence(self, value):
    self.value = value
    if self.value.endswith('.'):
      return True
    else:
      return False

  def is_question(self, value):
    self.value = value
    if self.value.endswith('?'):
      return True
    else:
      return False
  
  def is_exclamation(self, value):
    self.value = value
    if self.value.endswith('!'):
      return True
    else:
      return False
  
  def count_sentences(self):
             
    sentences = re.split(r'[.!?]', self.value)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


