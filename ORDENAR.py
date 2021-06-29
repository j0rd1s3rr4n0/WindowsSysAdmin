import os
gg = 0
carpet = ['ORDENADO','ORDENADO\\Video','ORDENADO\\Foto','ORDENADO\\Script','ORDENADO\\Exe','ORDENADO\\Doc']
vidext = ['*.mp4','*.webm','*.gif'] 
imgext = ['*.png','*.jpg','*.jpeg','*.ico','*.webp','*.md']
docext = ['*.pdf','*.txt','*.docx','*.zip','*.7z','*.rar','*.csv','*.xlsx','*.pptx']
scrext = ['*.py','*.pyw','*.cmd','*.bat','*.html','*.xml','*.php','*.sh']
exeext = ['*.exe']
audext = ['*.mp3']
carpo = len(carpet)
print(carpo)
vidin = len(vidext)
print(vidin)
lenin = len(imgext)
print(lenin)
pfin = len(docext)
print(pfin)
scct = len(scrext)
print(scct)
exte = len(exeext)
print(exte)

"""
print('CREANDO CARPETAS')
for t in carpet:
	pel = str(carpet[int(gg)])
	os.mkdir(str(carpet[int(gg)]))
	print(pel)
	gg = gg+1
"""
gg = 0
print('VIDEO')
for x in vidext:
	lel ="move /-Y"+" C:\\Users\\Jordi\\Desktop\\"+str(vidext[int(gg)])+" "+"C:\\Users\\Jordi\\Desktop\\ORDENADO\\Video\\"
	os.system(lel)
	#print(lel)
	gg = gg+1

gg = 0
print('IMG')
for c in imgext:
	nel ="move /-Y"+" C:\\Users\\Jordi\\Desktop\\"+str(imgext[int(gg)])+" "+"C:\\Users\\Jordi\\Desktop\\ORDENADO\\Foto\\"
	os.system(nel)
	#print(nel)
	gg = gg+1

gg = 0
print('DOC')
for v in docext:
	eel ="move /-Y"+" C:\\Users\\Jordi\\Desktop\\"+str(docext[int(gg)])+" "+"C:\\Users\\Jordi\\Desktop\\ORDENADO\\Doc\\"
	os.system(eel)
	#print(eel)
	gg = gg+1

gg = 0
print('SCRIPT')
for b in scrext:
	gel ="move /-Y"+" C:\\Users\\Jordi\\Desktop\\"+str(scrext[int(gg)])+" "+"C:\\Users\\Jordi\\Desktop\\ORDENADO\\Script\\"
	os.system(gel)
	#print(gel)
	gg = gg+1
gg = 0
print('EXE')
for d in exeext:
	hel ="move /-Y"+" C:\\Users\\Jordi\\Desktop\\"+str(exeext[int(gg)])+" "+"C:\\Users\\Jordi\\Desktop\\ORDENADO\\Exe\\"
	os.system(hel)
	#print(hel)
	gg = gg+1

gg = 0
print('AUDIO')
for j in audext:
	mel ="move /-Y"+" C:\\Users\\Jordi\\Desktop\\"+str(audext[int(gg)])+" "+"C:\\Users\\Jordi\\Desktop\\ORDENADO\\Exe\\"
	os.system(mel)
	#print(mel)
	gg = gg+1
