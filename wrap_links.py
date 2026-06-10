import re, os, glob

for f in glob.glob('paintings/*.html'):
    if os.path.basename(f) == 'index.html':
        continue
    with open(f) as fh:
        content = fh.read()
    
    def wrap_img(m):
        indent = m.group(1)
        src = m.group(2)
        alt = m.group(3)
        return f'{indent}<a href="{src}">\n{indent}<img src="{src}" alt="{alt}">\n{indent}</a>'
    
    content = re.sub(r'(\s*)<img src="([^"]+)" alt="([^"]+)">', wrap_img, content)
    
    with open(f, 'w') as fh:
        fh.write(content)
    print(f'Done: {f}')
