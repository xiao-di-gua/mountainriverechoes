# -*- coding: utf-8 -*-
"""山河回响·四族定制版 —— 桌面窗口入口
用 pywebview(EdgeChromium/WebView2) 把 WebUI 嵌进独立桌面窗口，不再调起外部浏览器。
服务线程随窗口关闭一起退出；若 8766 已有实例在服务，则直接把窗口指向它。
"""
import sys, os, socket, threading, time

# console=False(无窗口)模式下 stdout/stderr 为 None，pythonnet/clr_loader 写日志会崩
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w', encoding='utf-8')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w', encoding='utf-8')

if getattr(sys, 'frozen', False):
    BASE = sys._MEIPASS
    os.chdir(os.path.dirname(sys.executable))   # 与 lnk WorkingDir={app} 行为一致
else:
    BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

import webview
from webui import mountainriverechoes as mre


def _serving(host, port):
    """端口已有人监听且 / 能通 → 视为已有实例在服务"""
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except OSError:
        return False


def _start_server(host, port):
    # 与原 __main__ 一致: 预热歌名索引(后台) + Flask 线程
    threading.Timer(5.0, lambda: threading.Thread(target=mre._build_song_index, daemon=True).start()).start()
    t = threading.Thread(
        target=lambda: mre.app.run(host=host, port=port, threaded=True, use_reloader=False),
        daemon=True)
    t.start()


def _wait_ready(host, port, timeout=40):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if _serving(host, port):
            return True
        time.sleep(0.3)
    return False


def main():
    host = mre.HOST
    # 单族独立版通过环境变量注入端口/标题；缺省为四族定制版行为
    port = int(os.environ.get('SHE_PORT', str(mre.PORT)))
    title = os.environ.get('SHE_TITLE', '山河回响（四族定制版）')
    if not _serving(host, port):
        _start_server(host, port)
        _wait_ready(host, port)
    webview.create_window(
        title,
        f'http://{host}:{port}',
        width=1280, height=860, min_size=(980, 640),
        background_color='#101418',
    )
    webview.start()          # 阻塞至窗口关闭
    os._exit(0)              # 关窗即退出（daemon 服务线程随之终止）


if __name__ == '__main__':
    try:
        main()
    except Exception:
        # 窗口模式无控制台: 崩溃堆栈落到 exe 旁日志, 便于定位
        import traceback
        try:
            _lg = os.path.join(os.path.dirname(sys.executable) if getattr(sys, 'frozen', False)
                               else os.path.dirname(os.path.abspath(__file__)), '崩溃日志.txt')
            with open(_lg, 'w', encoding='utf-8') as f:
                f.write(traceback.format_exc())
        except Exception:
            pass
        raise
