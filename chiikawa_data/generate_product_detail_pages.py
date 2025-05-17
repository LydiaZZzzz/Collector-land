import pandas as pd
import os

TEMPLATE_PATH = 'product-detail_template.html'
CSV_PATH = 'products_test.csv'
OUTPUT_DIR = 'product-detailed_pages'

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

products = pd.read_csv(CSV_PATH).dropna(subset=['name', 'big image', 'image1', 'image2', 'image3', 'price', 'size', 'material', 'url'])

for i, row in products.head(10).iterrows():
    html = template.replace('{{name}}', str(row['name']))
    html = html.replace('{{main_image}}', str(row['big image']))
    html = html.replace('{{thumb1}}', str(row['image1']))
    html = html.replace('{{thumb2}}', str(row['image2']))
    html = html.replace('{{thumb3}}', str(row['image3']))
    html = html.replace('{{price}}', str(row['price']))
    html = html.replace('{{size}}', str(row['size']))
    html = html.replace('{{material}}', str(row['material']))
    html = html.replace('{{url}}', str(row['url']))
    filename = f"{row['name'].replace('/', '_').replace(' ', '_')}.html"
    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
print('产品详情页生成完毕！') 