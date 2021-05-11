# Assuming all banks place their daily reports in one of the common ftp location.
class FTPConnector(object)
  def __init__(self, config, directory):
    self.directory = directory
    self.config = config
   
  def __enter__():
    self.ftp = self.getConnection()
    return self
  
  def __exit__():
    self.ftp.close()
    
 def getConnection(self):
    ftp = connect(self.config)
    ftp.cwd(self.directory)
    return ftp
