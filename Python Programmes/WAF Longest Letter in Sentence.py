# Making a function
def longest_sentence(sentence):
    longest = max(sentence.split(), key=len)  # splits the sentence and finds the longest chr
    print("Longest word is: ", longest) # prints longest chr
    print("And its length is: ", len(longest)) # prints the len of longest chr

# Inputting the sentence
sentence = input("Enter sentence: ")

# Calling the function
longest_sentence(sentence)