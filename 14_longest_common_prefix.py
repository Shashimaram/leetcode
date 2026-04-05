import os.path


def longest_common_prefix(strs):
    prefex= ""
    if not strs:
        return prefex

    if len(strs)==1:
        return strs[0]

    else:
        for x in range(len(strs)-1):
            current_prefex = os.path.commonprefix([strs[0],strs[x+1]])
            if prefex == "":
                prefex = current_prefex
            if len(current_prefex) < len(prefex):
                prefex = current_prefex
            else:
                continue
        for x in strs:
            if x.startswith(prefex):
                continue
            else:
                return ""
    return prefex

# a = ["aaa","aa","aaa"]
# a = ["flower","flow","flight"]
a = ["c","acc","ccc"]

r = longest_common_prefix(a)
print(r)
