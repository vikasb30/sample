question_01 = """
Given a query string s and a list of all possible words, return all words that have s as a prefix.

Example 1:

Input:
s = “de”
words = [“dog”, “deal”, “deer”]

Output:
[“deal”, “deer”]

Explanation:
Only deal and deer begin with de.

Example 2:

Input:
s = “b”
words = [“banana”, “binary”, “carrot”, “bit”, “boar”]

Output:
[“banana”, “binary”, “bit”, “boar”]

Explanation:
All these words start with b, except for “carrot”.

Write your code bellow

"""
s=input("Enter the prefix")
str=input("Enter a list element separated by space ")
words=str.split()
news=[]
for j in words:
    if j.startswith(s):
        news.append(j)
print(news)
