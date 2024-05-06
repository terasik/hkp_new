""" 
modul zum handeln von keepass
"""
import logging
import os
import re
from configs import HkpDefs
from exceptions import KpdbError 
from helpers import gen_random_string
from getpass import getpass
from pykeepass import PyKeePass
from shutil import copy2


class Kpdb:
  """
  handle keepass files
  """
  def __init__(self, kpdb=HkpDefs.kpdb, readonly=HkpDefs.readonly):
    # keepass datei pfad
    self.kpdb=self.kpdb_orig=kpdb
    # keepass im ro modus öffnen
    self.readonly=readonly
    # pykeepass objekt
    self.pykp=None
    self.pwd="/"
    if not self.kpdb:
      raise KpdbError("kpdb ist nichts")
    if self.readonly:
      self.kpdb=self.create_ro_copy()

  def close_kpdb(self):
    if self.readonly:
      try:
        logging.info("lösche ro kpdb %s..", self.kpdb)
        os.unlink(self.kpdb)
      except Exception as _exc:
        logging.error("löschen von ro kpdb %s nicht möglich", self.kpdb)

  def open_kpdb(self, passwd="abc"):
    """ funktion zum öffnen der keepass """
    logging.info("öffne %s mit passwd %s", self.kpdb, passwd)
    if not passwd:
      passwd=getpass(f"Passwort ({self.kpdb})")
    self.pykp=PyKeePass(self.kpdb, passwd)

  def create_ro_copy(self):
    """ funktion zur erstellen der readonly kopie """
    rnd_str=gen_random_string()
    logging.info("erstelle kpdb kopie %s.%s", self.kpdb, rnd_str)
    try:
      copy2(self.kpdb, f"{self.kpdb}.{rnd_str}")
    except Exception as _exc:
      raise KpdbError(f"erstellen der kpdb kopie nicht möglich: {_exc}")
    return f"{self.kpdb}.{rnd_str}"

  def find_group_by_path(self, path=None, ignore_case=True):
    """ finde gruppe anhand vom pfad """
    if path:
      typename_path=type(path).__name__
      if typename_path=="str":
        path=[x for x in re.split("/+", path) if x]
      logging.info("path=%s", path)
      if ignore_case:
        return self.pykp.find_groups(path=path, regex=True, flags="i")
      else:
        return self.pykp.find_groups(path=path, regex=True)
      
    else:
      return None


