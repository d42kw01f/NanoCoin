import string
import random

def Transaction():
	SenderName = ''
	#asking user to enter the sender's name
	while SenderName.isalpha() is False:
	        SenderName = input("Enter the sender\'s name\n(make sure only to use letters and the maximum length is 10): ").strip().casefold()
	        RealSender = SenderName[0:10]
	        print('-----sending from ', RealSender, sep = '-> ', end='-----\n')
	#asking user to enter the Recipient's name
	RecipientName = ''
	while RecipientName.isalpha() is False:
	        RecipientName = input("Enter the recipient\'s name\n(make sure only to use letters and the maximum length is 10): ").strip().casefold()
	        RealRecipient = RecipientName[0:10]
	        print('-----sending to ', RealRecipient, sep = '-> ', end='-----\n')
	#asking user to enter the amount the want to send
	Amount = ''
	while(Amount.isdigit() is False):
	        Amount = input("Enter the amount you want to send to\n(make sure only to use digits and maximum lenght is 10): ")
	        RealAmount = Amount[0:10]
	        print('-----sending to ', RealAmount, sep = '-> ', end='-----\n')
	print('*' * 80)
	print('sending {} amount'.format(RealAmount), 'to {}'.format(RealRecipient), 'from {}'.format(RealSender), sep=' || ')


	try:
#creating the file and open it
		FileName = 'Transaction.txt'
		TheFile = open(FileName, mode='a+')
		sender = RealSender.ljust(10)
		recipient = RealRecipient.ljust(10)
#write the data on the file
		TheFile.write('|Sender: ' + sender)
		TheFile.write('|Reciver: ' + recipient)
		TheFile.write('|Amount: ' + RealAmount + '\n')
#if file cannot be opened or written on it
	except FileNotFoundError:
		print('OOPS!!!\nFound some problems with {} this file\nPlease start over.'.format(FileName))
		print('Shouting Down the program...')
		quit()

def Main_Program():
	try:
		while True:
#prompt user to continue or kill the program
			UserInput = ''
			while (UserInput != 'yes') and (UserInput != 'no'):
				print('-' * 110)
				UserInput = input('Do you to make a transaction\nEnter \'yes\' if you want: ').strip().casefold()
				if UserInput == 'yes' or UserInput == 'y':
					Transaction()
				if UserInput == 'no' or UserInput == 'n':
					quit()
#stop the program
	except KeyboardInterrupt:
		quit()

Main_Program()
