
def hacktext(text):
    newtext = text.lower()
    newtext = newtext.replace('e','3')
    newtext = newtext.replace('a','4')
    newtext = newtext.replace('o','0')
    newtext = newtext.replace('i','1')
    newtext = newtext.replace('u','2')
    return (newtext)
print (hacktext('Writing like a fake-hacker'))