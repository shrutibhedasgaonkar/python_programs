'''
user_input = input("Enter any word =  ").lower()
count = 0

for i in user_input:
    if i in 'aeiou':
        print(i)
        count = count + 1

print(count)
'''

'''Using list comprehension'''
user_input1 = input("Enter any word =  ").lower()
count = 0
vowels = [i for i in user_input1 if i in 'aeiou']

for vowel in vowels:
    count = count + 1

print("list of vowels in the word = ", vowels)
print("number of vowels in the word = ", count)


