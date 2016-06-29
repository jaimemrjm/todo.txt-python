# Object representing a todo
class Todo:
  data = {}

  def __init__(self, data = None):
      self.data['tags'] = []
      self.data['created'] = None
      self.data['due'] = None
      self.data['threshold'] = None
      if data:
          self.setData(data)

  def setData(self, data):
    self.data = data

  def getData(self):
    return self.data

  def getDescription(self):
    return self.data['description']

  def getProject(self):
    return self.data['project']

  def setProject(self, project):
    self.data['project'] = project

  def getContext(self):
    return self.data['context']

  def setContext(self, context):
    self.data['context'] = context

  def setDueDate(self, date):
      self.data['due'] = date

  def getDueDate(self):
      if 'due' in self.data:
          return self.data['due']
      else:
          return None

  def setThreshold(self, date):
      self.data['threshold'] = date

  def getThreshold(self):
      if 'threshold' in self.data:
          return self.data['threshold']
      else:
          return None

  def getCreationDate(self):
      if 'created' in self.data:
          return self.data['created']
      else:
          return None

  def setCreationDate(self, date):
      self.data['created'] = date

  def getTracksId(self):
    return self.data['tracks_id']

  def setTracksId(self, tracks_id):
    if tracks_id == None:
      self.data['tracks_id'] = None
    else:
      self.data['tracks_id'] = str(tracks_id)

  def isDone(self):
    return self.data['done']

  def setDone(self, done = True):
    self.data['done'] = done

  def setTags(self, tags):
      self.data['tags'] = tags

  def getTags(self):
      if 'tags' in self.data:
          return self.data['tags']
      else:
          return []

  def getCompletedDate(self):
    if 'completed' in self.data:
      return self.data['completed']
    else:
      return None

  def setCompletedDate(self, date):
    self.data['completed'] = date

  def getTextLine(self):
    '''
    Returns a line (string) that represent this Todo object in todo.txt format
    see Parser.makeTodoLine(data) also
    '''
    line = ''
    if self.isDone() == True:
      line += 'x '
    if self.getCompletedDate() != None:
      line += self.getCompletedDate() + ' '
    if self.getCreationDate() != None:
      line += self.getCreationDate() + ' '
    line += self.getDescription()
    if self.getDueDate() != None:
      line += ' due:' + self.getDueDate()
    if self.getThreshold() != None:
      line += ' t:' + self.getThreshold()
    if self.getContext() != 'default':
      line += ' @' + self.getContext()
    if self.getProject() != 'default':
      line += ' +' + self.getProject()
    if self.getTags() != [] and self.getTags() != None:
        for tag in self.getTags():
            line += ' +' + tag
    if self.getTracksId() != None:
      line += ' tid:' + self.getTracksId()

    return line
