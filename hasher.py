import argparse
import os
import hashlib
import shutil
from termcolor import colored


def parse_arguments():
	# Setup argument parser
	parse = argparse.ArgumentParser(description='Python hashing and de-duplicator.')
	
	parse.add_argument('--input-folder', type=str, default='input', help='root directory of input folder (default: input).')
	parse.add_argument('--output-folder', type=str, default='output', help='root directory of output folder (default: output).')
	
	return parse.parse_args()


def print_configuration(args):
	print('--- Configuration ---')
	
	# Command line arguments
	for key, value in vars(args).items():
		print(f'{key.replace("_", " ").title()}: {value}')


def find_files(input_folder):
	print('--- Locate Files ---')
	files = {}
	
	for root, directories, filenames in os.walk(input_folder):
		for file in filenames:
			files[os.path.join(root, file)] = None

	return files


def calculate_hash(path):
	with open(path, 'rb') as file:
		hasher = hashlib.sha256()
		chunk_size = 1048576 
		
		# Read files over 1GiB in 1MiB chunks
		if os.stat(path).st_size < 1073174824:
			data = file.read()
			hasher.update(data)
		else:
			data = file.read(chunk_size)
			while len(data) > 0:
				hasher.update(data)
				data = file.read(chunk_size)

	return hasher.hexdigest()


def hash_files(files):
	print('--- Hash Files ---')
	counter = 0
	
	for key, value in files.items():
		file_hash = calculate_hash(key)
		counter += 1
		progress_counter = f'[{counter}/{len(files)}]'
		
		if check_unique(files, file_hash):
			files[key] = file_hash
			print(f'{progress_counter:15} {key.rsplit("/", 1)[1]:24} {file_hash:64}')
		else:
			print(f'{progress_counter:15} {key.rsplit("/", 1)[1]:24} {file_hash:64} {colored("* DUPLICATE *", "red")}')


def check_unique(files, file_hash):
	if file_hash not in files.values():
		return True
	else:
		return False

def organise_files(files, output_folder):
	print('--- Organising Files ---')
	saved_files = 0
	ignored_files = 0
	
	# Make output directory if it does not exist
	if not os.path.exists(output_folder):
		os.mkdir(output_folder)
	
	for key, value in files.items():
		if value is not None:
			print(f'[{colored("+", "green")}] {"Copying":8} {key.rsplit("/", 1)[1]}')
			shutil.copy2(key, output_folder)
			saved_files += 1
		else:
			print(f'[{colored("-", "red")}] {"Ignoring":8} {key.rsplit("/", 1)[1]}')
			ignored_files += 1

	if saved_files > 0:
		print(f'Saved {saved_files} files to output folder')
	if ignored_files > 0:
		print(f'Ignored {ignored_files} ({ignored_files/len(files):.0%}) duplicate files')
	


def main():
	# Parse input arguments
	args = parse_arguments()
	print_configuration(args)
	
	if not os.path.exists(args.input_folder):
		print(f'{colored("* WARNING *", "red")} Input directory does not exist')
		return
	
	# Identify all input files
	files = find_files(args.input_folder)
	
	# Skip processing if not files were found
	if files:
		print(f'{len(files)} files found')
		
		# Hash all files
		hash_files(files)
	
		# Organise files
		organise_files(files, args.output_folder)
	else:
		print(f'{colored("* WARNING *", "red")} Input directory is empty')


if __name__ == '__main__':
	main()