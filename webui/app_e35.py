# -*- coding: utf-8 -*-
"""山河回响·仡佬族 单族独立版入口(由 _make_single.py 生成)"""
import os, sys
os.environ['SHE_ETH_KEY'] = 'e35'
os.environ['SHE_PORT'] = '8772'
os.environ['SHE_TITLE'] = '山河回响 · 仡佬族'
_here = os.path.dirname(os.path.abspath(__file__))
_root = os.path.dirname(_here)
if _root not in sys.path:
    sys.path.insert(0, _root)
from webui.app_window import main
main()
