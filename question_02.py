question_02 = """
Given a query string s and a list of all possible words,
return all words that have s as a suffix.

Example 1:
Input:
s = “ed”
words = [“called”, “aged”, “land”]

Output:
[“called”, “aged”]

Explanation:
Only called and aged ends with ed.

Example 2:
Input:
s = “d”
words = [“helped”,  “held”, “land”, “mat”, “cat”, “bold”]

Output:
[“helped”,  “held”, “land”, “bold”]

Explanation:
All these words ends with d, except for “mat” and “cat”.

Write your code bellow
"""
s=input("Enter the suffix")
str=input("Enter a list element separated by space ")
words=str.split()
news=[]
for j in words:
    if j.endswith(s):
        news.append(j)
print(news)