######for fubon insurance group product tracing

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
		print("新開商品：\n",list(set(new)-set(previous)),"\n")
		print("停售商品：\n",list(set(previous)-set(new)),"\n")
	def request(filename,page):			###write page content into csv
		csv_file = open(os.path.join(myPath, filename),'a', newline='',encoding='utf-8-sig')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([" ".join(date.split())])
		res=requests.get(page)
		res.raise_for_status()
		res.encoding='CJK'
		soup=bs4.BeautifulSoup(res.text,"html.parser")
		for i in soup.select('.title-13px'):
			insurance =i.text
			insurance=" ".join(insurance.split())
			#print(" ".join(insurance.split()))
			csv_writer.writerow([insurance.replace(u'\ufeff', '')])
		csv_file.close()
	def setdate():
		date=input("set the date in the file name: ")
		return date

print("\n===============================")
product_type=['保障型商品','利變型商品','oiu商品','實物給付商品','銀行商品']
report.set_path()
renew=input("Renew the product lists? y/n: ")

if renew=="n":
	print("process moves to list comparison")

elif renew=="y":
	print("the progam is exporting product lists from the web")
	#date=input("set the date in the file name: ")
	date=report.setdate()
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_periodf.htm')
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_healthf.htm')
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_alllifef.htm')
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_injuref.htm')
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_elderf.htm')
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_nodealf.htm')
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_bonusf.htm')
	report.request(product_type[0]+date+'.csv','https://www.fubon.com/life/indemnify_prod/ins_annuityf.htm')

	report.request(product_type[1]+date+'.csv','https://www.fubon.com/life/indemnify_prod/prf_changef.htm')
	report.request(product_type[2]+date+'.csv','https://www.fubon.com/life/indemnify_prod/oiu_alllifef.htm')
	report.request(product_type[3]+date+'.csv','https://www.fubon.com/life/indemnify_prod/real_alllifef.htm')

	report.request(product_type[4]+date+'.csv','https://www.fubon.com/life/indemnify_prod/spe_periodf.htm')
	report.request(product_type[4]+date+'.csv','https://www.fubon.com/life/indemnify_prod/spe_healthf.htm')
	report.request(product_type[4]+date+'.csv','https://www.fubon.com/life/indemnify_prod/spe_alllifef.htm')
	report.request(product_type[4]+date+'.csv','https://www.fubon.com/life/indemnify_prod/spe_injuref.htm')
	report.request(product_type[4]+date+'.csv','https://www.fubon.com/life/indemnify_prod/spe_elderf.htm')
	report.request(product_type[4]+date+'.csv','https://www.fubon.com/life/indemnify_prod/spe_bonusf.htm')
	print("product lists are done\n")

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
