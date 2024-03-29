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
    #logger=logging.getLogger('hkp')
    #logger.setLevel(logging.DEBUG)
    #self.logger=logger
    logging.basicConfig(level=logging.DEBUG, handlers=self.log_handlers)

  def _config_stream_handler(self):
    """ konfig console handler """
    log_stream_handler=logging.StreamHandler()
    log_stream_handler.setLevel(logging.INFO)
    log_form=logging.Formatter('%(asctime)s %(levelname)s [%(module)s %(funcName)s %(name)s] %(message)s')
    log_stream_handler.setFormatter(log_form)
    self.log_handlers.append(log_stream_handler)

  def set_console_loglevel(self, level):
    """ setze console loglevel """
    self.log_handlers[0].setLevel(level)
   
  def set_file_loglevel(self,level):
    """ setze file loglevel """
    self.log_handlers[1].setLevel(level)

 
class HkpDefs:
  """
  some defaults
  """
  kpdb_def='kdbx/uut.kdbx'
  host_def='myhost'
  sub_cmd_def='show'
  silent=False
  debug=False
  readonly=False

