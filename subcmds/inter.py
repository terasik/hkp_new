"""
modul für bearbeitung der inter aktion
"""
import logging
import sys
import cmd
sys.path.append("..")
from kpdb import Kpdb


class HkpInterCmd:
  """ klasse für inter aktion """
  def __init__(self, **kwargs):
    logging.info("kwargs=%s",kwargs)
    #self._get_opts_dict(opts_vars)
    self.kpdb=kwargs.get("kpdb")
    self.ro=kwargs.get("readonly")
    self.kpdb_obj=Kpdb(self.kpdb, self.ro)

  def run(self):
    """ hauptfunktion die aufgerufen wird """
    logging.info("kpdb=%s, ro=%s", self.kpdb, self.ro)
    self.kpdb_obj.open_kpdb()
    #self.kpdb_obj.create_ro_copy()

  #def _get_opts_dict(self, opts_vars):
  #  """ funktion die dict zurückliefert """
  #  return opts_vars

    
    
