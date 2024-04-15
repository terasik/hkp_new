"""
modul für allgmeine kofiguration 
logging, default werte
"""
import logging

class HkpLog:
  """
  logging logging
  """
  STREAM_HANDLER_NR=1
  def __init__(self):
    self.stream_handler_nr=0
    self.file_handler_nr=1
    self.log_handlers=[]
    self._config_stream_handler()
    self._init_root_logger()

  def _init_root_logger(self):
    """ init root (hkp) logger """
    logging.basicConfig(level=logging.DEBUG, handlers=self.log_handlers)

  def _config_stream_handler(self):
    """ konfig console handler """
    log_stream_handler=logging.StreamHandler()
    log_stream_handler.setLevel(logging.INFO)
    log_form=logging.Formatter('%(asctime)s %(levelname)s [%(module)-5s %(funcName)-15s] %(message)s')
    log_stream_handler.setFormatter(log_form)
    self.log_handlers.append(log_stream_handler)

  def set_stream_loglevel(self, level):
    """ setze console loglevel """
    self.log_handlers[self.stream_handler_nr].setLevel(level)
 
  def set_file_loglevel(self,level):
    """ setze file loglevel """
    self.log_handlers[self.file_handler_nr].setLevel(level)

class HkpDefs:
  """
  einige defaultwerte
  """
  kpdb='kdbx/uut.kdbx'
  sub_cmd='show'
  silent=False
  debug=False
  readonly=False
