import re

string1 = ("The integration of renewable energy sources into the global "
           "grid system has the potential to significantly reduce carbon "
           "emissions, while also encouraging sustainability in both "
           "developed and developing nations.")

string2 = ("By incorporating renewable energy into national power grids, "
           "countries can drastically lower their carbon footprints, "
           "fostering a future of sustainability and environmental responsibility "
           "across both industrialized and emerging economies.")

words_str1 = re.findall(r'\w+', string1.lower())
words_str2 = re.findall(r'\w+', string2.lower())

words_set1 = set(words_str1)
words_set2 = set(words_str2)

common_words = words_set1 & words_set2
unique = words_set1 | words_set2

ratio = len(common_words) / len(unique)

print(f"Jaccard Similarity: {ratio:.2f}")
