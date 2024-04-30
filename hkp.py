#!/usr/bin/python3
# PYTHON_ARGCOMPLETE_OK
"""
hkp einstiegsskript
"""
import logging
from optsargs import HkpOpts
from configs import HkpLog, HkpDefs
  

class Hkp:
  """ hauptklasse für das hkp projekt """

  def __init__(self, **kwargs):
    """ init hkp objekt """
    # bearbeite logging parameter
    # ...
    self.o_log=HkpLog()
    logging.info("initialisiere hkp")
    self.sub_cmd=kwargs.get("sub_cmd", HkpDefs.sub_cmd)
    cmd_class=kwargs.get("cmd_class")
    logging.info("ja du hast den anfang geschafft. sub cmd: %s", self.sub_cmd)
    logging.info("lade cmd class")
    self.cmd_obj=cmd_class(**kwargs)
    

  def run(self):
    """ funktion die alles zum laufen bringt"""
    logging.info("run Forest run")
    self.cmd_obj.run()
    

if __name__ == '__main__':
  o_opts=HkpOpts()
  opts=o_opts.parse_opts()
  o_hkp=Hkp(**opts)
  o_hkp.run()
else: 
  o_hkp=Hkp(sub_cmd="weltall")
  o_hkp.run()
