import os

input_directory_in_str = "/Users/isaacrowe/Documents/GitHub/tessajewel/img/studio/familial_code"
output_directory_in_str = "/Users/isaacrowe/Documents/GitHub/tessajewel/_posts/familial_code/"
directory = os.fsencode(input_directory_in_str)

count= 0
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     filename = os.path.splitext(filename)[0]
     writeFile = open(output_directory_in_str + "2020-3-13-" + filename + ".md", 'w')
     writeFile.write("---\n")
     writeFile.write("layout: piece\n")
     writeFile.write("hero-bg-color: \"#000000\"\n")
     writeFile.write("show: familial_code\n")
     writeFile.write("uid: " + filename + "\n")
     writeFile.write("title: " + filename + "\n")
     writeFile.write("medium: mixed\n")
     writeFile.write("dates: 2020\n")
     writeFile.write("type: studio\n")
     writeFile.write("---\n\n")
     writeFile.write("<img src=\"{{site.baseurl}}img/{{page.type}}/{{page.show}}/{{page.uid}}.jpg\" class=\"piece-photo\"/>\n")