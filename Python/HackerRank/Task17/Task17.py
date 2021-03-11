# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the
# given string. String traversal will take place from left to right,
# not from right to left.
# NOTE: String letters are case-sensitive.

# Program starts from here
g_str = input()
f_str = input()
g_str = list(g_str)
c = 0
j = 0
i = 0
# Loop starts
while i <= len(g_str):

    while j<= len(f_str):

        if f_str[j] == g_str[i]:

            c = c + 1

        j = j + 1

    i = i + 1
# Loop ends
print(c)
