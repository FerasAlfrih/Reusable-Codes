def remover(text, state):
    if state:
        removable = text.split("\\")[1]
        removable = removable.split(" ")[0]
        removable = "\\" + removable + " "
        print(removable)
        text = text.replace(removable, "")
        state = True if "\\" in text else False
    return text, state


text = "hello \\I'm new here \\good luck"
state = True
while state:
    text, state = remover(text, state)
print(text)
