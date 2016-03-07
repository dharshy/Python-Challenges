__author__ = 'Priyadharshini'
# Determine if a string contains unique characters
def unique_char(inp_str = ""):
    dict_char = {}
    #if the input string is empty return nothing
    #to process here
    if len(inp_str) == 0:
        print("This is an empty string")
        return
    #append the input characters into a dict where key is the char
    #and value is the number of times it is present in the string
    for i in inp_str:
        count = 1
        #check if the char already there in dict and if it is there
        #increment the vlue by 1
        if i in dict_char:
            dict_char[i] = count+1
        #if char is not present populate the dict with key and value
        else:
            dict_char[i] = count
    print(dict_char)
    #if any of the values in the dictionary is 2-it means there is repititon
    if 2 in dict_char.values():
        print("Not a unique character")
    else:
        print("This is a unique string")



if __name__ == "__main__":
    input_str = "abcd"
    unique_char(input_str)