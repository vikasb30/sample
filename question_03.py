question_03 = """
An anagram I am

Given two strings s0 and s1, return whether they are anagrams of each other. Two words are anagrams when you can rearrange one to become the other. For example, “listen” and “silent” are anagrams.

Constraints:
- Length of s0 and s1 is at most 5000.

Example 1:

Input:
s0 = “listen”
s1 = “silent”

Output:
True

Example 2:

Input:
s0 = “bedroom”
s1 = “bathroom”

Output:
False

Write your code here
"""
s1=input("Enter string 1")
s2=input("Enter string 2")

if (sorted(s1)==sorted(s2)):
    print("True")
else:
    print("False")