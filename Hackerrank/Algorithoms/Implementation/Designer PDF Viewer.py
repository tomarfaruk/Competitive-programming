from string import ascii_lowercase
letter = [_ for _ in ascii_lowercase]
number = list(map(int, input().split()))
word = input()

letter_number = dict(zip(letter, number))
max_num=1
for c in word:
    max_num = max(max_num, letter_number[c])
print(max_num*len(word))