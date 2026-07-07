"""PyInstaller specification for STOCK-CIO."""

from PyInstaller.utils.hooks import collect_all
import certifi
import os
import sys


datas = [("10_CONFIG", "10_CONFIG")]
binaries = []
hiddenimports = []

certifi_path = certifi.where()
if certifi_path:
    datas.append((certifi_path, "certifi"))

# Include Tcl/Tk runtime data for tkinter so packaged app can find tcl/tk
# On Windows the Python install keeps Tcl/Tk under sys.base_prefix / 'tcl'
tcl_root = os.path.join(sys.base_prefix, 'tcl')
if os.path.isdir(tcl_root):
    for sub in os.listdir(tcl_root):
        full = os.path.join(tcl_root, sub)
        if os.path.isdir(full):
            # copy into an internal _tcl_data folder inside the bundle
            datas.append((full, os.path.join('_internal', '_tcl_data', sub)))

for package in ("yfinance", "pykrx"):
    package_datas, package_binaries, package_hiddenimports = (
        collect_all(package)
    )
    datas += package_datas
    binaries += package_binaries
    hiddenimports += package_hiddenimports


analysis = Analysis(
    ["desktop_main.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    [],
    exclude_binaries=True,
    name="STOCK-CIO",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
)

collection = COLLECT(
    exe,
    analysis.binaries,
    analysis.datas,
    strip=False,
    upx=True,
    name="STOCK-CIO",
)
