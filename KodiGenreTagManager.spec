# -*- mode: python -*-
a = Analysis(['KodiGenreTagManager.py'],
             pathex=['F:\\Programming\\Kodi Genre and Tag Manager'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = [EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='KodiGenreTagManager.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon='icon.ico'
          )]
