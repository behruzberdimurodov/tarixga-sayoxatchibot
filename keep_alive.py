# -*- coding: utf-8 -*-
"""
Tarixga Sayohat Boti (@Tarixga_sayoxatchibot) uchun
24/7 Keep-Alive HTTP Health Check Serveri.
"""

import http.server
import os
import socketserver
import threading


class HealthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Tarixga Sayohat Boti 24/7</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0B132B; color: #fff; text-align: center; padding: 50px 20px; }
        .card { background: #1C2541; border: 2px solid #D4AF37; border-radius: 12px; max-width: 600px; margin: 0 auto; padding: 30px; box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
        h1 { color: #D4AF37; margin-bottom: 10px; }
        p { color: #E0E1DD; font-size: 18px; line-height: 1.6; }
        .badge { background: #28a745; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; display: inline-block; margin-top: 15px; }
        a { color: #D4AF37; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>⏳ Tarixga Sayohat Boti</h1>
        <p>🦖 Yura davridan to zamonaviy Sun'iy Intellektgacha bo'lgan tarixiy ensiklopediya boti 24/7 rejimida uzluksiz ishlamoqda.</p>
        <div class="badge">● TIZIM ISHLAMOQDA (24/7 ACTIVE)</div>
        <br><br>
        <p><a href="https://t.me/Tarixga_sayoxatchibot" target="_blank">👉 Telegram orqali ochish: @Tarixga_sayoxatchibot</a></p>
    </div>
</body>
</html>"""
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        # Konsolni to'ldirmaslik uchun sukut saqlash
        return


def run_server(port: int = 8081):
    try:
        with socketserver.TCPServer(("", port), HealthHandler) as httpd:
            httpd.serve_forever()
    except Exception as e:
        print(f"Keep-alive server warning: {e}")


def start_keep_alive_server(port: int = None):
    if port is None:
        port = int(os.environ.get("PORT", 8081))
    thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    thread.start()
    return thread
