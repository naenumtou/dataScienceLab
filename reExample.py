
import re
import string

# Example text
text = 'RT @___22Pythooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooon @alex #ตัดคำ #Python ทดสอบ! "การใช้งาน Regex ภาษา Python_Version 3.x" \U0001f602 ข้อมูล Link: https://www.thairath.co.th/news/tech/1948784'

# Remove link
re.sub(r'(?:http|ftp|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', text)

'''
Note:
    The link pattern can be found on the internet.
    re.sub is used for cutting given text and replacing with
    some other new text or white space
'''

# Define emoji pattern
emoji = re.compile("["
                   u"\U0001F600-\U0001F64F"  #Emoticons
                   u"\U0001F300-\U0001F5FF"  #Symbols & pictographs
                   u"\U0001F680-\U0001F6FF"  #Transport & map symbols
                   u"\U0001F1E0-\U0001F1FF"  #Flags (iOS)
                   u"\U00002500-\U00002BEF"  #Chinese char
                   u"\U00002702-\U000027B0"
                   u"\U00002702-\U000027B0"
                   u"\U000024C2-\U0001F251"
                   u"\U0001f926-\U0001f937"
                   u"\U00010000-\U0010ffff"
                   u"\u2640-\u2642"
                   u"\u2600-\u2B55"
                   u"\u200d"
                   u"\u23cf"
                   u"\u23e9"
                   u"\u231a"
                   u"\ufe0f"  #Dingbats
                   u"\u3030"
                   "]+", flags = re.UNICODE) #Flag option as Unicode

# Remove emoji
re.sub(emoji, '', text)

'''
Note:
    re.complie is used for compile Regex Pattern into 'regex object'
    The regex object can be used for other operation such as .sub
    The emoji unicode is needed to updated to cover all new emoji

'''

# Remove and extract @username
re.sub(r'@([a-zA-Z0-9_]+)', '', text) #Remove @username
re.findall(r'@([a-zA-Z0-9_]+)', text) #Extract @username

'''
Note:
    Twitter username with @ can contain only a-z lower or
    A-Z caital or 0-9 numberic. It can use only 1 symbol of _.
    Hence, regex pattern is @([a-zA-Z0-9_]+)
    
    re.findall() is used for extracting word pattern from text.
    It will return as list of string
'''

# Remove and extra beginning with '#'
re.sub(r'#([a-zA-Z0-9ก-๙_]+)', '', text) #Remove hashtags
re.findall(r'#([a-zA-Z0-9ก-๙_]+)', text) #Extract hashtags

'''
Note:
    Twitter hashtag can be anything. However, the white space
    is not allowed. The hashtage can be in Thai language.
    Using the same logic with [ก-๙] to define Thai characters.
    It also allows more than 50 characters in hashtag. Hence,
    replace {1,50} with + to find all pattern
'''

# Remove punctuation
text.translate(str.maketrans('', '', string.punctuation))

'''
Note:
    Using string module to sub all punctuation in text.
    This operation should be the last step for cleansing text.
    To ensure that there is sufficient information needed.
'''

# Apply all .sub()
newText = re.sub(r'(?:http|ftp|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', text)
newText = re.sub(emoji, '', newText)
newText = re.sub(r'@([a-zA-Z0-9_]+)', '', newText)
newText = re.sub(r'#([a-zA-Z0-9ก-๙_]+)', '', newText)
newText = newText.translate(str.maketrans('', '', string.punctuation))
print(newText)