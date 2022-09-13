print("Program to remove all the lines that contain the character 'a' in a file and write it to another file.")
def Remove():
    f = open("SampleOld.txt","r")
    lines = f.readlines()
    f.close()
    f = open("SampleOld.txt","w")
    fn = open("SampleNew.txt","w")
    for line in lines:
          if 'a' in line:
              fn.write(line)
          else:
              f.write(line)
    print("All line that contains 'a' character has been extracted from SampleOld.txt file and saved to SampleNew.txt file" )
    print("Data updated in Sample Old File....")
    f.close()
    fn.close()
