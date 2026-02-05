#Reference: https://docs.python.org/3/library/re.html
import re

mail_content = "Create insights for coaches and fans: new metrics, strategy comparisons, or visual breakdowns of key play moments.";
mail_content_array = re.split(r'\s', mail_content, 10, 1)

print(mail_content_array)
for each_word in mail_content_array:
    print(each_word)
    print()
        