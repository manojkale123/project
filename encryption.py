import string

plain_text= "Hello world"
shift =1

alphabet=string.ascii_lowercase
shifted =alphabet[shift:]+alphabet[:shift]
table=str.maketrans(alphabet,shifted)
encrypted= plain_text.translate(table)

print(encrypted)