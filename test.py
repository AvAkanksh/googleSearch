import sys
print("Hello World")
argv = sys.argv
final_string = ''
# https://www.google.com/search?q=imagenet%20how%20many%20images
for i in range(1,len(argv)):
  final_string+= argv[i] + '%20'
url = "https://www.google.com/search?q="+final_string
print("Your final url : \n"+url)
