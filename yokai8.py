def generateAcronym(title):

    bawalNaWord = {"the","and","of","in"}

    words = title.split() # [ "Lord" | "of" | "Shadow" ]

    initial = [] # Lord , Shadow

    for word in words:
        if word.lower() not in bawalNaWord:
          initial.append(word[0].upper())

    return "".join(initial)


title = input("enter your true name:")

aspect = generateAcronym(title)

print(aspect)