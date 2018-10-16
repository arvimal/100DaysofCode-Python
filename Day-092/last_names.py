authors = "Audre Lorde, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')

print("\nAuthor names: ")
print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

print("\nAuthor last names:")
print(author_last_names)