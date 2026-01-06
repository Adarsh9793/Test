# sub (pattern, string, count=0, flags=0,repl)

import re
string = "Today is a nice day"
pattern = "day"
print(re.sub(pattern, "evening", string))  # Replaces 'day' with 'evening'
