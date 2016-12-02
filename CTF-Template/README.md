# Project with templates and directory structure for writing CTF writeups

* Problems of each CTF are divided in multiple catagory. There is directory for each problem of a category for it's writeup content like code and README.md. Code and relevant resources of problem are stored in problem directory as it is. README.md file has the actual writeup.
* This directory conatins a Template-readme.md file that has template for writing README.md for Top Level CTF writeup directory, which conatains all catogories.
* Each category directory contains a template readme.md file that contains structure for writing writeup for problem of that category.
* One can directly clone this repository and use these template for writing writeups.

### Steps
1. Download or Clone this directory on your own git repo
2. Rename the directory to your CTF-NAME
3. Create a directory for each problem of a category in its category directory. Place all relevent resources to that problem in that directory. 
4. Use that category's Catagory-Problem-Template-README.md for writing writeup of that problem. If you are writing writeup for problem of Binary-Exploitation category use [Catagory-Problem-Template-README.md](Binary-Exploitation/Catagory-Problem-Template-README.md).
5. To write the writeup copy Catagory-Problem-Template-README.md to prbomem directory, go to the problem directory, modify the content of copied file with your content as per the structure of original file. Once finished save the file.
6. Rename the Catagory-Problem-Template-README.md present in problems directory to README.md.
7. Do this for all problems of different category.
8. Once done for all the problems modify  [Template-CTF-README.md](Template-CTF-README.md) as per your new CTF name and writeups of problems.
9. Remove the README.md 
10. rename the [Template-CTF-REDME.md](Template-CTF-README.md) to README.md in your CTF directory with command: mv Template-CTF-README.md README.md. Now, you are done with writeup of your CTF, just commit these changes.

