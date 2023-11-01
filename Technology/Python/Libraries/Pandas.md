### Concepts

### Read a file

```python
pd.read_excel('filepath')
```

### Aggregated functions

```python
import pandas as pd

#create a DataFrame (dictionary):
data = {
	'Product': ['A', 'B', 'C', 'A'],
	'Region': ['North', 'East', 'South', 'South'],
	'Sales': [120, 300, 28, 50]
}

df = pd.DataFrame(data)
```

```python
# sales sum by product
df.groupby('Product')['Sales'].sum()

# middle
[].mean()

# median
[].median()

# minimum
[].min()

# maximum
[].max()

#count
[].count()

# standard deviantion
[].std()
```

### AI

```python
panda_ai = PandasAI(llm, verbose=True)
Pandas_ai(df, prompt='list all region names from london')
```

#ai #python 
