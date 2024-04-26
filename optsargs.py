# PYTHON_ARGCOMPLETE_OK
"""
modul zum einlesen/bearbeiten der kommandozeilenargumente
"""

import argparse
import argcomplete
from version import version
from configs import HkpDefs
from subcmds.show import HkpShowCmd

class HkpOpts:
  """ klasse zum einlesen der arg optionen"""
  def __init__(self):
    opts_parser=argparse.ArgumentParser(prog='hkp', description='handle keepass', epilog='do sth with keepass')
    opts_parser.add_argument('-V', '--version', action="version", version=version)
    self._init_subparsers(opts_parser)
    self.opts_parser=opts_parser
    self.opts=None

  def _add_common_args(self, subparser):
    """ füge gemeinsame optionen einem parser hinzu """
    # debug Option
    subparser.add_argument("-d", "--debug", help="gib mir mehr", action="store_true", default=HkpDefs.debug)
    subparser.add_argument('-k', '--kpdb', required=False, help='pfad zu keepass datei', metavar="<KDBX>", default=HkpDefs.kpdb)
    

  def _init_subparsers(self, opts_parser):
    """initialisiere sub parser"""
    subparsers=opts_parser.add_subparsers(title='subcmds')
    self._init_show_subparser(subparsers)
    self._init_inter_subparser(subparsers)
    argcomplete.autocomplete(opts_parser)

  def _init_show_subparser(self, subparsers):
    """init subparser für aktion show"""
    p_show=subparsers.add_parser('show', help="show aktion", aliases=[])
    p_show.add_argument('hosts', metavar="HOSTS", nargs='+', help="zeige user/password daten für diese hosts")
    p_show.set_defaults(sub_cmd="show")
    p_show.set_defaults(readonly=True)
    p_show.set_defaults(cmd_class=HkpShowCmd)
    self._add_common_args(p_show)

  def _init_inter_subparser(self, subparsers):
    """init subparser für aktion inter"""
    p_inter=subparsers.add_parser('interactive', help="inter aktion", aliases=[])
    p_inter.add_argument('-r', '--readonly', action='store_true', help='nur lesender zugriff')
    p_inter.set_defaults(sub_cmd="interactive")
    self._add_common_args(p_inter)
     
  def parse_opts(self):
    """parse cmd argumente"""
    opts=self.opts_parser.parse_args()
    #print(opts)
    self.opts=opts
    return vars(opts)

  def post_parse_opts(self, opts):
    """bearbeite geparste opts"""
    return True

if __name__ == "__main__":
  o=HkpOpts()
  o.parse_opts()

