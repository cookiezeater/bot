#!/usr/bin/python3

import json
from pprint import pprint

class Parser():
  def __init__(self):
    pass
  
  def parse(self,filename):
    with open(filename) as file:
      data = json.load(file)
      pprint(data)
      return data
