from defaults import defaults

class kpdb(defaults):
  """
  handle keepass files
  """
  def __init__(self):
    super().__init__()


  def open_kpdb(self):
    self.logger.info(f"open kpdb {self.kpdb}")

    

