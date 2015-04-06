from django.db import models

class Share(models.Model):
  name = models.CharField(max_length=64)
  path = models.CharField(max_length=4096)
  def __str__(self):
    return "{0} : {1}".format(self.name,self.path)

class File(models.Model):
  share = models.ForeignKey('Share')
  directory = models.CharField(max_length=4096,db_index=True)
  name = models.CharField(max_length=4096)
  def __str__(self):
    return "{0} - {1} : {2}".format(self.share,self.directory,self.name)
  

class Setting(models.Model):
  key = models.CharField(max_length=4096,db_index=True)
  value = models.CharField(max_length=4096)
  def __str__(self): 
    return "{0}".format(self.key)

class Peer(models.Model):
  uid = models.CharField(max_length=64,db_index=True)
  local_nickname = models.CharField(max_length=4096)
  remote_nickname  = models.CharField(max_length=4096)
  enabled = models.BooleanField()

  hostname = models.CharField(max_length=4096)
  port = models.IntegerField()

  dynamic = models.BooleanField()

  client_key = models.CharField(max_length=4096)
  server_key = models.CharField(max_length=4096)
  def __str__(self): 
    return "{0} -- {1} @ {2}:{3}".format(self.uid,self.local_nickname,self.hostname,self.port)
