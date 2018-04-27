import re

sample_text = """
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
"""

sentence_list = sample_text.strip().split(".")

print("Sentences:\n")
for i in range(0, len(sentence_list) - 1):
    print("{}. {}.\n".format(i + 1, sentence_list[i]))

# ----

print("\nPattern matching:\n")
pattern = "Lorem Ipsum"

# for i in sentence_list:
for i in range(0, len(sentence_list) - 1):
    match = re.search(pattern, sentence_list[i])
    print("{}. `{}` found at start position `{}` till end position `{}` in `{}`\n".format(
        i + 1, match.re.pattern, match.start(), match.end(), match.string))
