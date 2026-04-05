import re

haystack = "sadbutsad"
needle = "sad"

test = re.search(needle,haystack)
print(test.span()[0])
