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
## Class serverAddFrame
###########################################################################

class serverAddFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add / Edit MySQL Server", pos = wx.DefaultPosition, size = wx.Size( 383,222 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer75 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer76 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer76.AddSpacer( ( 0, 20), 0, 0, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Server Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer7.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.serverNameBox = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer7.Add( self.serverNameBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer76.Add( bSizer7, 0, 0, 5 )
		
		
		bSizer76.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		bSizer771 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText351 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"IP Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText351.Wrap( -1 )
		bSizer771.Add( self.m_staticText351, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.serverIPbox = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer771.Add( self.serverIPbox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer771.AddSpacer( ( 20, 0), 0, 0, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer771.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.serverPortBox = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer771.Add( self.serverPortBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer771.AddSpacer( ( 20, 0), 0, wx.EXPAND, 5 )
		
		
		bSizer76.Add( bSizer771, 0, wx.EXPAND, 5 )
		
		
		bSizer76.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		bSizer7711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3511 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3511.Wrap( -1 )
		bSizer7711.Add( self.m_staticText3511, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.serverUserBox = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 295,-1 ), 0 )
		bSizer7711.Add( self.serverUserBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer76.Add( bSizer7711, 0, wx.EXPAND, 5 )
		
		
		bSizer76.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		bSizer77111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.serverPasswordBox = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.serverPasswordBox.Wrap( -1 )
		bSizer77111.Add( self.serverPasswordBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.serverPasswdBox = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer77111.Add( self.serverPasswdBox, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer77111.AddSpacer( ( 20, 0), 0, 0, 5 )
		
		self.serverAddSaveButton = wx.Button( self.m_panel14, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer77111.Add( self.serverAddSaveButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer77111.AddSpacer( ( 20, 0), 0, wx.EXPAND, 5 )
		
		
		bSizer76.Add( bSizer77111, 0, 0, 5 )
		
		
		bSizer76.AddSpacer( ( 0, 20), 0, 0, 5 )
		
		
		self.m_panel14.SetSizer( bSizer76 )
		self.m_panel14.Layout()
		bSizer76.Fit( self.m_panel14 )
		bSizer75.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer75 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.serverAddSaveButton.Bind( wx.EVT_BUTTON, self.onServerAddSubmit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onServerAddSubmit( self, event ):
		event.Skip()
	

