# import os
# os.remove("demofile2.txt")


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")