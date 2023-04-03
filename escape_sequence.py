# Escape Sequence

# weather = 'It's sunny' - won't work

weather = 'It\'s "kind of" sunny'
storm = "It's raining 'cats and dogs'"
choices = "let's have red and\\or white"

# \ let's Python know that whatever follows is a string
# 'It\'s \"kind of sunny\"' ---> 'It's "kind of" sunny'
# 'It\'s raining \'cats and dogs\'' ---> "It's raining 'cats and dogs'"
# 'Let\'s have red and\\or white' ---> "Let's have red and\or white"

print(weather)
print(storm)
print(choices)

# \t = tab
# \n = new line

greeting = '\t It\'s "kind of" sunny.\n hope you have a good day!'
print(greeting)
