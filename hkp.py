#!/usr/bin/python3
"""
hkp einstiegsskript
"""
import logging
from optsargs import HkpOpts
from configs import HkpLog, HkpDefs
  

class Hkp(HkpDefs):

  def __init__(self, **kwargs):
    # bearbeite logging parameter
    # ...
    super().__init__()
    self.o_log=HkpLog()
    self.sub_cmd=kwargs.get("sub_cmd", self.sub_cmd_def)
    l_log=logging.getLogger("hkp_init")
    l_log.info("initialisiere hkp")

  def run(self):
    logging.info(f"ja du hast den anfang geschafft. sub cmd: {self.sub_cmd}")
    

if __name__ == '__main__':
  o_opts=HkpOpts()
  opts=o_opts.parse_opts()
  o_hkp=Hkp(**opts)
  o_hkp.run()
else: 
  o_hkp=Hkp(sub_cmd="weltall")
  o_hkp.run()
