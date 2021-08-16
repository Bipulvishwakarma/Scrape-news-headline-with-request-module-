import requests
from bs4 import BeautifulSoup
url='https://resumes.indeed.com/search?q=software+developer&l=bangalore&searchFields='
z=requests.get(url)
htmlContent=z.content
soup=BeautifulSoup(htmlContent,'html.parser')
top=soup.find('div',class_="rezemp-ResumeSearchPage-resumeCards rezemp-ResumeSearchPage-resumeCards--withBottomPadding")
print(top)