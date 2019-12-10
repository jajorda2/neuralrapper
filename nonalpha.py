with open(r'lyrics.txt', 'r') as infile, \
     open(r'noalpha.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("_", "").replace("+", "").replace("-", "").replace("=", "").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(";", "").replace(":", "").replace(",", "").replace(".", "").replace("<", "").replace(">", "").replace("/", "").replace("?", "").replace("]", "").replace("...", "")
    outfile.write(data)
