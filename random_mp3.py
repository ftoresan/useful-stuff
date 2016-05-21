import sys, os, random, glob, shutil

def copyFiles():
	if len(sys.argv) < 3:
		print('Insufficient arguments!\n')
		print('Usage: python3 random_mp3 <source_dir> <dest_dir> [limit (Mb)]\n')
		sys.exit(0)															
	source = sys.argv[1]
	source += '**/*.mp3'
	dest = sys.argv[2]
	limit = sys.argv[3]
	limit = int(limit)
	limit *= 1024 * 1024
	size = 0
	allFiles = glob.glob(source, recursive=True)
	random.shuffle(allFiles) # Extra shuffling
	while size < limit:
		chosen = random.choice(allFiles)
		try:
			shutil.copy(chosen, dest)
			size += os.stat(chosen).st_size
		except:
			print ('Error copying ' + chosen) 		
		sys.stdout.write("Copying %d Mb of %d Mb \r" % ((size / 1024 / 1024), (limit / 1024 / 1024)) )
		sys.stdout.flush()

if __name__ == "__main__":
	copyFiles()
