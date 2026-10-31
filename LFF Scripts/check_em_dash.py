import glob

em_dash = "\u2014"
for ext in ['html', 'md', 'json', 'py']:
    for f in glob.glob(f'**/*.{ext}', recursive=True):
        if '.venv' in f or 'node_modules' in f: continue
        try:
            with open(f, 'r', encoding='utf-8') as fl:
                c = fl.read()
                if em_dash in c:
                    print(f"Found em dash in {f}: {c.count(em_dash)} occurrences")
        except Exception:
            pass
