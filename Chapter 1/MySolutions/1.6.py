'''
Space: 0(n) since we update the string with N number of characters

Complexity: 0(n^2) since we concatenate each new set of characters on

TODO: This could be improved by adding the new characters (e.g. A2) into a set and then use .join on them all
'''

def sCompress(s):
    ret = ""
    winstart = 0
    for winend in range(len(s)):
        if s[winstart] != s[winend]:
            ret += f'{s[winstart]}{(winend)-winstart}'
            winstart = winend
        elif winend == len(s) - 1:
            ret += f'{s[winstart]}{(winend+1)-winstart}'
            winstart = winend
    if len(ret) >= len(s):
        return s
    else:
        return ret
 
if __name__ == "__main__":
    s = "aabcccccaaa"
    assert sCompress(s) == "a2b1c5a3", f"Nope."