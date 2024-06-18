print("Write your own story")
with open('story.txt','r') as f:
    story = f.read()
start_char = '['
end_char = ']'
start_index = -1
words = set()
for i,char in enumerate(story):
    if(char==start_char):
        start_index = i
    if(char==end_char and start_char != -1):
        words.add(story[start_index: i+1])
        start_index = -1
for word in words:
    value = input(f'Enter your value for the {word} : ')
    story = story.replace(word,value)
print(story)
with open('story_modified.txt','w') as f:
    f.write(story)