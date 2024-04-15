"""
modul für bearbeitung der show aktion
"""
import logging
import sys
sys.path.append("..")
from kpdb import Kpdb


class HkpShowCmd:
  """ klasse für show aktion """
  def __init__(self, **kwargs):
    logging.info("kwargs=%s",kwargs)
    #self._get_opts_dict(opts_vars)
    self.kpdb=kwargs.get("kpdb")
    self.hosts=kwargs.get("hosts")
    self.ro=kwargs.get("readonly")
    self.kpdb_obj=Kpdb(self.kpdb, self.ro)

  def run(self):
    """ hauptfunktion die aufgerufen wird """
    logging.info("kpdb=%s, hosts=%s, ro=%s", self.kpdb, self.hosts, self.ro)
    self.kpdb_obj.open_kpdb()
    self.kpdb_obj.create_ro_copy()

  #def _get_opts_dict(self, opts_vars):
  #  """ funktion die dict zurückliefert """
  #  return opts_vars

    
    
