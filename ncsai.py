from ncs.core import NCS_Core
x = input("\nMasukkan Kata : ")
sin = NCS_Core('db/db_kimin.ncs', 'db/stopwords.ncs', 'db/chat.ncs', 'db/python')
cos = sin.NCSAi(x)
# out = "NCS AI	      : "
print(cos)
	# for i in cos:
		# out = out + i
		# timestr = f'\r{out}'
		# sys.stdout.write(timestr)
		# sys.stdout.flush()
		# time.sleep(0.1)