Word Cloud is a data visualization technique. In which words from a given text display on the main chart. In this technique, more frequent or essential words display in a larger and bolder font, while less frequent or essential words display in smaller or thinner fonts. It is a beneficial technique in NLP that gives us a glance at what text should be analyzed.

**Properties:**

1. **font_path**: It specifies the path for the fonts we want to use.
2. **width**: It specifies the width of the canvas.
3. **height**: It specifies the height of the canvas.
4. **min_font_size**: It specifies the smallest font size to use.
5. **max_font_size:** It specifies the largest font size to use.
6. **font_step**: It specifies the step size for the font.
7. **max_words**: It specifies the maximum number of words on the word cloud.
8. **stopwords**: Our program will eliminate these words.
9. **background_color:** It specifies the background color for canvas.
10. **normalize_plurals**: It removes the trailing “s” from words.

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud().generate(text)

plt.figure(figsize = (12, 12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
```

![[Pasted image 20231028203548.png]]

As shown in the graph above, the most frequent words display in larger fonts. The word cloud can be displayed in any shape or image.

**Word CloudAdvantages:**

- They are fast.
- They are engaging.
- They are simple to understand.
- They are casual and visually appealing.

**Word Cloud Disadvantages:**

- They are non-perfect for non-clean data.
- They lack the context of words.

#ai #python #npl