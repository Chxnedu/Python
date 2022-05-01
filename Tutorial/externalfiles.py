# to access a file in the same directory you're in, use the open command
games = open("games", "a")
# the r there means readable. you can use w(write), a(append), or r+(readable and writable)
# using w overrides everything in an existing file. it can also be used to create a new file by
# specifying the name of the file after open

# to check if a file is readable, use the function .readable
# print(games.readable())

# to actually read the file, use the .read function
# print(games.read())

# to write to a file, use the a(append) and the .write function.
games.write('\nTHE WITCHER 3')

# whenever you open a file, make sure to close the file with the .close function
# you can also automatically close a file when youre through by starting the open statement with 'with'
games.close()