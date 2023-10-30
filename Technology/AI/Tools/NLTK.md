# Concepts

The NLTK Python framework is generally used as an education and research tool. It’s not usually used on production applications. However, it can be used to build exciting programs due to its ease of use.

### Exploring

**Opening the text file for processing:**

```python
text_file = open("filename.txt")
text = text_file.read()

print(f'DataType: {text} - {len(text)} - \n Text: {text}')
```

```python
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
```

**Sequence tokenizing:**

By tokenizing the text with `sent_tokenize( )`, we can get the text as sentences.

```python
sentences = sent_tokenize(text)
print(len(sentences))
```

**Word tokenizing:**

By tokenizing the text with `word_tokenize( )`, we can get the text as words.

```python
words = word_tokenize(text)
print(len(words))
```

**Find the frequency distribution:**

```python
from nltk.probability import FreqDist

fdist = FreqDist(words)

#print 10 most frequent words:
fdist.most_common(10)
```

Notice that the most used words are punctuation marks and stopwords. We will have to remove such words to analyze the actual text.

**Plot the frequency graph:**

Let’s plot a graph to visualize the word distribution in our text.

```python
import matplotlib.pyplot as plt

fdist.plot(10)
```

![[Pasted image 20231028201258.png]]

**Remove punctuation marks:**

Next, we are going to remove the punctuation marks as they are not very useful for us. We are going to use `isalpha( )` method to separate the punctuation marks from the actual text. Also, we are going to make a new list called `words_no_punc`, which will store the words in lower case but exclude the punctuation marks.

```python
words_no_punc = []

for w in words:
	if w.isalpha():
		words_no_punc.append(w.lower())

print(words_no_punc)
```

**Plotting graph without punctuation marks:**

```python
fdist = FreqDist(words_no_punc)
fdist.most_common(10)
fdist.plot(10)
```

Notice that we still have many words that are not very useful in the analysis of our text file sample, such as “and,” “but,” “so,” and others. Next, we need to remove coordinating conjunctions.

**List of stopwords:**

```python
from nltk.corpus import stopwords

stopwords = stopwords.words("english")
print(stopwords)
```

**Removing stopwords:**

```python
clean_words = []

for w in words_no_punc:
	if w not in stopwords:
		clean_words.append(w)

print(clean_words)
```

**Final frequency distribution:**

```python
fdist = FreqDist(clean_words)
fdist.most_common(10)
```

![[Pasted image 20231028202500.png]]

As shown above, the final graph has many useful words that help us understand what our sample data is about, showing how essential it is to perform data cleaning on NLP.

Next, we will cover various topics in NLP with coding examples.

* [[Word Cloud]]

* [[Stemming]]



#ai #python #npl