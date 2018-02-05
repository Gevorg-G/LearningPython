# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    w = sentence.split()

    for i in range(len(w)):
       if len(w[i]) >= 5:
          w[i]=w[i][::-1]
    
    return ' '.join(w)

print (spin_words('Hello world!'))