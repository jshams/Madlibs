variables = "noun, adjective, verb, adverb, pluralNoun, pluralFood, place".split(', ')
story = "One adjective summer morning, the zebras woke up to see three adjective pluralNoun. They were unlocking the door to their pen! The zebras adverb ran through the open door, then verb behind a nearby noun. The zebras quickly verb for the zoo restaurant where they ordered pluralFood and pluralFood. They adverb took their treats and went to place."
#yesNo = input("Would you like to create your own madlib or use our own? (y/n)")
#if yesNo in "Yy":
#    story = input("Type your madlib story using your own variables (you will add the variables you used later)")
#    variables = input("add your variables separated by commas and spaces (', ')").split(', ')
storySplit = story.split(' ')
filledIn = ""

print(story)
for word in storySplit:
    newWord = word
    period = word[-1]
    if period == ".":
        word = word[0:-1]
    if word in variables:
        newWord = input("Enter a(n) " + word + ": ")
        if period == ".":
            newWord = newWord + "."
    filledIn += newWord + " "

print(filledIn)
