from flask import Flask, send_from_directory
import os
import argparse
import sys
import threading


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, 'web')

app = Flask(__name__, static_folder=WEB_DIR, template_folder=WEB_DIR)


@app.route('/')
def index():
    return send_from_directory(WEB_DIR, 'index.html')


@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(WEB_DIR, path)


def _open_in_edge(url: str):
    try:
        # Works on Windows 10/11 to open Microsoft Edge directly
        os.startfile(f"microsoft-edge:{url}")  # type: ignore[attr-defined]
    except Exception:
        # Fallback: try default browser if Edge protocol fails
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception:
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Serve Snake Web UI')
    parser.add_argument('--open-edge', action='store_true', help='Open the app in Microsoft Edge')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5000)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    url = f"http://{args.host}:{args.port}/"
    if args.open_edge:
        # Delay a bit so the server is up before opening
        threading.Timer(0.6, _open_in_edge, args=(url,)).start()

    app.run(host=args.host, port=args.port, debug=args.debug)


