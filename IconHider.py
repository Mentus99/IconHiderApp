import win32gui
import win32con
import keyboard
import time
import os

def encontrar_janela_icones():
    """
    Tenta encontrar o handle (HWND) da janela que contém os ícones da área de trabalho.
    """
    handle = win32gui.FindWindow("Progman", None)
    handle = win32gui.FindWindowEx(handle, 0, "SHELLDLL_DefView", None)
    handle = win32gui.FindWindowEx(handle, 0, "SysListView32", "FolderView")
    
    if handle:
        return handle
    
    handle = win32gui.FindWindow("Progman", None)
    handle = win32gui.FindWindowEx(handle, 0, "SHELLDLL_DefView", None)
    if handle:
        return handle
    
    return None

def alternar_visibilidade_icones():
    """
    Verifica se a janela dos ícones está visível e alterna a sua visibilidade.
    """
    hwnd = encontrar_janela_icones()
    if not hwnd:
        return

    if win32gui.IsWindowVisible(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    else:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

if __name__ == "__main__":
    # Configura o hotkey e mantém o script em execução
    keyboard.add_hotkey('f12', alternar_visibilidade_icones)
    
    # Esta linha impede que o script feche imediatamente
    keyboard.wait()
