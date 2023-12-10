input_string=input("Enter a lowercase string that has alphabetic characters only and no spaces:")

def solve(input_string):
    vowels = "aeiou"
    
    #The dictionary maps letters to values
    letter_values = {letter: index + 1 for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}

    #Split the string by vowels and calculate the sum of values for each consonant substring
    consonant_values = [sum(letter_values[c] for c in substring) for substring in input_string.split(vowels) if substring]

    return max(consonant_values, default=0)

result=solve(input_string)
print(f"Highest value of {input_string} is {result}")

