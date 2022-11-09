import re

n = int(input())
valid_emails = []
pattern = r'(\w*)\s{1}(\<\w*\@\w+\.)(com>)'
for i in range(n):
    email = input()
    if re.findall(pattern, email):
        valid_emails.append(email)

for i in valid_emails:
    print(i, end = "\n")


