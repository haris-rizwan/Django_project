import re
#
"""
This regular expression is used to find patterns in strings
it will help us finding the urls
"""

patterns = ['term1','term2']

text = 'This is a string with term1'

for pattern in patterns:
    print('Im searching for pattern ' +pattern)

    if re.search(pattern,text):
        print('match')

    else:
        print('no match')



#
# # List of patterns to search for
# patterns = [ 'term1', 'term2' ]
#
# # Text to parse
# text = 'This is a string with term1, but it does not have the other term.'
#
# for pattern in patterns:
#     print ('Searching for "%s" in: \n"%s"' % (pattern, text)),
#
#     #Check for match
#     if re.search(pattern,  text):
#         print ('\n')
#         print ('Match was found. \n')
#     else:
#         print ('\n')
#         print ('No Match was found.\n')
