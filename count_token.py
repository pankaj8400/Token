import tiktoken


encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
response_format={ "type": "json_object" },
messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
],
text = "This is an example sentence to count tokens."
token_count = len(encoding.encode(text))

print(f"The text contains {token_count} tokens.")

def count_characters_using_encode(text, encoding='utf-8'):
    encoded_string = text.encode(encoding)
    return len(encoded_string)

#input_string = input("Enter a string: ")
total_bytes = count_characters_using_encode(text)
print("Total number of bytes used to encode the string:", total_bytes)


# def count_total_characters(text):
#     return len(text)

# #input_string = input("Enter a string: ")
# total_characters = count_total_characters(text)
# print("Total number of characters:", total_characters)


#char_count = count(encoding.encode(text))
#print(f"The text contains {char_count} tokens.")

#for i in text:
 #   print(i,'=',text.count(i),'times')
 
# def count_characters(text):
#     char_count = {}
#     for char in text:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count

# #input_string = input("Enter a string: ")
# character_count = count_characters(text)
# print("Character count:")
# for char, count in character_count.items():
#     print(f"'{char}': {count}")
