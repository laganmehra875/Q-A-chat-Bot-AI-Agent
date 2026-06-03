import json
import pathlib

nb_path = pathlib.Path('/Users/mac/Downloads/Agentic AI course/Langchain_Series/langchainbasic.ipynb')

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

changed = False
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        source = cell.get('source', [])
        new_source = []
        for line in source:
            if '"yser"' in line:
                new_source.append(line.replace('"yser"', '"user"'))
                changed = True
            else:
                new_source.append(line)
        cell['source'] = new_source

if changed:
    with nb_path.open('w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)
    print('Typo fixed.')
else:
    print('No typo found.')
