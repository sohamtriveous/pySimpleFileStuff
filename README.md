pySimpleFileStuff
=================

A simple python program that allows you to list __pattern__ files in a given directory and then copy/zip them on a case-case basis

###Usage

```bash
./dirparse.py [--todir dir][--tozip zipfile] dir dir dir
```

###Sample output

```bash
Searching in directory: /Users/sohammondal/Documents/pytmp
Found: /Users/sohammondal/Documents/pytmp/he__helloworld__.txt
Found: /Users/sohammondal/Documents/pytmp/newww__annsda__asd.doc
Successfully zipped 'hello.zip' with the following files:  /Users/sohammondal/Documents/pytmp/he__helloworld__.txt   /Users/sohammondal/Documents/pytmp/newww__annsda__asd.doc
```
