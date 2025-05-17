import pandas as pd
import os

TEMPLATE_PATH = 'products_test_template.html'
CSV_PATH = 'products_test.csv'
OUTPUT_DIR = 'generated_pages'

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 读取模板
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

# 读取 CSV
products = pd.read_csv(CSV_PATH).dropna(subset=['name', 'big image'])

for i, row in products.head(10).iterrows():
    html = template.replace('{{name}}', str(row['name']))
    html = html.replace('{{big image}}', str(row['big image']))
    # 文件名用 name 字段，去除特殊字符
    filename = f"{row['name'].replace('/', '_').replace(' ', '_')}.html"
    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
print('生成完毕！') 