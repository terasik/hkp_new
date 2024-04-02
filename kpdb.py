""" 
modul zum handeln von keepas
"""
import logging
from configs import HkpDefs
from helpers import *

class kpdb:
  """
  handle keepass files
  """
  def __init__(self, kpdb=None, readonly=False):
    self.kpdb=kpdb
    self.readonly=readonly
    if readonly:
      self.kpdb_copy=self.create_ro_copy
    

  def open_kpdb(self):
    """ funktion zum öffnen der keepass """


  def create_ro_copy(self):
    """ funktion zur erstellen der readonly kopie """
    

