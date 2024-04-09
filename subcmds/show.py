"""
modul für bearbeitung der show aktion
"""
import logging


class HkpShowCmd:
  """ klasse für show aktion """
  def __init__(self, **kwargs):
    logging.info("kwargs=%s",kwargs)
    #self._get_opts_dict(opts_vars)
    self.kpdb=kwargs.get("kpdb")
    self.hosts=kwargs.get("hosts")

  def run(self):
    """ hauptfunktion die aufgerufen wird """
    logging.info("kpdb=%s, hosts=%s", self.kpdb, self.hosts)

  #def _get_opts_dict(self, opts_vars):
  #  """ funktion die dict zurückliefert """
  #  return opts_vars

    
    
