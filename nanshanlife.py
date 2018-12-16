######for nanshan life insurance group product tracing

import requests
import os
import bs4
import csv


class report:
	def __init__(self, new, previous, date):
		self.new=new
		self.previous=previous
		self.date=date
	def set_path():
		global myPath
		myPath=input("Enter the path of the directory: ")
		return myPath
	def open(filename):						####read csv
		with open(os.path.join(myPath, filename), 'rU',encoding='utf-8-sig') as csvfile:
			readCSV=csv.reader(csvfile, delimiter=',')
			insurances=[]
			p_final=[]
			for insurance in readCSV:
				insurances.append(" ".join(insurance))
			for word in insurances:
				insurance=word.replace(" ", "")
				p_final.append(insurance.replace(u'\ufeff', ''))
			return p_final 
	def compare(new,previous):			####compare products in two csvs
		print("Newly Launched：\n",list(set(new)-set(previous)),"\n")
		print("Discontinued：\n",list(set(previous)-set(new)),"\n")
	def request(filename,page):			###write page content into csv
		csv_file = open(os.path.join(myPath, filename),'a', newline='',encoding='utf-8-sig')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([" ".join(date.split())])
		res=requests.get(page)#
		#res.raise_for_status()
		#res.encoding='CJK'
		soup=bs4.BeautifulSoup(res.text,"html.parser")
		for i in soup.select('.text-center'):
			insurance =i.text
			insurance=" ".join(insurance.split())
			#print(" ".join(insurance.split()))
			csv_writer.writerow([insurance.replace(u'\ufeff', '')])
		csv_file.close()
	def request_addition(filename,page):			###because the class at 網路投保商品 product page is different from others
		csv_file = open(os.path.join(myPath, filename),'a', newline='',encoding='utf-8-sig')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([" ".join(date.split())])
		res=requests.get(page)#
		#res.raise_for_status()
		#res.encoding='CJK'
		soup=bs4.BeautifulSoup(res.text,"html.parser")
		for i in soup.select('.proText02'):
			insurance =i.text
			insurance=" ".join(insurance.split())
			#print(" ".join(insurance.split()))
			csv_writer.writerow([insurance.replace(u'\ufeff', '')])
		csv_file.close()
	def request_addition_2(filename,page):			###網路年金險 because the class at 網路投保商品 product page is different from others
		csv_file = open(os.path.join(myPath, filename),'a', newline='',encoding='utf-8-sig')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([" ".join(date.split())])
		res=requests.get(page)#
		#res.raise_for_status()
		#res.encoding='CJK'
		soup=bs4.BeautifulSoup(res.text,"html.parser")
		for i in soup.select('.proBut02'):
			insurance =i.text
			insurance=" ".join(insurance.split())
			#print(" ".join(insurance.split()))
			csv_writer.writerow([insurance.replace(u'\ufeff', '')])
		csv_file.close()
	def request_addition_3(filename,page):			###because the class at oiu商品 product page is different from others
		csv_file = open(os.path.join(myPath, filename),'a', newline='',encoding='utf-8-sig')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([" ".join(date.split())])
		res=requests.get(page)#
		#res.raise_for_status()
		#res.encoding='CJK'
		soup=bs4.BeautifulSoup(res.text,"html.parser")
		for i in soup.select('.title-h3'):
			insurance =i.text
			insurance=" ".join(insurance.split())
			#print(" ".join(insurance.split()))
			csv_writer.writerow([insurance.replace(u'\ufeff', '')])
		csv_file.close()	
	def setdate():
		date=input("set the date in the file name: ")
		return date

print("\n===============================")
product_type=['ProtectionProducts','SavingProducts','HealthProducts','BankProducts','OIU','GroupInsurance','InternetProducts']
report.set_path()
renew=input("Renew the product lists? y/n: ")

if renew=="n":
	print("process moves to list comparison")

elif renew=="y":
	print("the progam is exporting product lists from the web")
	#date=input("set the date in the file name: ")
	date=report.setdate()

	for i in range(10,14):	
		report.request(product_type[0]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/'+str(i))
	#report.request(product_type[0]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/11')
	#report.request(product_type[0]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/12')
	#report.request(product_type[0]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/13')
	#=========
	for i in range(15,21):	
		report.request(product_type[1]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/'+str(i))
	#=========
	report.request(product_type[2]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/23')
	report.request(product_type[2]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/24')
	report.request(product_type[2]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/26')
	report.request(product_type[2]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/27')
	report.request(product_type[2]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/28')
	report.request(product_type[2]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/29')
	report.request(product_type[2]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/30')
	#==========
	for i in range(35,41):
		report.request(product_type[3]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/'+str(i))
	#==========		
	report.request_addition_3(product_type[4]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/static-sidebar/60')
	#==========
	for i in range(272,276):
		report.request(product_type[5]+date+'.csv','https://www.nanshanlife.com.tw/NanshanWeb/product/'+str(i))
	#========== 網路商品
	report.request_addition(product_type[6]+date+'.csv','https://www.nanshanlife.com.tw/public_promotion/subject/OnlineInsurance/productList.html')
	report.request_addition_2(product_type[6]+date+'.csv','https://www.nanshanlife.com.tw/public_promotion/subject/OnlineInsurance/productList.html')


else:
	print("wrong input")

print("===============================")
renew=input("to compare all lists, please input: 1 \nto compare only two lists, please input: 2\nyour input: ")
if renew=="1":
	new_file=input("Enter the date of the new file: ")
	old_file=input("Enter the date of the previous file: ")
	for i in product_type:
		a=report.open(i+new_file+'.csv')
		b=report.open(i+old_file+'.csv')
		print("\n",i)
		report.compare(a,b)
		print("\n")


elif renew=="2":
	new_file=input("Enter the name of the new file: ")
	old_file=input("Enter the name of the previous file: ")
	a=report.open(new_file)
	b=report.open(old_file)
	report.compare(a,b)

else:
	print("wrong input")

exit=input("Quit the program?: ")
print(exit)
