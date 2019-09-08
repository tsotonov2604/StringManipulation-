import string 
def reverse_letter(stri):
    letters = string.ascii_letters
    reverse = stri[::-1]
    new = []
    for letter in reverse:
        for char in letters:
            if letter == char:
                new.append(letter)
    
    word = "".join(new)
    print(word)
        

reverse_letter('krish21an')
