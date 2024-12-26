# TODO

import cs50
import math

x = cs50.get_string("Enter your string here: ")

letters = 0;
words = 0;
sentences = 0;

#Calculate letters

len_letters = len(x)

space_letters = x.count(' ')
comma_letters = x.count(',')
dot_letters = x.count('.')
exclamation_letters = x.count('!')
questionmark_letters = x.count('?')
apos_letters = x.count("\'")

letters = len_letters - space_letters - comma_letters - dot_letters - exclamation_letters - questionmark_letters - apos_letters

#Calculate Words

res = x.split()
words = len(res)

#Calculate Sentences

if (exclamation_letters + questionmark_letters + dot_letters == 0):
    sentences = 1
else:
    sentences = exclamation_letters + questionmark_letters + dot_letters

#Calculate grade

averagewords = words / 100
L = letters / averagewords
S = sentences / averagewords

index = 0.0588 * L - 0.296 * S - 15.8

print("Letters:", letters)
print("Words:", words)
print("Sentences:", sentences)

if(index< 1):
    print("Before Grade 1")
elif(index>16):
    print("Grade 16+")
else:
    print("Grade:", round(index))