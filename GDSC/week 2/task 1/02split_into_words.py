def split_into_words(text):
    words = text.split()
    return words

# Get user input
user_input = input("Enter a paragraph of text: ")
word_list = split_into_words(user_input)
print("List of words:", word_list)