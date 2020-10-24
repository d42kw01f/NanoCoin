# NanoCoin
This is a simulate of a crypto currency system using Python.



●	def Search_Genesis():
○	#check any previous blocks. When I use "a+" it will automatically create the file it there is no file in the directory.
	BlockChainFile = open(Blockchain, mode="a+")
○	#first check the TheGenesis to True. after it will use to identify whether there is any first block there.
	TheGenesis = True
○	#if there is a new block it should be Contain this header.
	BlockHeader = '*****The Hash of the Block*****'
○	#go to the first line of the BC file.
	BlockChainFile.seek(0)
	FirstLine = BlockChainFile.readline()
○	# identifing whether is fist block there by finding BCfile first line to BlockHeader.
	if FirstLine.strip() == BlockHeader.strip():
○	#if the arguement is true there is first block in the BCfile. therefore TheGenesis set to False.
		TheGenesis = False
○	#if there is no first Block in the BC file this if statement will create the first block.
	if TheGenesis is True:
		print('\nstarting the the Genesis...\n')
		print('-' * 120)
		TheTime = Time_Stamp()
		TheIndex = 0
		TheData = 'first block'
		ThePrevious = 'None'
		TheNonce = 'None'
		EnData = TheData.encode(encoding='UTF-8',errors='strict')
		sha = hashlib.sha256(EnData)
		TheDigest = sha.hexdigest()
○	#creating the new block.
		Creating_Block(TheIndex, TheTime, TheData, TheDigest, ThePrevious, TheNonce)

			PROGRAM OUTPUT: ![image](https://user-images.githubusercontent.com/72387469/97069788-2f031e80-15f0-11eb-8689-be7399ec0b25.png)

●	def Block_Index():
○	#Return the last index form the file
○	#open the file
	BlockChainFile = open(Blockchain, mode='a+')
○	#seek to the start of the file
	BlockChainFile.seek(0)
○	#file content will be listed.
	LinesList = list(BlockChainFile)
If I print LinesList out, program will show this:
 
○	#the list will be reversed from this code.
	LinesList = reversed(LinesList)
○	#remove all the whitespaces.
	Line = (Line.strip() for Line in LinesList)
○	#remove all the white spaces and black spaces
	Line = (Line1 for Line1 in Line if Line1)
○	#set a count to 0
	Number = 0
○	# read every single line in the BC file.
	for Line1 in Line:
		Number += 1
○	# get the sixth line because it is the line that contains the index(The List has been reversed.)
		if Number == 6:
Which is this:
	 
○	# get the last data in that line.
			LastIndex = int(Line1[10:])
	If I print LastIndex out, program will show this:
 
which is the index number of the last block. 

○	# increase that last block index, and it will get the new block index.
			LastIndex + 1
			break
	BlockChainFile.close()

●	def Block_Data():
#Return last line from Transection.txt file
	LedgerFile = open(Transaction, mode='a+')
	LedgerFile.seek(0)
○	#Transaction file content will be listed.
	FileLines = list(LedgerFile)
○	#List will be reversed.
	Lines = reversed(FileLines)
○	#Remove all the whitespaces and blank spaces.
	Lines = (Line.strip() for Line in Lines)
	Lines = (Line for Line in Lines if Line)
○	# Start a counter for the for loop
	for Line in Lines:
		NewTransaction = Line
		break
○	#athis will be the most recent transaction data.
	return NewTransaction

If I print NewTransactionout, the program will give the most recent value:

PROGRAM OUTPUT:
 
REAL FILE(Transaction.txt):
 

	
●	def Pre_Block_Hash():
	BlockChainFile = open('Blockchain.txt', mode='a+')
	BlockChainFile.seek(0)
	Lines = list(BlockChainFile)
	Lines = reversed(Lines)
	Lines = (Line.strip() for Line in Lines)
	Lines = (Line for Line in Lines if Line)
	Lines = list(Lines)
●	#Trim the reversed list to just the first (last) 6 lines,
●	#these are the lines that only contains important data about the transaction. 
	Lines = Lines[1:6]
Which means this:
 
If I print Lines:
 
●	#reversed the line.
	Lines = reversed(Lines)
	Lines = list(Lines)
	Number = 0
	for Line in Lines:
		Lines[Number] = Line.strip()
●	#this will give you only the values(Data). Without “Index: ,Data: ,Previous Hash: ,Nonce: “
		Lines[Number] = Line[10:]
If I print Lines[Number] output is:
	 
		Number += 1
	sha = hashlib.sha256()
	for Line in Lines:
●	#encode each line update it to sha.
sha.update(Line.encode(encoding='UTF-8',errors='strict'))
	BlockChainFile.close()
	return sha

FUNCTION FINAL OUTPUT:
 

●	def Create_New_Block():
○	#call the important functions
○	#get the time.
	Time = Time_Stamp()
○	#get the new block index.
	BlockIndex = Block_Index()
○	#get the data of the new block
	Data = Block_Data()
○	#get the previous hash value.
	PreHash = Pre_Block_Hash()
	Nonce = 0
○	#encode the string
	EnBlockIndex = (str(BlockIndex)).encode(encoding='UTF-8',errors='strict')
	EnTime = Time.encode(encoding='UTF-8',errors='strict')
	EnData = Data.encode(encoding='UTF-8',errors='strict')
	PreBlockHash = PreHash.hexdigest()
	EnPreBlockHash = PreBlockHash.encode(encoding='UTF-8',errors='strict')
○	#create the block
	TheBlock = '{}{}{}{}'.format(EnBlockIndex, EnData, EnTime, EnPreBlockHash)
	TheBlock = TheBlock.encode(encoding='UTF-8',errors='strict')
	while True:
○	#set the new block hash to none.when this looping it is important to set to None.
		NewBlockHash = None
		NewBlockHash = hashlib.sha256()
		NewBlockHash.update(TheBlock)
○	#encode the Nonce value
		EnNonce = (str(Nonce)).encode(encoding='UTF-8',errors='strict')
○	#and update it into NewBlockHash.
		NewBlockHash.update(EnNonce)
		Digits = NewBlockHash.hexdigest()
○	#leading Fouteen Zeros
		FourteenDigits = Digits[0:3]
		Zeros = '0' * 3
○	#searching fouteen zeros in the front of the
		if (FourteenDigits == Zeros):
			Creating_Block(BlockIndex, Time, Data, Digits, PreBlockHash, Nonce)
			break
○	#searching nonce 50000 or more than that
		if Nonce >= 50000:
			Creating_Block(BlockIndex, Time, Data, Digits, PreBlockHash, Nonce)
○	# Per instructions call it quits at nonce value of 50 000
			break
○	#increasing Nonce while looping.
		Nonce += 1
PROGRAM OUTPUT:
 
REAL FILE(Transaction.txt):
 
