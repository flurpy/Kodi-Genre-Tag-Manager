# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from MyObjectListView import *

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1107,668 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menuBar = wx.MenuBar( 0 )
		self.menuBar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.menuBar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.menu_DB = wx.Menu()
		self.dbSubMenu = wx.Menu()
		self.menu_DB.AppendSubMenu( self.dbSubMenu, u"Switch to Different Database" )
		
		self.menuItemEditServer = wx.MenuItem( self.menu_DB, wx.ID_ANY, u"Edit MySQL Server", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_DB.AppendItem( self.menuItemEditServer )
		
		self.menuBar.Append( self.menu_DB, u"Kodi Database" ) 
		
		self.menu_SearchFor = wx.Menu()
		self.menuItemG = wx.MenuItem( self.menu_SearchFor, wx.ID_ANY, u"G Movies", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_SearchFor.AppendItem( self.menuItemG )
		
		self.menuItemPG = wx.MenuItem( self.menu_SearchFor, wx.ID_ANY, u"PG Movies", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_SearchFor.AppendItem( self.menuItemPG )
		
		self.menuItemPG13 = wx.MenuItem( self.menu_SearchFor, wx.ID_ANY, u"PG-13 Movies", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_SearchFor.AppendItem( self.menuItemPG13 )
		
		self.menuItemR = wx.MenuItem( self.menu_SearchFor, wx.ID_ANY, u"R Movies", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_SearchFor.AppendItem( self.menuItemR )
		
		self.menuBar.Append( self.menu_SearchFor, u"Search For..." ) 
		
		self.menu_KodiConnection = wx.Menu()
		self.menuItem_setupKodi = wx.MenuItem( self.menu_KodiConnection, wx.ID_ANY, u"Setup Kodi Connection", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_KodiConnection.AppendItem( self.menuItem_setupKodi )
		
		self.submenu_kodiConnection = wx.Menu()
		self.menu_KodiConnection.AppendSubMenu( self.submenu_kodiConnection, u"Connect To:" )
		
		self.menuItem_deleteKodi = wx.MenuItem( self.menu_KodiConnection, wx.ID_ANY, u"Delete Current Connection", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_KodiConnection.AppendItem( self.menuItem_deleteKodi )
		self.menuItem_deleteKodi.Enable( False )
		
		self.menuItem_editKodi = wx.MenuItem( self.menu_KodiConnection, wx.ID_ANY, u"Edit Current Connection", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_KodiConnection.AppendItem( self.menuItem_editKodi )
		self.menuItem_editKodi.Enable( False )
		
		self.menuItem_updateKodi = wx.MenuItem( self.menu_KodiConnection, wx.ID_ANY, u"Update Library", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_KodiConnection.AppendItem( self.menuItem_updateKodi )
		self.menuItem_updateKodi.Enable( False )
		
		self.menuItem_cleanKodi = wx.MenuItem( self.menu_KodiConnection, wx.ID_ANY, u"Clean Library", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_KodiConnection.AppendItem( self.menuItem_cleanKodi )
		self.menuItem_cleanKodi.Enable( False )
		
		self.menuItem_exportKodi = wx.MenuItem( self.menu_KodiConnection, wx.ID_ANY, u"Export Library To Files", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_KodiConnection.AppendItem( self.menuItem_exportKodi )
		self.menuItem_exportKodi.Enable( False )
		
		self.menuBar.Append( self.menu_KodiConnection, u"Kodi Connection" ) 
		
		self.SetMenuBar( self.menuBar )
		
		parentSizer = wx.BoxSizer( wx.VERTICAL )
		
		
		parentSizer.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		self.splitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3DBORDER )
		self.splitter.Bind( wx.EVT_IDLE, self.splitterOnIdle )
		
		self.panelLeft = wx.Panel( self.splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerLeftPanel = wx.BoxSizer( wx.VERTICAL )
		
		
		sizerLeftPanel.AddSpacer( ( 0, 10), 0, 0, 5 )
		
		sizerDisplayChooser = wx.BoxSizer( wx.HORIZONTAL )
		
		
		sizerDisplayChooser.AddSpacer( ( 5, 0), 0, 0, 5 )
		
		self.textDisplay = wx.StaticText( self.panelLeft, wx.ID_ANY, u"Display: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textDisplay.Wrap( -1 )
		sizerDisplayChooser.Add( self.textDisplay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		displayComboChoices = [ u"TV Shows", u"Movies" ]
		self.displayCombo = wx.ComboBox( self.panelLeft, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, displayComboChoices, 0 )
		self.displayCombo.SetSelection( 0 )
		sizerDisplayChooser.Add( self.displayCombo, 0, wx.ALL, 5 )
		
		self.buttonRetrieve = wx.Button( self.panelLeft, wx.ID_ANY, u"Retreive", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerDisplayChooser.Add( self.buttonRetrieve, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sizerLeftPanel.Add( sizerDisplayChooser, 0, 0, 5 )
		
		self.itemBox = MyOvl( self.panelLeft, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sizerLeftPanel.Add( self.itemBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelLeft.SetSizer( sizerLeftPanel )
		self.panelLeft.Layout()
		sizerLeftPanel.Fit( self.panelLeft )
		self.panelRight = wx.Panel( self.splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerRightPanel = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerGenre = wx.StaticBoxSizer( wx.StaticBox( self.panelRight, wx.ID_ANY, u"Genres" ), wx.VERTICAL )
		
		genreFilterSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radio_OnlyTVgenres = wx.RadioButton( sizerGenre.GetStaticBox(), wx.ID_ANY, u"Only TV Genres", wx.DefaultPosition, wx.DefaultSize, 0 )
		genreFilterSizer.Add( self.radio_OnlyTVgenres, 0, wx.ALL, 5 )
		
		self.radio_OnlyMoviesGenres = wx.RadioButton( sizerGenre.GetStaticBox(), wx.ID_ANY, u"Only Movie Genres", wx.DefaultPosition, wx.DefaultSize, 0 )
		genreFilterSizer.Add( self.radio_OnlyMoviesGenres, 0, wx.ALL, 5 )
		
		self.radio_AllGenres = wx.RadioButton( sizerGenre.GetStaticBox(), wx.ID_ANY, u"Show All Genres", wx.DefaultPosition, wx.DefaultSize, 0 )
		genreFilterSizer.Add( self.radio_AllGenres, 0, wx.ALL, 5 )
		
		
		sizerGenre.Add( genreFilterSizer, 0, 0, 5 )
		
		self.genreBox = MyOvl( sizerGenre.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sizerGenre.Add( self.genreBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerGenreButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonDeleteGenre = wx.Button( sizerGenre.GetStaticBox(), wx.ID_ANY, u"Delete Sected Genre", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerGenreButtons.Add( self.buttonDeleteGenre, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.buttonGenreShow = wx.Button( sizerGenre.GetStaticBox(), wx.ID_ANY, u"Show Titles For Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerGenreButtons.Add( self.buttonGenreShow, 1, wx.ALL, 5 )
		
		
		sizerGenre.Add( sizerGenreButtons, 0, wx.EXPAND, 5 )
		
		self.buttonGenreUpdate = wx.Button( sizerGenre.GetStaticBox(), wx.ID_ANY, u"Update Database for (Un)Checked Genres", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerGenre.Add( self.buttonGenreUpdate, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerGenreAdd = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textAddGenre = wx.StaticText( sizerGenre.GetStaticBox(), wx.ID_ANY, u"Add New Genre: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textAddGenre.Wrap( -1 )
		sizerGenreAdd.Add( self.textAddGenre, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.newGenreBox = wx.TextCtrl( sizerGenre.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		sizerGenreAdd.Add( self.newGenreBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonGenreOK = wx.Button( sizerGenre.GetStaticBox(), wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerGenreAdd.Add( self.buttonGenreOK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sizerGenre.Add( sizerGenreAdd, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sizerGenre.AddSpacer( ( 0, 10), 0, 0, 5 )
		
		
		sizerRightPanel.Add( sizerGenre, 1, wx.EXPAND, 5 )
		
		sizerTag = wx.StaticBoxSizer( wx.StaticBox( self.panelRight, wx.ID_ANY, u"Tags" ), wx.VERTICAL )
		
		self.tagBox = MyOvl( sizerTag.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		sizerTag.Add( self.tagBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		sizerTagButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonDeleteTag = wx.Button( sizerTag.GetStaticBox(), wx.ID_ANY, u"Delete Selected Set(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTagButtons.Add( self.buttonDeleteTag, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.buttonTagShow = wx.Button( sizerTag.GetStaticBox(), wx.ID_ANY, u"Show Titles For Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTagButtons.Add( self.buttonTagShow, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerTag.Add( sizerTagButtons, 0, wx.EXPAND, 5 )
		
		self.buttonTagUpdate = wx.Button( sizerTag.GetStaticBox(), wx.ID_ANY, u"Update Database for (Un)Checked Tag", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTag.Add( self.buttonTagUpdate, 0, wx.ALL|wx.EXPAND, 5 )
		
		sizerTagAdd = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textAddTag = wx.StaticText( sizerTag.GetStaticBox(), wx.ID_ANY, u"Add New Tag:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textAddTag.Wrap( -1 )
		sizerTagAdd.Add( self.textAddTag, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.newTagBox = wx.TextCtrl( sizerTag.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		sizerTagAdd.Add( self.newTagBox, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.buttonTagOk = wx.Button( sizerTag.GetStaticBox(), wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerTagAdd.Add( self.buttonTagOk, 0, wx.ALL, 5 )
		
		
		sizerTag.Add( sizerTagAdd, 0, 0, 5 )
		
		
		sizerTag.AddSpacer( ( 0, 10), 0, 0, 5 )
		
		
		sizerRightPanel.Add( sizerTag, 1, wx.EXPAND, 5 )
		
		
		self.panelRight.SetSizer( sizerRightPanel )
		self.panelRight.Layout()
		sizerRightPanel.Fit( self.panelRight )
		self.splitter.SplitVertically( self.panelLeft, self.panelRight, 375 )
		parentSizer.Add( self.splitter, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( parentSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.onEditMYSQL, id = self.menuItemEditServer.GetId() )
		self.Bind( wx.EVT_MENU, self.onSearchG, id = self.menuItemG.GetId() )
		self.Bind( wx.EVT_MENU, self.onSearchPG, id = self.menuItemPG.GetId() )
		self.Bind( wx.EVT_MENU, self.onSearchPG13, id = self.menuItemPG13.GetId() )
		self.Bind( wx.EVT_MENU, self.onSearchR, id = self.menuItemR.GetId() )
		self.Bind( wx.EVT_MENU, self.onSetupKodi, id = self.menuItem_setupKodi.GetId() )
		self.Bind( wx.EVT_MENU, self.onDeleteKodi, id = self.menuItem_deleteKodi.GetId() )
		self.Bind( wx.EVT_MENU, self.onEditKodi, id = self.menuItem_editKodi.GetId() )
		self.Bind( wx.EVT_MENU, self.onUpdateLibrary, id = self.menuItem_updateKodi.GetId() )
		self.Bind( wx.EVT_MENU, self.onCleanLibrary, id = self.menuItem_cleanKodi.GetId() )
		self.Bind( wx.EVT_MENU, self.onExportLibrary, id = self.menuItem_exportKodi.GetId() )
		self.buttonRetrieve.Bind( wx.EVT_BUTTON, self.onRetrieve )
		self.buttonDeleteGenre.Bind( wx.EVT_BUTTON, self.onDeleteGenre )
		self.buttonGenreShow.Bind( wx.EVT_BUTTON, self.onShowGenreTitles )
		self.buttonGenreUpdate.Bind( wx.EVT_BUTTON, self.onUpdateGenres )
		self.newGenreBox.Bind( wx.EVT_TEXT_ENTER, self.OnAddGenre )
		self.buttonGenreOK.Bind( wx.EVT_BUTTON, self.OnAddGenre )
		self.buttonDeleteTag.Bind( wx.EVT_BUTTON, self.onDeleteTag )
		self.buttonTagShow.Bind( wx.EVT_BUTTON, self.onShowTagTitles )
		self.buttonTagUpdate.Bind( wx.EVT_BUTTON, self.onUpdateTags )
		self.newTagBox.Bind( wx.EVT_TEXT_ENTER, self.OnAddTag )
		self.buttonTagOk.Bind( wx.EVT_BUTTON, self.OnAddTag )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onEditMYSQL( self, event ):
		event.Skip()
	
	def onSearchG( self, event ):
		event.Skip()
	
	def onSearchPG( self, event ):
		event.Skip()
	
	def onSearchPG13( self, event ):
		event.Skip()
	
	def onSearchR( self, event ):
		event.Skip()
	
	def onSetupKodi( self, event ):
		event.Skip()
	
	def onDeleteKodi( self, event ):
		event.Skip()
	
	def onEditKodi( self, event ):
		event.Skip()
	
	def onUpdateLibrary( self, event ):
		event.Skip()
	
	def onCleanLibrary( self, event ):
		event.Skip()
	
	def onExportLibrary( self, event ):
		event.Skip()
	
	def onRetrieve( self, event ):
		event.Skip()
	
	def onDeleteGenre( self, event ):
		event.Skip()
	
	def onShowGenreTitles( self, event ):
		event.Skip()
	
	def onUpdateGenres( self, event ):
		event.Skip()
	
	def OnAddGenre( self, event ):
		event.Skip()
	
	
	def onDeleteTag( self, event ):
		event.Skip()
	
	def onShowTagTitles( self, event ):
		event.Skip()
	
	def onUpdateTags( self, event ):
		event.Skip()
	
	def OnAddTag( self, event ):
		event.Skip()
	
	
	def splitterOnIdle( self, event ):
		self.splitter.SetSashPosition( 375 )
		self.splitter.Unbind( wx.EVT_IDLE )
	

