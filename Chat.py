#Python script to parse through text file
file = open('WhatsApp Chat.txt', 'r',  encoding="utf8") 
counts = {}
for line in file:
    words = line.partition(" - ")[2:][0].split(":")[1].split()

    try:
        words.remove('<Media')
        words.remove("omitted>")
    except:
        pass

    for word in words:
        word_tmp = word.rstrip(" ?<>,!.").lower()
        counts[word_tmp] = counts.get(word_tmp, 0) + 1

df = pd.DataFrame.from_dict(counts, orient='index')
df = df.sort_values(by=[0], ascending=False)
df = df.head(50)
print(df)
