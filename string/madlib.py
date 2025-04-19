with open('story.txt', 'r') as file:
    story = file.read()

word = set()
start_index = -1

answers = {
    "<noun1>": "dragon",
    "<noun2>": "toaster",
    "<adjective1>": "sparkly",
    "<adjective2>": "curious",
    "<verb1>": "dance",
    "<verb2>": "all",
    "<adverb1>": "gracefully",
    "<place>": "underwater city"
}

for i in range(len(story)):
    if story[i] == '<':
        start_index = i
    if story[i] == '>' and start_index != -1:
        word.add(story[start_index: i+1])
        start_index = -1
print(word)

for i in answers:
    story = story.replace(i, answers[i])
print(story)
