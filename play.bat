@echo off
chcp 65001 >nul
title 🎮 JUST LEARNING GIT - Arcade
mode con: cols=108 lines=40 >nul 2>&1
python "%~dp0play.py" --new-window
pause
