# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['compiler_pdf.py'],  # Chemin vers votre script Python
    pathex=['C:\\Users\\TAT\\Desktop\\pypdfcompiler'],  # Chemin vers votre projet
    binaries=[],
    datas=[('ghostscript\\gs', 'ghostscript\\gs')],  # Chemin vers le dossier Ghostscript
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PDFCompressor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='PDFCompressor'
)
