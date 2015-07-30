# opening a file
"""
f = open("/file/directory/here/...", "rb")

# reading a file
f.tell() # gives the current position in the open file

f.seek(a,b) # moves to another position in the file, 'a' bytes
			The second parameter specifies what the 
			first one means; 0 means move to an absolute 
			position (counting from the start of the file), 
			1 means move to a relative position (counting 
			from the current position), and 2 means move to 
			a position relative to the end of the file.

f.read(a) # reads 'a' bytes of data

# closing a file
f.closed() # returns boolean on the state of the file's open or closed position
f.close() # actually does the closing


# handling I/O errors
try:
	fsock = open(filename, "rb", 0)
	try:
		fsock.seek(-128,2)
		tagData = fsock.read(128)
	finally:
		fsock.close()
except IOError:
	pass
"""
# writing to files
logfile = open("test.log", 'w')
logfile.write('test succeeded\n')
logfile.close()
print file('test.log').read()

logfile = open("test.log", 'a')
logfile.write("line 2\n")
logfile.close()
print file("test.log").read()


# iterating through a dictionary
import os
for k,v in os.environ.items():
	print "%s=%s" %(k,v)

def listDirectory(directory, fileExtList):
	"get list of file info objects for files of particular extensions"
	fileList = [os.path.normcase(f) for f in os.listdir(directory)]
	fileList = [os.path.join(directory,f) for f in fileList if os.path.splitext(f)[1] in fileExtList]
	def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
		"get file info class from filename extension"
		subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
		return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
	return [getFileInfoClass(f)(f) for f in fileList]

