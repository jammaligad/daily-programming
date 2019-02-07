'''
Implement an autocomplete system. That is, given a query string S and a set of all possible query strings, return all strings in the set that have S as a prefix.
For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].
'''
def autocomplete(string_set, s):
    auto = []
    for word in string_set:
        if s in word:
            auto.append(word)
    return print(auto)

s_str = input().split()
s = input()
autocomplete(s_str, s)

