# -*- mode: python ; coding: utf-8 -*-
# 山河回响·锡伯族 单族独立版 spec(由 _make_single.py 生成)
import os
repo = SPECPATH
cache = os.path.join(repo, 'webui', 'ethnos_cache')
datas = [
    (os.path.join(repo, 'webui', 'templates', 'mountainriverechoes.html'), 'webui/templates'),
    (os.path.join(cache, 'e36_锡伯族.json'), 'webui/ethnos_cache'),
]
a = Analysis(
    ['webui/app_e36.py'],
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
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='山河回响-锡伯族',
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
    exe, a.binaries, a.datas,
    strip=False, upx=False, upx_exclude=[],
    name='山河回响-锡伯族',
)
