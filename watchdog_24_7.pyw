# -*- coding: utf-8 -*-
"""
Tarixga Sayohat Boti (@Tarixga_sayoxatchibot) uchun
Windows Oynasiz (Silent background) 24/7 Watchdog nazoratchisi.
"""

import os
import subprocess
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "watchdog.log")


def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} [WATCHDOG] {msg}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass


def run_watchdog():
    log("Tarixga Sayoxatchibot Watchdog ishga tushdi.")
    bot_script = os.path.join(BASE_DIR, "bot.py")

    # pythonw.exe topish (oynasiz fon rejimi uchun)
    python_dir = os.path.dirname(sys.executable)
    pythonw_path = os.path.join(python_dir, "pythonw.exe")
    exe = pythonw_path if os.path.exists(pythonw_path) else sys.executable

    while True:
        try:
            log("Bot jarayoni ishga tushirilmoqda...")
            proc = subprocess.Popen(
                [exe, bot_script],
                cwd=BASE_DIR,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
            proc.wait()
            log(f"Bot jarayoni {proc.returncode} kodi bilan to'xtadi. 5 soniyada qayta yoqiladi...")
        except Exception as e:
            log(f"Xatolik: {e}. 10 soniyada qayta uriniladi...")
            time.sleep(5)
        time.sleep(5)


if __name__ == "__main__":
    run_watchdog()
