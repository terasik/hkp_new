"""
modul für bearbeitung der inter aktion
    readline.set_completer(self.completer)
"""
import readline
import logging
import sys
import cmd
import re
sys.path.append("..")
from kpdb import Kpdb


class InterLoop(cmd.Cmd):
  """ command loop """
  prompt="> "
  intro="interaktive keepass konsole"

  entries=["uzt", "agf jl", "jgj"]
  #groups=["bvfm", "hz", "öklml zg"]

  def __init__(self, kpdb):
    super().__init__()
    readline.parse_and_bind("tab: complete")
    readline.set_completer_delims(" \n\t=")
    logging.info("kpdb ist %s", kpdb.kpdb)
    logging.info("pwd ist %s", kpdb.pwd)
    self.kpdb=kpdb
    self.groups=["/"+"/".join(g.path) for g in self.kpdb.pykp.groups if g]
    #self.groups=["/bvfm", "hz/uz", "öklml zg", "/bt/z", "/zt te/tr", "/zh"]
    logging.info("gruppen: %s",self.groups)

  def resolve_path(self, path=None):
    pwd=self.kpdb.pwd
    if not path: return pwd
    else:
      path_new=pwd
      path_spl=[x for x in re.split("/+", path) if x]
      #print(f"path_spl: {path_spl}")
      pwd_spl=[x for x in re.split("/+", pwd) if x]
      if path.startswith("/"):
        path_new_spl=[]
      else:
        path_new_spl=pwd_spl
      c=1
      for d in path_spl:
        if (not d) or re.match("^\.{1}$",d): 
          continue
        elif re.match("^\.{2,}$",d):
          _o=len(path_new_spl)-(c)
          path_new_spl=path_new_spl[0:_o]
          c+=1
        else:
          path_new_spl.append(d)
          c=1
        #print(f"3 c: {c} d: {d} path_new: {path_new_spl}")
      if len(path_new_spl)==0: 
        return "/"
      else:
        return "/"+"/".join(path_new_spl)

  def emptyline(self):
    pass

  def do_cd(self, line):
    "wechsle ins verzeichnis"
    print(f"wechsle ins {line} verzeichnis")
    #for g in groups:
    #  print(g)
    res_path=self.resolve_path(line)
    self.kpdb.pwd=res_path
    print(f"aufgelöster pfad {res_path}")

  def complete_cd(self,text, line, begidx, endidx):
    #groups=self.groups
    if text.startswith("/"):
      groups=self.kpdb.get_groups_from_root()
    else:
      groups=self.kpdb.get_groups_from_pwd()
    if not text:
      completions=groups[:]
    else:
      completions=[c for c in groups if c.startswith(text)]
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

  def do_exit(self, line):
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
    InterLoop(self.kpdb_obj).cmdloop()
    self.kpdb_obj.close_kpdb()
    


    
    
