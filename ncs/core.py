import json, os, math, time, sys, random
class NCS_Core:
	def __init__(ncs,  dasar, stopword, db, db_script):
		ncs.dasar = dasar
		ncs.stopword = stopword
		ncs.db = db
		ncs.script = db_script
	
	def GetSC(ncs, sc):
		file = os.listdir(f"{ncs.script}/{sc}")
		hasil = random.choice(file)
		with open(f"{ncs.script}/{sc}/{hasil}",'r') as dataku:
			sin = dataku.read()
		return sin

	def BukaDb(ncs, path):
		with open(path) as dataku:
			sin = json.loads(dataku.read())
		return sin

	def Hapus_Sufix(ncs, kata):
		def hapus_akhir(string, old, new):
			return new.join(string.rsplit(old, 1))
		data = ncs.BukaDb(ncs.dasar)
		data = data['sufix']
		hasil = ""
		for i in data:
			total = len(i)
			if i in kata:
				if kata[kata.rfind(i)+total:] == "":
					hasil = hapus_akhir(kata, i, '')
				else:
					if kata[kata.rfind(i)+total:] in data:
						continue
					hasil = kata
		if len(hasil) < 4:
			return kata
		return hasil
	  
	def Hapus_prefix(ncs,kata):
		datas = ncs.BukaDb(ncs.dasar)
		data = datas['prefix']
		for i in data:
			total = len(i)
			if i in kata:
				# return kata.replace(i, '')[0:1:]
				if kata.replace(i, '')[1:2:] in datas["vocal"]:
					if len(kata.replace(i, '')) > 3:
						return kata.replace(i, '')
				else:
					if len(kata.replace(f"{i}r", '')) > 3:
						return kata.replace(f"{i}r", '')
		return kata
	
	def Transfrom(ncs, data):
		with open(ncs.stopword,'r') as dataku:
			sin = dataku.read().splitlines()
		hasil = []
		for i in data:
			if not i in sin:
				hasil.append(i)
		return hasil
	
	def GetTf(ncs, data):
		db = ncs.BukaDb(ncs.db)
		hasil = []
		for a in db['data']:
			# return a
			ttl = a['pertanyaan'].count(data)
			if ttl == 0:
					tf= 0
			else:
					tf = math.log10(ttl) +1
			hasil.append(tf)
		return hasil

	def GetIdf(ncs, data):
		db = ncs.BukaDb(ncs.db)
		hasil = []
		n = len(db['data'])
		temp = 0
		for i in db['data']:
			ttl = i['pertanyaan'].count(data)
			temp += ttl

		if temp > 0:
			return math.log10(n / temp)
		elif temp < 0:
			return 0
	
	def GetTFIDF(ncs, data, idf):
		tf = ncs.GetTf(data)
		hasil = []
		for i in tf:
			hasil.append(i * idf)
		return hasil
	
	def Parse_Kalimat(ncs, kalimat):
		hasil = []
		for i in kalimat.lower().split(" "):
			hasil.append(i)
		return hasil
	
	def GetJawaban(ncs, data):
		jawab = max(data)
		no = data.index(jawab)
		db = ncs.BukaDb(ncs.db)
		label = db['data'][no]['label']
		hasil = db['data'][no]['jawab']
		if label == 1:
			hasil = ncs.GetSC(hasil)
		return hasil
	
	def NCSAi(ncs, quest):
		kata = ncs.Parse_Kalimat(quest)
		kata2 = ncs.Transfrom(kata)
		hasil = []
		for i in kata2:
			awal = ncs.Hapus_prefix(i)
			
			akhir = ncs.Hapus_Sufix(awal)
			
			tf = ncs.GetTf(akhir)
			idf = ncs.GetIdf(akhir)
			if not idf is None:
				tfidf = ncs.GetTFIDF(akhir, idf)
				# print("idf : ",idf)
				# print("TF-IDF : ", tfidf)
				hasil.append(tfidf)

		akhir = []
		if len(hasil) > 0:
			for i in range(len(hasil[0])):
				temp = 0
				for a in hasil:
					temp += a[i]
				akhir.append(temp)

		if len(akhir) > 0:
			jawab = ncs.GetJawaban(akhir)
			return jawab
		elif len(akhir) == 0:
			return "Maaf Saya Tidak Mengerti Maksud Anda!"
