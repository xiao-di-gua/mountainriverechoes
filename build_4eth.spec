# -*- mode: python ; coding: utf-8 -*-
# 山河回响·四族定制版 PyInstaller spec
# datas: 模板 + 四族曲库(裁剪后) 全部落在 _MEIPASS/webui/ 下, 与源码运行时布局一致
import os

repo = SPECPATH
cache = os.path.join(repo, 'webui', 'ethnos_cache')
datas = [
    (os.path.join(repo, 'webui', 'templates', 'mountainriverechoes.html'), 'webui/templates'),
]
_ETH_KEYS = ('e34', 'e35', 'e36', 'e49')
for n in sorted(os.listdir(cache)):
    if n.endswith('.json') and not n.endswith('.bak') and not '.bak_' in n and not n.endswith('.pre_clean'):
        if any(n.startswith(k + '_') for k in _ETH_KEYS):
            datas.append((os.path.join(cache, n), 'webui/ethnos_cache'))

a = Analysis(
    ['webui/app_window.py'],
    pathex=[repo],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'webview.platforms.edgechromium',
        'webview.platforms.winforms',
        'webview.platforms.cef',
        'clr_loader',
        'pythonnet',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='山河回响',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='山河回响',
)
