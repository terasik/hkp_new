"""
modul für bearbeitung der show aktion
"""

class HkpShowCmd:
  """ klasse für show aktion """
  def __init__(self, opts):
    opts_vars=vars(opts)
    self._get_opts_dict(opts_vars)

  def _get_opts_dict(self, opts_vars):
    """ funktion die dict zurückliefert """
    opts_dict={
    
    
