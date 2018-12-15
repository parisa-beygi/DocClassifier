from HamshahriReader import HamshahriReader
import pickle
import time

directory = '/media/parisa/Windows7_OS/Documents and Settings/Parisa/Documents/Courses/term2/NLP/HWs/HW1/HAM2-corpus-short-with-tag-selected.txt'
# directory = 'HAM2-corpus-short-with-tag-selected.txt'
hr = HamshahriReader()
read_start = time.time()
hr.read(directory)
elapsed_read = time.time() - read_start

with open('resources/hr.pkl', 'wb') as output:
	pickle.dump(hr, output, pickle.HIGHEST_PROTOCOL)

print('reading time: ' + str(elapsed_read))

hr.print_wordDict()
hr.print_categories()
