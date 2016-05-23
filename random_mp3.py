import sys, os, random, glob, shutil, argparse

def toMb(sizeInBytes):
	return sizeInBytes / 1024 / 1024

def toBytes(sizeInMb):
	return sizeInMb * 1024 * 1024

def copyFiles():
	parser = argparse.ArgumentParser(description='Copy random mp3s files')
	parser.add_argument('source', metavar='source', help='Folder where the mp3 files must be copied from')
	parser.add_argument('dest', metavar='dest', help='Destination folder where the mp3 files must be copied to')
	parser.add_argument('limit', metavar='limit', type=int, help='Size limit to copy (in Mb)')
	parser.add_argument('-v', dest='verbose', required=False, action='store_true', help='verbose mode')

	args = parser.parse_args()
	source = args.source
	source += '**/*.mp3'
	dest = args.dest
	limit = toBytes(args.limit)
	size = 0
	allFiles = glob.glob(source, recursive=True)
	random.shuffle(allFiles) # Extra shuffling
	while size < limit and len(allFiles) > 0:
		chosen = random.choice(allFiles)
		try:
			shutil.copy(chosen, dest)
			size += os.stat(chosen).st_size
		except:
			try: 
				print ('Error copying ' + chosen)
			except:
 				print ('You have a song with a messy name!')
		if args.verbose:
			print("Copying " + chosen + "\n\t(" + str(int(toMb(size))) + " Mb of " + str(toMb(limit)) + " Mb)")
		else:
			sys.stdout.write("Copying %d Mb of %d Mb \r" % ((toMb(size)), (toMb(limit))) )
			sys.stdout.flush()
		allFiles.remove(chosen)

	if size < limit:
		print("Insufficient files to reach the specified limit")
if __name__ == "__main__":
	copyFiles()
