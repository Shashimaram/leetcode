

s ="     a     "

words = []

w = ""
try:
    for x in s:
        if x != " ":
            w+=x
        elif x == " ":
            if w != "":
                words.append(w)
                w = ""
            else:
                continue
finally:
    if w != "":
        words.append(w)

    
len(words[-1])