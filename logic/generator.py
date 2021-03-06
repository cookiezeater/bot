#!/usr/bin/python3 

class Generator():
  def __init__(self, db):
    self.db = db
    
  def gen_full_rand(self):
    phrase = ''
    last = False
    words = self.db.fetch_three_words()
    while not last:
      print(words)
      phrase = phrase + str(words[1]) + ' '
      if '#end#' in words:
        last = True
      words = self.db.fetch_three_words(first = words[1], second = words[2])
    return phrase
      
  
  def gen_by_word(self, word_gen):
    left_part = ''
    right_part = ''
    left = False
    right = False
    
    init_words = self.db.fetch_three_words(word = word_gen)
    
    left_words = init_words
    while not left:
      print(left_words)
      left_part = str(left_words[1]) + ' ' + left_part
      if '#beg#' in left_words:
        left = True
      left_words = self.db.fetch_three_words(second = left_words[0], third = left_words[1])
    
    right_words = init_words
    while not right:
      print(right_words)
      right_part = right_part + str(right_words[1]) + ' '
      if '#end#' in right_words:
        right = True
      right_words = self.db.fetch_three_words(first = right_words[1], second = right_words[2])
    
    return left_part + right_part
