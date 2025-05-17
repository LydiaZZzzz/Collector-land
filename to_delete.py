import pandas as pd

df = pd.read_csv('products_test.csv')
# 只保留有 name 和 description 的行
df = df.dropna(subset=['name', 'description'])
js = "const productKeywords = [\n"
for _, row in df.head(10).iterrows():
    keywords = [k.strip() for k in str(row['description']).split(',')]
    page = f"generated_pages/{row['name'].replace('/', '_').replace(' ', '_')}.html"
    js += f'  {{name: "{row["name"]}", keywords: {keywords}, page: "{page}"}},\n'
js += "];"
print(js)