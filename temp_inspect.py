from pathlib import Path
root = Path(r'd:\3. 업무 (GitHub)\Stock-CIO')
for p in [root/'dist'/'STOCK-CIO'/'_internal', root/'dist'/'STOCK-CIO'/'_internal'/'certifi', root/'dist'/'STOCK-CIO'/'certifi']:
    print(p, 'exists=', p.exists())
    if p.exists():
        try:
            for child in p.iterdir():
                print(' ', child.name)
        except Exception as e:
            print(' err', e)
