"""
modul für bearbeitung der inter aktion
"""
import logging
import sys
import cmd
sys.path.append("..")
from kpdb import Kpdb


class InterLoop(cmd.Cmd):
  """ command loop """
  prompt="> "
  intro="interaktive keepass konsole"

  entries=["uzt", "agf jl", "jgj"]
  groups=["bvfm", "hz", "öklml zg"]

  def do_cd(self, line):
    "wechsle ins verzeichnis"
    print(f"wechsle ins {line} verzeichnis")

  def complete_cd(self,text, line, begidx, endidx):
    if not text:
      completions=self.groups[:]
    else:
      completions=[c for c in self.groups if c.startswith(text)]
    return completions

  def complete_ls(self,text, line, begidx, endidx):
    choices=self.entries+self.groups
    if not text:
      completions=choices[:]
    else:
      completions=[c for c in choices if c.startswith(text)]
    return completions

  def do_ls(self, line):
    "liste etwas auf"
    print(f"liste {line} auf")

  def do_EOF(self, line):
    """ ende """
    print("beende interaktive konsole")
    return True
  

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
    InterLoop().cmdloop()
    self.kpdb_obj.close_kpdb()
    

  #def _get_opts_dict(self, opts_vars):
  #  """ funktion die dict zurückliefert """
  #  return opts_vars

    
    
