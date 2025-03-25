filename = "TEXTOVYSUBOR"

with open(filename, 'r') as file:
    content = file.read()
    print(content)
    # print(repr(content))

    words = content.split()
    print(words)


print('task ...')