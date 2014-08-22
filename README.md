pySimpleFileStuff
=================

A simple python program that allows you to list __pattern__ files in a given directory and then copy/zip them on a case-case basis

###Usage

```bash
./dirparse.py [--todir dir][--tozip zipfile] dir dir dir
```

###Example

```bash
./dirparse.py --tozip hello111.zip /Users/sohammondal/Documents/pytmp /Users/sohammondal/Documents/pytmp/other
```

###Sample output

```bash
Searching in directory: /Users/sohammondal/Documents/pytmp
Found: /Users/sohammondal/Documents/pytmp/he__helloworld__.txt
Found: /Users/sohammondal/Documents/pytmp/newww__annsda__asd.doc
Searching in directory: /Users/sohammondal/Documents/pytmp/other
Found: /Users/sohammondal/Documents/pytmp/other/this__is__a_text_file.asa
Found: /Users/sohammondal/Documents/pytmp/other/this__is__a_text_file1.asa
Found: /Users/sohammondal/Documents/pytmp/other/this__is__a_text_file2.asa
Successfully zipped 'hello111.zip' with the following files:  /Users/sohammondal/Documents/pytmp/he__helloworld__.txt /Users/sohammondal/Documents/pytmp/newww__annsda__asd.doc /Users/sohammondal/Documents/pytmp/other/this__is__a_text_file.asa /Users/sohammondal/Documents/pytmp/other/this__is__a_text_file1.asa /Users/sohammondal/Documents/pytmp/other/this__is__a_text_file2.asa
```
