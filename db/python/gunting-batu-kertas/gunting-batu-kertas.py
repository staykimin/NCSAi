import random

def checkForWin(user,computer):
	if(user == "batu"):
		if(computer == "batu"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : draw")
		elif(computer == "kertas"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : lose")
		elif(computer == "gunting"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : win")
	elif(user == "kertas"):
		if(computer == "batu"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : win")
		elif(computer == "kertas"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : draw")
		elif(computer == "gunting"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : kalah")
	elif(user == "gunting"):
		if(computer == "batu"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : lose")
		elif(computer == "kertas"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : win")
		elif(computer == "gunting"):
			print("user : ",user,"\ncomputer : ",computer,"\nstatus : draw")

looping = True
while(looping):
	option = ['gunting','kertas','batu']
	user = input("pilih salah satu (gunting,batu,kertas)")
	computer = random.choice(option)
	checkForWin(user,computer)
	confirm = input('coba lagi? y/n')
	if(confirm == 'n'):
		looping = False
