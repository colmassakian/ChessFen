from selenium import webdriver 

class piece:
	def __init__(self, file, rank, pieceID):
		self.file = file
		self.rank = rank
		self.pieceID = pieceID

# https://www.chess.com/puzzles/battle/2KDwKNvb8
def getFEN(link): 
	activePieces = []

	# TODO: Use chrome driver in headless form
	driver = webdriver.Firefox()
	driver.get(link)

	parent = driver.find_element_by_class_name('pieces')
	try:
	    piecesList = parent.find_elements_by_tag_name('div')
	except:
		print("Error opening link")

	for currPiece in piecesList:
		# Find currPiece id in dom, if error, continue
		try:
			file = int(currPiece.get_attribute("class")[14])
		except:
			continue
		
		rank = int(currPiece.get_attribute("class")[16])

		# Split string to isolate the two characters that specify the color and type of each piece
		generalType = currPiece.get_attribute("style").split(".")
		pieceID = generalType[2].split("/")[-1]

		activePieces.append(piece(file, rank, pieceID))

	result = ""
	currRank = []

	for i in range(8, 0, -1):
		# Group pieces on the same rank
		for currPiece in activePieces:
			if currPiece.rank == i:
				currRank.append(currPiece)
		
		sortByFile = sorted(currRank, key=lambda x: x.file)
		
		# Go through sorted file and place pieces or gaps as necessary for FEN
		prev = 0
		for pos in sortByFile:
			fileDiff = pos.file - prev - 1
			if fileDiff != 0:
				result += str(fileDiff)

			if pos.pieceID[0] == 'w':
				result += (pos.pieceID[1]).upper()
			else:
				result += pos.pieceID[1]

			prev = pos.file

		# No slash after last rank
		if i != 1:
			result += '/'

		del currRank [:]

	return result

