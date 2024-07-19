import requests,sys

def download(savePath, url,year):
	res = requests.get(url,stream=True)
	if(res.status_code==200):
		with open(savePath , "wb") as f:
			f.write(res.content)
	else:
		print("No paper found for year :-", year)

# url = "https://gtu.ac.in/uploads/S2018/BE/3110018.pdf"
baseUrlForS = "https://gtu.ac.in/uploads/S"
baseUrlForW = "https://gtu.ac.in/uploads/W"

branchcode = "BE/"

subjectCode = sys.argv[1]
subjectName = sys.argv[2]

startYear = sys.argv[3]
endYear = sys.argv[4] 

year = int(startYear);

while (year <= int(endYear)):

	urlForS = baseUrlForS+str(year)+"/"+branchcode+subjectCode+".pdf"
	download(subjectName+"-"+"S"+str(year)+".pdf", urlForS,"S"+str(year))

	urlForW = baseUrlForW+str(year)+"/"+branchcode+subjectCode+".pdf"
	download(subjectName+"-"+"W"+str(year)+".pdf", urlForW,"W"+str(year))

	year +=1
