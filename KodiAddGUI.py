# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class kodiAddFrame
###########################################################################

class kodiAddFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add / Edit Kodi Connection", pos = wx.DefaultPosition, size = wx.Size( 392,189 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		kodiAddFrameSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.kodiMainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.kodiMainPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		KodiMainPanelSizer = wx.BoxSizer( wx.VERTICAL )
		
		
		KodiMainPanelSizer.AddSpacer( ( 0, 20), 0, 0, 5 )
		
		kodiFirstSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.kodiIPtext = wx.StaticText( self.kodiMainPanel, wx.ID_ANY, u"Kodi Hostname/IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kodiIPtext.Wrap( -1 )
		kodiFirstSizer.Add( self.kodiIPtext, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.KodiNameBox = wx.TextCtrl( self.kodiMainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		kodiFirstSizer.Add( self.KodiNameBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.kodiPortText = wx.StaticText( self.kodiMainPanel, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kodiPortText.Wrap( -1 )
		kodiFirstSizer.Add( self.kodiPortText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.KodiPortBox = wx.TextCtrl( self.kodiMainPanel, wx.ID_ANY, u"8080", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		kodiFirstSizer.Add( self.KodiPortBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		KodiMainPanelSizer.Add( kodiFirstSizer, 0, 0, 5 )
		
		
		KodiMainPanelSizer.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		
		KodiMainPanelSizer.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		kodiSecondSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.kodiUserText = wx.StaticText( self.kodiMainPanel, wx.ID_ANY, u"User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kodiUserText.Wrap( -1 )
		kodiSecondSizer.Add( self.kodiUserText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.KodiUserBox = wx.TextCtrl( self.kodiMainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		kodiSecondSizer.Add( self.KodiUserBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.kodiPasswordText = wx.StaticText( self.kodiMainPanel, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kodiPasswordText.Wrap( -1 )
		kodiSecondSizer.Add( self.kodiPasswordText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.KodiPasswdBox = wx.TextCtrl( self.kodiMainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 123,-1 ), 0 )
		kodiSecondSizer.Add( self.KodiPasswdBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		KodiMainPanelSizer.Add( kodiSecondSizer, 0, wx.EXPAND, 5 )
		
		
		KodiMainPanelSizer.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		kodiThirdSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		kodiThirdSizer.AddSpacer( ( 35, 0), 0, 0, 5 )
		
		self.KodiAddSaveButton = wx.Button( self.kodiMainPanel, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		kodiThirdSizer.Add( self.KodiAddSaveButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		kodiThirdSizer.AddSpacer( ( 20, 0), 0, wx.EXPAND, 5 )
		
		
		KodiMainPanelSizer.Add( kodiThirdSizer, 0, 0, 5 )
		
		
		KodiMainPanelSizer.AddSpacer( ( 0, 20), 0, 0, 5 )
		
		
		self.kodiMainPanel.SetSizer( KodiMainPanelSizer )
		self.kodiMainPanel.Layout()
		KodiMainPanelSizer.Fit( self.kodiMainPanel )
		kodiAddFrameSizer.Add( self.kodiMainPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( kodiAddFrameSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.KodiAddSaveButton.Bind( wx.EVT_BUTTON, self.onKodiAddSubmit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onKodiAddSubmit( self, event ):
		event.Skip()
	

