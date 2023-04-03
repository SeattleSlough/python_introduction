# variables are a way to store information in our programs
# assigning information to a variable is also called 'binding'

iq = 190
print(iq)

# Industry Best Practices
# snake_case
# start with lowercase or underscore (NEVER a number)
# letters, numbers, underscores
# case sensitive
# don't overwrite reserved keywords (e..g, print, else, pass, etc.)

# EXAMPLES

user_iq = 120  # snake_case
_user_iq = 130  # start w/lowercase or underscore
user_iq462 = 145  # letters, numbers, underscores
user_IQ = 120
user_iq != user_IQ  # case sensitive

# keywords should be easy enough to understand so someone can edit your program w/out too much context
# rule of thumb: code should read as easily as english

# variables can be reassigned
user_age = user_iq / 4

# shorthand assignment
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 2

# GOTCHAS
# constants
# a constant is defined in ALL CAPS to signal to other developers should never be changed

# 'dunder' or double underscore
# never create a variable with two underscores
# the language has 'dunder' already set aside and you don't want to overwite
