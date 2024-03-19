#Character Frequency Counter Code
def count_frequency(input):
    empty_dict={}
    for char in input:
        if char in empty_dict:
            empty_dict[char] += 1
        else:
            empty_dict[char] = 1
    print("Character frequency:")
    for char, empty in empty_dict.items():
        print(f"{char}: {empty}")

input = input("Enter a string: ")
count_frequency(input)