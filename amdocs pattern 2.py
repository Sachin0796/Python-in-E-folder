max_length=0
max_length_string=''
input_string=input("Enter the string for which u need to find the longest string with no repeated character:")
for i in range(len(input_string)):
    for j in range(len(input_string)):
        substring_of_main_string=input_string[i:j+1]
        if (len(substring_of_main_string) == len(set(substring_of_main_string))
                and max_length< len(substring_of_main_string)):
            max_length_string = substring_of_main_string
            max_length = len(substring_of_main_string)
print(f"Longest string with no repeated characters is {max_length_string} and its length is {max_length}")