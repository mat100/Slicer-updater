# -*- mode: python -*-
from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['src\\updater.py'],
             pathex=['.\\src'],
             binaries=[],
             datas=[('src\\updater.kv', '.'), 
                    ('resources\\icons\\trilab.ico', '.')
                ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='trilab-slicer-updater',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='resources\\icons\\trilab.ico')
