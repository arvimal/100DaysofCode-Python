#!/usr/bin/env python3

"""
The string below contains a book name, Author name, and the year it was published,
separated by a comma.

We need to output the information in the following format, for each entry.

"The book `BOOK_NAME` was published by `AUTHOR_NAME` in `YEAR`"

"""

highlighted_poems = "Afterimages:Audre Lorde:1997,  \
The Shadow:William Carlos Williams:1915, \
Ecstasy:Gabriela Mistral:1925,   \
Georgia Dusk:Jean Toomer:1923,   \
Parting Before Daybreak:An Qi:2014, \
The Untold Want:Walt Whitman:1871, \
Mr. Grumpledump's Song:Shel Silverstein:2004, \
Angel Sound Mexico City:Carmen Boullosa:2013, \
In Love:Kamala Suraiyya:1965, \
Dream Variations:Langston Hughes:1994, \
Dreamwood:Adrienne Rich:1987"

# 1. Split the string to a list, based on the comma delimiter
highlighted_poems_list = highlighted_poems.split(",")
# print(highlighted_poems_list)

# 2. Strip any white space present in each elements
highlighted_poems_stripped = []
for word in highlighted_poems_list:
    highlighted_poems_stripped.append(word.strip())
# print(highlighted_poems_stripped)

# 3. Split each author info into a separate list for
# easier iteration. The split is done at the ":" delimiter.
# We end up with a list of lists.
highlighted_poems_details = []
for data in highlighted_poems_stripped:
    highlighted_poems_details.append(data.split(":"))
# print(highlighted_poems_details)

# 4. Create three lists to carry specific information
titles = []
poets = []
dates = []

# 5. Iterate through the lists within the main list,
# and append the info to the respective list.
for poet_list in highlighted_poems_details:
    titles.append(poet_list[0])
    poets.append(poet_list[1])
    dates.append(poet_list[2])

# 6. Print the information in the desired format.
for info in highlighted_poems_details:
    print("The poem {} was published by {} in {}".format(info[0], info[1], info[2]))
