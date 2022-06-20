import os
import music21 

def preprocessing(data):
	pass
	
def load(data):
#os walk recursively goes through folder structure
	for path,subdr,files in os.walk(data):
		for file in files:
			if file[-3:]=="krn":
				music=music21.converter.parse(os.path.join(path,file))

