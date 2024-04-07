""" 
modul zum handeln von keepass
"""
import logging
from configs import HkpDefs
from exceptions import KpdbError 
from helpers import gen_random_string

class Kpdb:
  """
  handle keepass files
  """
  def __init__(self, kpdb=HkpDefs.kpdb, readonly=HkpDefs.readonly):
    # keepass datei pfad
    self.kpdb=kpdb
    # keepass im ro modus öffnen
    self.readonly=readonly
    # pykeepass objekt
    self.pykp=None
    if not self.kpdb:
      raise KpdbError("kpdb ist nichts")
    if readonly:
      self.kpdb_copy=self.create_ro_copy

  def open_kpdb(self, passwd="abc"):
    """ funktion zum öffnen der keepass """
    logging.info("öffne %s mit passwd %s", self.kpdb, passwd)

  def create_ro_copy(self):
    """ funktion zur erstellen der readonly kopie """
    rnd_str=gen_random_string()
    logging.info("erstelle kpdb kopie %s.%s", self.kpdb, rnd_str)
    
