######for Tracing Products of China Life Insurance Group  

import requests
import os
import bs4
import csv


class report:
	def __init__(self, new, previous, date):
		self.new=new
		self.previous=previous
		self.date=date
	def set_path():						#set the path of the directory
		global myPath
		myPath=input("Enter the path of the directory: ")
		return myPath
	def open(filename):						####read csv
		with open(os.path.join(myPath, filename), 'rU') as csvfile:
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
		print("Newly Launched:\n",list(set(new)-set(previous)),"\n")
		print("Discontinued:\n",list(set(previous)-set(new)),"\n")
	def request(filename,page):			###write page content into csv
		csv_file = open(os.path.join(myPath, filename),'a', newline='',encoding='utf-8-sig')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([" ".join(date.split())]) ###leave out blank spaces in the name
		res=requests.get(page)
		#res.raise_for_status()
		#res.encoding='CJK'
		soup=bs4.BeautifulSoup(res.text,'lxml')
		for i in soup.select('.panel-header'):
			insurance =i.text
			insurance=" ".join(insurance.split())
			#print(" ".join(insurance.split()))
			csv_writer.writerow([insurance.replace(u'\ufeff', '')])
		csv_file.close()
	def setdate():
		date=input("set the date in the file name: ")
		return date

print("\n===============================")
product_type=['Life_Insurance','Annuity_Insurance','Health_Insurance','Travel_Accident_Insurance']
report.set_path()
renew=input("Renew the product lists? y/n: ")

if renew=="n":
	print("process moves to list comparison")

elif renew=="y":
	#date=input("set the date in the file name: ")
	date=report.setdate()
	print("the progam is exporting product lists from the web")	
	report.request(product_type[0]+date+'.csv','https://www.chinalife.com.tw/wps/portal/chinalife/product-overview/personal/life-refund')	
	report.request(product_type[1]+date+'.csv','https://www.chinalife.com.tw/wps/portal/chinalife/product-overview/personal/annuity-assurance')
	report.request(product_type[2]+date+'.csv','https://www.chinalife.com.tw/wps/portal/chinalife/product-overview/personal/health')
	report.request(product_type[3]+date+'.csv','https://www.chinalife.com.tw/wps/portal/chinalife/product-overview/personal/travel')

	print("product lists are prepared\n")

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
