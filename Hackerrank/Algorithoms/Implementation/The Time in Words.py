words = ["", "one", "two", "three", "four", "five", "six","seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
        "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine", "half"]

h = int(input())
m = int(input())
pastorto = 'past'
minute = ''


if m>30:
    pastorto = "to"

if m == 1:
    minute = ' minute '
elif m%15==0:
    minute = ' '
else:
    minute = ' minutes '

if m==0:
    print(words[h]+" o' clock")
elif m < 31:
    print(words[m] + minute + pastorto + " " + words[h])
else:
    print(words[60 - m] + minute + pastorto + " " + words[h+1])

