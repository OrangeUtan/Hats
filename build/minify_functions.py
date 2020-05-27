import os

def get_functions(root):
	for root, dirs, files in os.walk(root):
		for file in files:
			_, extension = os.path.splitext(file)
			if extension == '.mcfunction':
				yield os.path.join(root, file)

for function in get_functions('datapack/data/hats/functions'):
	print(function)
	lines = open(function).readlines()
	lines = filter(lambda l: not l.strip().startswith('#'), lines) # Remove comments
	lines = filter(lambda l: l.strip(), lines) # Remove blank lines
	lines = map(lambda l: l.lstrip(), lines) # Remove whitespace
	
	open(function, 'w').writelines(lines)