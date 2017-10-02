import wx
import wx.lib.newevent
import sqlite3
import os
import pymysql
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler
from ObjectListView import ObjectListView, ColumnDefn, OLVEvent
from wx.lib.mixins import inspection
from functools import partial
from GUI import *
from ServerAddGUI import *
# Add this to the GUI.py file:  from MyObjectListView import *

## To Do
## 


currentVersion = '1.0'
MyAppDir = os.path.join(os.path.expanduser('~'), '.LucidDev')
ThisAppDir = os.path.join(MyAppDir, 'KodiDBeditor')
LogDir = os.path.join(ThisAppDir, 'logs')
logFile = os.path.join(LogDir, 'KodiDBeditor.log')
settingsDB = os.path.join(ThisAppDir, 'settings.db')




class addServerFrame (serverAddFrame):
   ## Dialog frame to add the MySQL server details
   
   def onServerAddSubmit( self, event ):
      try:
         serverName = self.serverNameBox.GetValue()
         serverIP = self.serverIPbox.GetValue()
         serverPort = self.serverPortBox.GetValue()
         serverUser = self.serverUserBox.GetValue()
         serverPasswd = self.serverPasswdBox.GetValue()
         if serverName == "":
            dlg = wx.MessageDialog(self, 'You forgot to add the server name!', 'No Server Name', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
         elif serverIP == "":
            dlg = wx.MessageDialog(self, 'You forgot to add the IP!', 'No IP', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
         elif serverPort == "":
            dlg = wx.MessageDialog(self, 'You forgot to add the port!', 'Invalid Port', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
         elif not serverPort.isdigit():
            dlg = wx.MessageDialog(self, 'The port should be a number!', 'No Port', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
         elif serverUser == "":
            dlg = wx.MessageDialog(self, 'You forgot to add the username!', 'No Username', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
         elif serverPasswd == "":
            dlg = wx.MessageDialog(self, 'You forgot to add the password!', 'No Password', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
         else:
            try:
               self.Conn = sqlite3.connect(settingsDB)
               self.CURSOR = self.Conn.cursor()
               if self.EDIT:
                  logging.debug('Deleting existing server entry')
                  self.CURSOR.execute('delete from SQLservers where NAME = "%s"' % self.ORIGNAME)
               logging.debug('Adding new server entry')
               self.CURSOR.execute('INSERT INTO SQLservers (NAME, IP, PORT, USER, PASSWD) VALUES ("%s","%s","%d","%s","%s")' % (serverName,str(serverIP),int(serverPort),str(serverUser),str(serverPasswd)))
               self.Conn.commit()
               logging.info('Successfully added a new MySQL server')
               self.CURSOR.execute('select * from SQLservers;')
               servers = self.CURSOR.fetchall()
               if len(servers) == 1:
                  logging.info('Connecting to %s MySQL server' % servers[0][0])
                  self.FRAME.statusBar.SetStatusText('Connected to %s' % servers[0][0])
                  try:
                     logging.debug('Host = %s, Port = %s, User = %s, Password = %s' % (str(servers[0][1]), servers[0][2], servers[0][3], servers[0][4]))
                     self.FRAME.mysqlConn = pymysql.connect(host=servers[0][1], port=servers[0][2], user=servers[0][3], passwd=servers[0][4], charset='utf8')
                     self.FRAME.C = self.FRAME.mysqlConn.cursor()
                     sql = 'show databases'
                     self.FRAME.C.execute(sql)
                     databases = self.FRAME.C.fetchall()
                     videoDatabases = []
                     for database in databases:
                        if database[0].startswith('MyVideo'):
                           videoDatabases.append(database[0])
                     logging.debug('The following databases are available %s' % str(videoDatabases))
                     if len(videoDatabases) > 1:
                        DBmenuItems = []
                        for db in videoDatabases:
                           DBmenuItems.append([wx.MenuItem( self.FRAME.dbSubMenu, wx.ID_ANY, db, wx.EmptyString, wx.ITEM_NORMAL ), db])
                        for item in DBmenuItems:
                           self.FRAME.dbSubMenu.AppendItem( item[0] )
                           self.FRAME.Bind( wx.EVT_MENU, partial(self.FRAME.onSwitchDB, item[1]), id = item[0].GetId() )
                     if len(videoDatabases) > 0:
                        logging.info('Will use the %s database' % videoDatabases[-1])
                        sql = 'use %s' % videoDatabases[-1]
                        self.FRAME.C.execute(sql)
                        self.FRAME.statusBar.SetStatusText('Connected to %s and using %s' % (servers[0][0], videoDatabases[-1]))
                        self.FRAME.refreshGenreList()
                        self.FRAME.refreshTagList()
                     else:
                        dlg = wx.MessageDialog(self.FRAME, 'There are no kodi video databases available on this MySQL server', 'No Databases Available', wx.OK)
                        dlg.ShowModal()
                        dlg.Destroy() 
                  except:
                     dlg = wx.MessageDialog(self.FRAME, 'Failed to connect to the MySQL database! See log %s for details' % logFile, 'Failed to Connect to MySQL', wx.OK)
                     dlg.ShowModal()
                     dlg.Destroy()
                     logging.exception('Failed to connect to the MySQL database')
               self.Destroy()
            except:
               logging.exception('Failed to add a new MySQL server')
               dlg = wx.MessageDialog(self.FRAME, 'Failed to add the mysql server. See log %s for details' % logFile, 'Failed To Add Server', wx.OK)
               dlg.ShowModal()
               dlg.Destroy()
               try:
                  self.Conn.close()
               except:
                  pass
      except:
         logging.exception('Unexpected Error')
         dlg = wx.MessageDialog(self.FRAME, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

         
class titleItem(object):
   ## Create objectListView object for movie/tvshow titles
   def __init__(self, item):
      try:
         self.ID = item[0]
         self.TITLE = item[1]
         self.TYPE = item[2]
      except:
         logging.exception('Failed to create title item')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

         
class genreItem(object):
   ## Create objectListView object for genres
   def __init__(self, item):
      try:
         self.ID = item[0]
         self.GENRE = item[1]
      except:
         logging.exception('Failed to create genre item')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

         
class tagItem(object):
   ## Create objectListView object for tags
   def __init__(self, item):
      try:
         self.ID = item[0]
         self.TAG = item[1]
      except:
         logging.exception('Failed to create tag item')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()


         
class KodiDBeditorFrame(MyFrame):

   def onSetupMYSQL( self, event ):
      ## Create initial MySQL server connection if non exists
      try:
         serverAddWin = addServerFrame(None)
         serverAddWin.EDIT = False
         serverAddWin.FRAME = self
         serverAddWin.Show(True)
      except:
         logging.exception('Failed to add MySQL server')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

   def onEditMYSQL( self, event ):
      ## Edit the MySQL server details
      try:
         self.Conn = sqlite3.connect(settingsDB)
         self.C = self.Conn.cursor()
         self.C.execute('select * from SQLservers;')
         servers = self.C.fetchall()
         self.Conn.close()
         serverAddWin = addServerFrame(None)
         serverAddWin.EDIT = True
         serverAddWin.FRAME = self
         serverAddWin.ORIGNAME = servers[0][0]
         serverAddWin.serverNameBox.SetValue(servers[0][0])
         serverAddWin.serverIPbox.SetValue(servers[0][1])
         serverAddWin.serverPortBox.SetValue(str(servers[0][2]))
         serverAddWin.serverUserBox.SetValue(servers[0][3])
         serverAddWin.serverPasswdBox.SetValue(servers[0][4])
         serverAddWin.Show(True)
      except:
         logging.exception('Failed to edit MySQL server')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

   def onSelectTitle(self,event):
      ## Called when a tvshow/movie is selected
      
      ## Get the selected item
      item = self.itemBox.GetSelectedObject()
      
      ## Get genres for the selected title
      if item.TYPE == 'tvshow':
         sql = 'select genre_id from genre_link where media_id = %s and media_type = "tvshow"'
      else:
         sql = 'select genre_id from genre_link where media_id = %s and media_type = "movie"'
      self.C.execute(sql, item.ID)
      matches = self.C.fetchall()
      itemGenres = []
      for match in matches:
         itemGenres.append(match[0])
         
      ## Get tags for the selected title if selection is movie
      if item.TYPE == 'tvshow':
         sql = 'select tag_id from tag_link where media_id = %s and media_type = "tvshow"'
      else:
         sql = 'select tag_id from tag_link where media_id = %s and media_type = "movie"'
      self.C.execute(sql, item.ID)
      matches = self.C.fetchall()
      itemTags = []
      for match in matches:
         itemTags.append(match[0])
      
      ## Clear the genre and tag boxes
      self.genreBox.Objects = None
      self.tagBox.Objects = None
      
      ## Re-popualte the genre box with the matching genres
      sql = 'select * from genre'
      self.C.execute(sql)
      genres = self.C.fetchall()
      results = []
      for genre in genres:
         results.append(genreItem([genre[0],genre[1]]))
      self.genreBox.SetObjects(results)
      objects = self.genreBox.GetObjects()
      for object in objects:
         if object.ID in itemGenres:
            self.genreBox.SetCheckState(object, True)
      self.genreBox.RefreshObjects(objects)
      
      ## Re-popluate the tag box with matching sets if selection is movie
      sql = 'select * from tag'
      self.C.execute(sql)
      tags = self.C.fetchall()
      results = []
      for tag in tags:
         results.append(tagItem([tag[0],tag[1]]))
      self.tagBox.SetObjects(results)
      objects = self.tagBox.GetObjects()
      for object in objects:
         if object.ID in itemTags:
            self.tagBox.SetCheckState(object, True)
      self.tagBox.RefreshObjects(objects)
      
      ## Setup tooltip for movies
      if item.TYPE == 'movie':
         sql = 'select C12,C01 from movie where idMovie=%s'
         self.C.execute(sql, item.ID)
         Movie = self.C.fetchall()[0]
         msg = '%s\n%s' % (Movie[0],Movie[1])
         event.GetEventObject().SetToolTipString(msg)
         event.Skip()
      else:
         msg = ''
         event.GetEventObject().SetToolTipString(msg)
         event.Skip()
         
   def onDeleteGenre( self, event ):
      ## Delete the selected genre
      try:
         genre = self.genreBox.GetSelectedObject()
         if genre:
            logging.info('Attempting to delete genre %s' % genre.GENRE)
            sql = 'select media_id,media_type from genre_link where genre_id=%s'
            self.C.execute(sql, genre.ID)
            matches = self.C.fetchall()
            if len(matches) > 0:
               logging.info('There are still some titles using this genre that you are trying to delete\n%s' % str(matches))
               self.itemBox.Objects = None
               results = []
               for match in matches:
                  if match[1] == 'tvshow':
                     sql = 'select idShow,C00 from tvshow where idShow=%s'
                  else:
                     sql = 'select idMovie,C00 from movie where idMovie=%s'
                  self.C.execute(sql, match[0])
                  titles = self.C.fetchall()
                  for title in titles:
                     results.append(titleItem([title[0],title[1],match[1]]))
               self.itemBox.SetObjects(results)
               dlg = wx.MessageDialog(self, 'The genre that you selected to delete is still in use. The titles shown on the left use this genre. Do you want to remove this genre from those titles and then delete this genre?', 'Genre In Use', wx.YES_NO | wx.ICON_QUESTION)
               result = dlg.ShowModal() == wx.ID_YES
               dlg.Destroy()
               if result:
                  logging.info('Going to start removing this genre from these titles that still use it')
                  for match in matches:
                     if match[1] == 'tvshow':
                        sql = 'delete from genre_link where media_id="%s" and media_type="tvshow" and genre_id=%s'
                     else:
                        sql = 'delete from genre_link where media_id="%s" and media_type="movie" and genre_id=%s'
                     logging.debug('Deleting genre, step 1 - remove this genre for this title in genre_link')
                     self.C.execute(sql, (match[0],genre.ID))
                     logging.debug('Deleting genre, step 2 - replace genre list of this title')
                     genreList = []
                     sql = 'select genre_id from genre_link where media_id=%s and media_type=%s'
                     self.C.execute(sql, (match[0],match[1]))
                     genreIDs = self.C.fetchall()
                     for genreID in genreIDs:
                        sql = 'select name from genre where genre_id=%s'
                        self.C.execute(sql, genreID)
                        genreNames = self.C.fetchall()
                        for genreName in genreNames:
                           genreList.append(genreName[0])
                     if match[1] == 'tvshow':
                        sql = 'update tvshow set C08="%s" where idShow="%s"'
                        self.C.execute(sql, (" / ".join(genreList), match[0]))
                     else:
                        sql = 'update movie set C14="%s" where idMovie="%s"'
                        self.C.execute(sql, (" / ".join(genreList), match[0]))
                  logging.info('Removing genre from the genre table and updating the genre list')
                  sql = 'delete from genre where genre_id=%s'
                  self.C.execute(sql, genre.ID)
                  sql = 'select * from genre'
                  self.C.execute(sql)
                  matches = self.C.fetchall()
                  if len(matches) > 0:
                     results = []
                     for match in matches:
                        results.append(genreItem([match[0],match[1]]))
                     self.genreBox.SetObjects(results)
                  self.mysqlConn.commit()
               else:
                  logging.info('Genre deletion canceled')
      except:
         logging.exception('Failed to delete genre')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
      
   def onDeleteTag( self, event ):
      ## Delete the selected tag
      try:
         tag = self.tagBox.GetSelectedObject()
         if tag:
            logging.info('Attempting to delete tag %s' % tag.TAG)
            sql = 'select media_id,media_type from tag_link where tag_id=%s'
            self.C.execute(sql, tag.ID)
            matches = self.C.fetchall()
            if len(matches) > 0:
               logging.info('There are still some titles using this tag that you are trying to delete\n%s' % str(matches))
               self.itemBox.Objects = None
               results = []
               for match in matches:
                  if match[1] == 'tvshow':
                     sql = 'select idShow,C00 from tvshow where idShow=%s'
                  else:
                     sql = 'select idMovie,C00 from movie where idMovie=%s'
                  self.C.execute(sql, match[0])
                  titles = self.C.fetchall()
                  for title in titles:
                     results.append(titleItem([title[0],title[1],match[1]]))
               self.itemBox.SetObjects(results)
               dlg = wx.MessageDialog(self, 'The tag that you selected to delete is still in use. The titles shown on the left use this tag. Do you want to remove this tag from those titles and then delete this tag?', 'Tag In Use', wx.YES_NO | wx.ICON_QUESTION)
               result = dlg.ShowModal() == wx.ID_YES
               dlg.Destroy()
               if result:
                  logging.info('Going to start removing this tag from these titles that still use it')
                  for match in matches:
                     if match[1] == 'tvshow':
                        sql = 'delete from tag_link where media_id="%s" and media_type="tvshow" and tag_id=%s'
                     else:
                        sql = 'delete from tag_link where media_id="%s" and media_type="movie" and tag_id=%s'
                     logging.debug('Remove this tag for this title in tag_link')
                     self.C.execute(sql, (match[0],tag.ID))
                  logging.info('Removing tag from the tag table and updating the tag list')
                  sql = 'delete from tag where tag_id=%s'
                  self.C.execute(sql, tag.ID)
                  self.refreshTagList()
                  self.mysqlConn.commit()
               else:
                  logging.info('Tag deletion canceled')
      except:
         logging.exception('Failed to delete tag')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
 
   def onSwitchDB( self, db, event ):
      ## Switch to a different Kodi database in case there is more than one (after upgrading). The highest version database should be selected by default
      try:
         self.CURSOR.execute('select * from SQLservers;')
         servers = self.CURSOR.fetchall()
         logging.info('Switching to the %s database' % db)
         sql = 'use %s' % db
         self.C.execute(sql)
         self.statusBar.SetStatusText('Connected to %s and using %s' % (servers[0][0], db))
         self.refreshGenreList()
         self.refreshTagList()
      except:
         logging.exception('Failed to switch databases')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

   def onRetrieve( self, event ):
      ## Get either tvshows or movies based on the combo box selection and display them in the itemBox
      try:
         if self.displayCombo.GetSelection() == 0:
            sql = 'select idShow,C00 from tvshow'
            media_type = 'tvshow'
         else:
            sql = 'select idMovie,C00 from movie'
            media_type = 'movie'
         self.C.execute(sql)
         titles = self.C.fetchall()
         if len(titles) > 0:
            results = []
            for title in titles:
               results.append(titleItem([title[0],title[1],media_type]))
            self.itemBox.SetObjects(results)
         self.refreshGenreList()
         self.refreshTagList()
      except:
         logging.exception('Failed to retrieve titles')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
      
   def OnAddGenre( self, event ):
      ## Add a new genre to the list
      try:
         newGenre = self.newGenreBox.GetValue()
         logging.info('Attempting to add new genre %s' % newGenre)
         if newGenre == "":
            dlg = wx.MessageDialog(self, 'You forgot to type a genre name in the box!', 'No Genre Name', wx.OK)
            logging.info('You forgot to type a genre name in the box!')
            dlg.ShowModal()
            dlg.Destroy()
         else:
            sql = 'select name from genre'
            self.C.execute(sql)
            genres = []
            for genre in self.C.fetchall():
               genres.append(genre[0])
            if newGenre in genres:
               dlg = wx.MessageDialog(self, 'The genre you are trying add already exists!', 'Genre Already Exists', wx.OK)
               logging.info('The genre you are trying add already exists!')
               dlg.ShowModal()
               dlg.Destroy()
            else:
               sql = 'INSERT INTO genre (name) VALUES (%s)'
               self.C.execute(sql,newGenre)
               sql = 'select * from genre'
               self.C.execute(sql)
               genres = self.C.fetchall()
               results = []
               for genre in genres:
                  results.append(genreItem([genre[0],genre[1]]))
               self.genreBox.SetObjects(results)
               self.mysqlConn.commit()
               logging.info('New genre added')
      except:
         logging.exception('Failed to add new genre')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

   def OnAddTag( self, event ):
      ## Add a new tag to the list
      try:
         newTag = self.newTagBox.GetValue()
         logging.info('Attempting to add new tag %s' % newTag)
         if newTag == "":
            dlg = wx.MessageDialog(self, 'You forgot to type a tag name in the box!', 'No Tag Name', wx.OK)
            logging.info('You forgot to type a tag name in the box!')
            dlg.ShowModal()
            dlg.Destroy()
         else:
            sql = 'select name from tag'
            self.C.execute(sql)
            tags = []
            for tag in self.C.fetchall():
               tags.append(tag[0])
            if newTag in tags:
               dlg = wx.MessageDialog(self, 'The tag you are trying add already exists!', 'Tag Already Exists', wx.OK)
               logging.info('The tag you are trying add already exists!')
               dlg.ShowModal()
               dlg.Destroy()
            else:
               sql = 'INSERT INTO tag (name) VALUES (%s)'
               self.C.execute(sql,newTag)
               sql = 'select * from tag'
               self.C.execute(sql)
               tags = self.C.fetchall()
               results = []
               for tag in tags:
                  results.append(tagItem([tag[0],tag[1]]))
               self.tagBox.SetObjects(results)
               self.mysqlConn.commit()
               logging.info('New tag added')
      except:
         logging.exception('Failed to add new tag')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()

   def onUpdateGenres( self, event ):
      ## Make the genre changes for the selected title based on the current checkbox selections
      item = self.itemBox.GetSelectedObject()
      try:
         logging.info('Updating genres for %s' % item.TITLE)
         objects = self.genreBox.GetObjects()
         checked = []
         for object in objects:
            if self.genreBox.IsChecked(object):
               checked.append(object.ID)
         logging.debug('The selected genre IDs are %s' % str(checked))
         if len(checked) == 0:
            dlg = wx.MessageDialog(self, "You don't have any genres checked!", 'No Genres Selected', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
         else:
            if item.TYPE == 'tvshow':
               sql = 'delete from genre_link where media_id="%s" and media_type="tvshow"'
            else:
               sql = 'delete from genre_link where media_id="%s" and media_type="movie"'
            logging.debug('Updating genres, step 1 - remove all existing genre links for this title')
            self.C.execute(sql, item.ID)
            logging.debug('Updating genres, step 2 - add new genre links for this title')
            genreList = []
            if item.TYPE == 'tvshow':
               for entry in checked:
                  sql = 'INSERT INTO genre_link (genre_id, media_id, media_type) VALUES ("%s","%s",%s)'
                  self.C.execute(sql, (entry, item.ID, 'tvshow'))
                  sql = 'select name from genre where genre_id="%s"'
                  self.C.execute(sql, entry)
                  genres = self.C.fetchall()
                  for genre in genres:
                     genreList.append(genre[0])
            else:
               for entry in checked:
                  sql = 'INSERT INTO genre_link (genre_id, media_id, media_type) VALUES ("%s","%s",%s)'
                  self.C.execute(sql, (entry, item.ID, 'movie'))
                  sql = 'select name from genre where genre_id="%s"'
                  self.C.execute(sql, entry)
                  genres = self.C.fetchall()
                  for genre in genres:
                     genreList.append(genre[0])
            if item.TYPE == 'tvshow':
               sql = 'update tvshow set C08="%s" where idShow="%s"'
               self.C.execute(sql, (" / ".join(genreList), item.ID))
            else:
               sql = 'update movie set C14="%s" where idMovie="%s"'
               self.C.execute(sql, (" / ".join(genreList), item.ID))
            self.mysqlConn.commit()
      except:
         logging.exception('Failed to update genres')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
      
   def onUpdateTags( self, event ):
      ## Make the tag changes for the selected title based on the current checkbox selections
      item = self.itemBox.GetSelectedObject()
      try:
         logging.info('Updating tags for %s' % item.TITLE)
         objects = self.tagBox.GetObjects()
         checked = []
         for object in objects:
            if self.tagBox.IsChecked(object):
               checked.append(object.ID)
         logging.debug('The selected tag IDs are %s' % str(checked))
         if item.TYPE == 'tvshow':
            sql = 'delete from tag_link where media_id="%s" and media_type="tvshow"'
         else:
            sql = 'delete from tag_link where media_id="%s" and media_type="movie"'
         logging.debug('Updating tags, step 1 - remove all existing tag links for this title')
         self.C.execute(sql, item.ID)
         logging.debug('Updating tags, step 2 - add new tag links for this title')
         if item.TYPE == 'tvshow':
            for entry in checked:
               sql = 'INSERT INTO tag_link (tag_id, media_id, media_type) VALUES ("%s","%s",%s)'
               self.C.execute(sql, (entry, item.ID, 'tvshow'))
         else:
            for entry in checked:
               sql = 'INSERT INTO tag_link (tag_id, media_id, media_type) VALUES ("%s","%s",%s)'
               self.C.execute(sql, (entry, item.ID, 'movie'))
         self.mysqlConn.commit()
      except:
         logging.exception('Failed to update tags')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
      
   def onShowGenreTitles( self, event ):
      ## Show tvshow/movies titles that have the selected genre
      genre = self.genreBox.GetSelectedObject()
      try:
         logging.info('Getting titles for selected genre: %s' % genre.GENRE)
         sql = 'select media_id,media_type from genre_link where genre_id="%s"'
         self.C.execute(sql, genre.ID)
         matches = self.C.fetchall()
         self.itemBox.Objects = None
         results = []
         for match in matches:
            if match[1] == 'tvshow':
               sql = 'select idShow,C00 from tvshow where idShow="%s"'
            else:
               sql = 'select idMovie,C00 from movie where idMovie="%s"'
            self.C.execute(sql, match[0])
            titles = self.C.fetchall()
            for title in titles:
               results.append(titleItem([title[0],title[1],match[1]]))
         self.itemBox.SetObjects(results)
      except:
         logging.exception('Failed to retrieve titles for selected genre')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
         
   def onShowTagTitles( self, event ):
      ## Show tvshow/movies titles that have the selected tag
      tag = self.tagBox.GetSelectedObject()
      try:
         logging.info('Getting titles for selected tag: %s' % tag.TAG)
         sql = 'select media_id,media_type from tag_link where tag_id="%s"'
         self.C.execute(sql, tag.ID)
         matches = self.C.fetchall()
         self.itemBox.Objects = None
         results = []
         for match in matches:
            if match[1] == 'tvshow':
               sql = 'select idShow,C00 from tvshow where idShow="%s"'
            else:
               sql = 'select idMovie,C00 from movie where idMovie="%s"'
            self.C.execute(sql, match[0])
            titles = self.C.fetchall()
            for title in titles:
               results.append(titleItem([title[0],title[1],match[1]]))
         self.itemBox.SetObjects(results)
      except:
         logging.exception('Failed to retrieve titles for selected tag')
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
      
   def refreshTagList( self ):
      ## Refresh the list of tags from the databse. Called by other procedures
      sql = 'select * from tag'
      self.C.execute(sql)
      tags = self.C.fetchall()
      if len(tags) > 0:
         results = []
         for tag in tags:
            results.append(tagItem([tag[0],tag[1]]))
         self.tagBox.SetObjects(results)
      
   def refreshGenreList( self ):
      ## Refresh the list of genres from the databse. Called by other procedures
      sql = 'select * from genre'
      self.C.execute(sql)
      genres = self.C.fetchall()
      if len(genres) > 0:
         results = []
         for genre in genres:
            results.append(genreItem([genre[0],genre[1]]))
         self.genreBox.SetObjects(results)
      
   def searchMovieByRating(self, rating):
      ## Display movie titles based on the supplied rating. Called by the rating search menu items
      try:
         logging.info('Getting rated %s movies' % rating)
         sql = 'select idMovie,C00 from movie where C12=%s'
         self.C.execute(sql, 'Rated %s' % rating)
         matches = self.C.fetchall()
         self.itemBox.Objects = None
         results = []
         for match in matches:
            results.append(titleItem([match[0],match[1],'movie']))
         self.itemBox.SetObjects(results)
      except:
         logging.exception('Failed to retrieve rated %s movies' % rating)
         dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
      
   def onSearchG( self, event ):
      ## Find G rated Movies
      self.searchMovieByRating('G')

   def onSearchPG( self, event ):
      ## Find PG rated Movies
      self.searchMovieByRating('PG')

   def onSearchPG13( self, event ):
      ## Find PG13 rated Movies
      self.searchMovieByRating('PG-13')

   def onSearchR( self, event ):
      ## Find R rated Movies
      self.searchMovieByRating('R')
      

      
def start():
   
   ## Start program:
   app = wx.App(False)
   #app = inspection.InspectableApp(0)
   frame = KodiDBeditorFrame(None)
   frame.SetTitle("Kodi Genre/Tag Manager    version " + currentVersion)
   
   ## Setup tvshow/movie Title box for objectListView
   TitleColumn = ColumnDefn("Title/Show", "left", 100, "TITLE", isSpaceFilling=True)
   frame.itemBox.SetColumns([
      TitleColumn
      ])
   frame.itemBox.SetEmptyListMsg("")
   frame.itemBox.Bind(wx.EVT_LIST_ITEM_SELECTED, frame.onSelectTitle)
   frame.itemBox.SetSortColumn(TitleColumn)

   ## Setup genre box for objectListView
   genreColumn = ColumnDefn("Genre", "left", 100, "GENRE", isSpaceFilling=True)
   frame.genreBox.SetColumns([
      genreColumn
      ])
   frame.genreBox.SetEmptyListMsg("")
   frame.genreBox.CreateCheckStateColumn()
   frame.genreBox.SetSortColumn(genreColumn)
   
   ## Setup tag box for objectListView
   tagColumn = ColumnDefn("Tag", "left", 100, "TAG", isSpaceFilling=True)
   frame.tagBox.SetColumns([
      tagColumn
      ])
   frame.tagBox.SetEmptyListMsg("")
   frame.tagBox.CreateCheckStateColumn()
   frame.tagBox.SetSortColumn(tagColumn)
   
   ## Load/create Settings DB file
   try:
      if os.path.isfile(settingsDB):
         try:
            frame.Conn = sqlite3.connect(settingsDB)
            frame.CURSOR = frame.Conn.cursor()
            frame.CURSOR.execute('select * from SQLservers;')
         except:
            logging.exception('Failed while connecting to the settingsDB, it may be corrupt')
            dlg = wx.MessageDialog(frame, 'The settings file for this program seems to be corrupt, would you like to create a new one?', 'Unable to open settings file', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal() == wx.ID_YES
            dlg.Destroy()
            if result:
               try:
                  frame.Conn.close()
                  os.remove(settingsDB)
               except:
                  logging.exception('Failed while trying to delete the settings file')
                  dlg = wx.MessageDialog(frame, "Could not overwrite file %s, is it open somewhere?" % settingsDB, "Unble to Delete Settings File", wx.OK)
                  dlg.ShowModal()
                  dlg.Destroy()
                  frame.Destroy()
               logging.info('Creating a new settingsDB file')
               frame.Conn = sqlite3.connect(settingsDB)
               frame.CURSOR = frame.Conn.cursor()
               frame.CURSOR.execute('''CREATE TABLE SQLservers
                                 (NAME TEXT,
                                  IP TEXT,
                                  PORT INTEGER,
                                  USER TEXT,
                                  PASSWD TEXT);''')
               frame.Conn.commit()          
            else:
               logging.info('User decided to not create a new settingsDB, closing the program')
               dlg = wx.MessageDialog(frame, "It's been fun! Hope you get that figured out", "Database not valid", wx.OK)
               dlg.ShowModal()
               dlg.Destroy()
               frame.Destroy()
      else:
         logging.info('Creating a new settingsDB file')
         frame.Conn = sqlite3.connect(settingsDB)
         frame.CURSOR = frame.Conn.cursor()
         frame.CURSOR.execute('''CREATE TABLE SQLservers
                           (NAME TEXT,
                            IP TEXT,
                            PORT INTEGER,
                            USER TEXT,
                            PASSWD TEXT);''')
         frame.Conn.commit()
      frame.CURSOR.execute('select * from SQLservers;')
      servers = frame.CURSOR.fetchall()
      logging.debug('MySQL Server List is %s' % str(servers))
   except:
      logging.exception('Failed while loading/creating settings file')
      dlg = wx.MessageDialog(self, 'Hit an unexpected error. See log %s for details' % logFile, 'Unexpected Error', wx.OK)
      dlg.ShowModal()
      dlg.Destroy()

   ## Show the frame
   frame.Show(True)
   
   ## Connect/Setup MySQL server
   if len(servers) == 0:
      frame.onSetupMYSQL(frame)
   else:
      logging.info('Connecting to %s MySQL server' % servers[0][0])
      try:
         logging.debug('Host = %s, Port = %s, User = %s, Password = %s' % (str(servers[0][1]), servers[0][2], servers[0][3], servers[0][4]))
         frame.mysqlConn = pymysql.connect(host=servers[0][1], port=servers[0][2], user=servers[0][3], passwd=servers[0][4], charset='utf8')
         frame.C = frame.mysqlConn.cursor()
         sql = 'show databases'
         frame.C.execute(sql)
         databases = frame.C.fetchall()
         videoDatabases = []
         for database in databases:
            if database[0].startswith('MyVideo'):
               videoDatabases.append(database[0])
         logging.debug('The following databases are available %s' % str(videoDatabases))
         if len(videoDatabases) > 1:
            DBmenuItems = []
            for db in videoDatabases:
               DBmenuItems.append([wx.MenuItem( frame.dbSubMenu, wx.ID_ANY, db, wx.EmptyString, wx.ITEM_NORMAL ), db])
            for item in DBmenuItems:
               frame.dbSubMenu.AppendItem( item[0] )
               frame.Bind( wx.EVT_MENU, partial(frame.onSwitchDB, item[1]), id = item[0].GetId() )
         if len(videoDatabases) > 0:
            logging.info('Will use the %s database' % videoDatabases[-1])
            sql = 'use %s' % videoDatabases[-1]
            frame.C.execute(sql)
            frame.statusBar.SetStatusText('Connected to %s and using %s' % (servers[0][0], videoDatabases[-1]))
            frame.refreshGenreList()
            frame.refreshTagList()
         else:
            dlg = wx.MessageDialog(frame, 'There are no kodi video databases available on this MySQL server', 'No Databases Available', wx.OK)
            dlg.ShowModal()
            dlg.Destroy() 
      except:
         dlg = wx.MessageDialog(frame, 'Failed to connect to the MySQL database! See log %s for details' % logFile, 'Failed to Connect to MySQL', wx.OK)
         dlg.ShowModal()
         dlg.Destroy()
         logging.exception('Failed to connect to the MySQL database')
   
   ## Start the GUI loop[
   app.MainLoop()



if __name__ == "__main__":
   
   ## Make directories
   if not os.path.exists(MyAppDir):
      os.makedirs(MyAppDir)
   if not os.path.exists(ThisAppDir):
      os.makedirs(ThisAppDir)
   if not os.path.exists(LogDir):
      os.makedirs(LogDir)
   
   ## Setup Logging
   handler = RotatingFileHandler(logFile, maxBytes=10485760, backupCount=5)
   formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s')
   handler.setFormatter(formatter)
   logger = logging.getLogger()
   logger.addHandler(handler)
   logger.setLevel(logging.DEBUG)
   logging.info('Starting up')
   start()