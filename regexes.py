>>> import re
>>> re.findall("ab*c", "ac")
['ac']
>>> re.findall("ab*c", "ABC", re.IGNORECASE)
>>> #use re.search() to search for a particular pattern inside a string
>>> #calling .group() on a MatchObject will return the first and most inclusive result
>>> match_results = re.search("ab*c", "ABC", re.IGNORECASE)
>>> match_results.group()
'ABC'
>>> #re.sub(), which is short for substitute, allows you to replace text in a string that matches a regular expression with new text. 
>>> # It behaves sort of like the .replace() string method.
>>> string = "Everything is <replaced> if it's in <tags>."
>>> string = re.sub("<.*>", "ELEPHANTS", string)
>>> string
'Everything is ELEPHANTS.'
>>> #the shorter version of replacements is with *?
>>> string = "Everything is <replaced> if it's in <tags>."
>>> string = re.sub("<.*?>", "ELEPHANTS", string)
>>> string
"Everything is ELEPHANTS if it's in ELEPHANTS."
>>> 
