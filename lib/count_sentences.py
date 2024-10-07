#!/usr/bin/env python3

class MyString:
  def __init__(self, value="String"):
    self.value = value

  @property
  def value(self):
    """The value property"""
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    return (self._value[-1] == ".")
  
  def is_question(self):
    return (self._value[-1] == "?")
  
  def is_exclamation(self):
    return (self._value[-1] == "!")
  
  def count_sentences(self):
    tmp = self._value.replace("???", "?", -1)
    tmp = tmp.replace("??", "?", -1)
    tmp = tmp.replace("?", ".", -1)
    tmp = tmp.replace("!!!", "!", -1)
    tmp = tmp.replace("!!", "!", -1)
    tmp = tmp.replace("!", ".", -1)
    tmp = tmp.replace("...", ".", -1)
    tmp = tmp.replace("..", ".", -1)
    
    tmp = tmp.split(".")
    return len(tmp) - 1
