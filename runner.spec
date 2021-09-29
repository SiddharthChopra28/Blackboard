# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\runner.py'],
             pathex=['C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('logo.ico', 'C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\logo.ico', 'DATA')]
a.datas += [('arrow.png', 'C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\arrow.png', 'DATA')]
a.datas += [('FiraCode-VariableFont_wght.ttf', 'C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\FiraCode-VariableFont_wght.ttf', 'DATA')]
a.datas += [('SmoothMarker-45d6.ttf', 'C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\SmoothMarker-45d6.ttf', 'DATA')]
a.datas += [('SqueakyChalkSound-ZG8.ttf', 'C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\SqueakyChalkSound-ZG8.ttf', 'DATA')]
a.datas += [('Ubuntu-Light.ttf', 'C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\Ubuntu-Light.ttf', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Blackboard',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          icon='C:\\Users\\pooja\\Desktop\\Python_Codes\\Blackboard\\logo.ico',
          codesign_identity=None,
          entitlements_file=None )
