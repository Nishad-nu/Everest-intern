from collections import Counter 
text = """In the age of information, data flows endlessly across networks, devices, and clouds,
Every click, search, and transaction creates a digital footprint that reveals patterns of behavior,
intent, and identity. Companies that can organize, clean, and analyze Uis ocean of raw data gain
insights that drive smarter decisions, personalized experiences, and innovative products.
Yet, with great data comes great responsibility privacy, ethics, and security challenges grow
just as rapidly. The future will belong to those who balance curiosity with caution,
turning data into wisdom rather than chaos."""

words = text.replace(",","").lower().split(" ")
word_count = Counter(words)
print("=============", word_count)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("**************"), dict(sorted_words)
