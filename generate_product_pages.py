import pandas as pd
import os

TEMPLATE_PATH = 'products_test_template.html'
CSV_PATH = 'products_test.csv'
OUTPUT_DIR = 'generated_pages'

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

products = pd.read_csv(CSV_PATH).dropna(subset=['name', 'search result (main)'])

for i, row in products.head(10).iterrows():
    img_path = str(row['search result (main)'])
    # 确保路径前有 ../
    if not img_path.startswith('../'):
        if img_path.startswith('/'):
            img_path = '..' + img_path
        else:
            img_path = '../' + img_path
    html = template.replace('{{name}}', str(row['name']))
    html = html.replace('{{big image}}', img_path)
    filename = f"{row['name'].replace('/', '_').replace(' ', '_')}.html"
    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
print('生成完毕！') 