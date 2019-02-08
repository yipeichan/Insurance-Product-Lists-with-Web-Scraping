# Insurance Product Lists with Web Scraping
<a href="https://yipeichan.github.io"><b>Link to additional explanations</b></a>
<br>
<div class="f">
This program was written because I have to do insurance market investigation weekly at work. Information such as products dicontinued, new products being launched, coverage of policies and so on would be recorded and later be genreated as a report. In Taiwan it is regulated by law that the loading of certain ages, clause and exception clause be disclosed publicly on the internet. While large insurance companies in Taiwan often provide 100 to 200 insurance contracts, it is not efficient to go through webpages to find new products, or discontinued ones.  Therefore, I wrote the program to generate lists weekly to track newly launched/ discontinued product in the insurance market.<br><br></div>

## Method:

1. First part: Extracting information from the web<br> 
The program extract all the names of products available from the site of the targeted insurance company; <br>
it then export the information into seperated csv files according to the category of insurance (ex. life/ health/ accident/ annuities/ annuity, etc) with the inputed date added at the end of the name of the csv files

2. Second part of the program: Comparing lists<br>
The program can compare product lists of two designated dates(ex. all types of insurances of 20180716 vs those of 20180709 ) and produce outcomes of new products that had been luanched (i.e newly posted on the site) within the period and what had been discontinued (i.e no longer on the site)<br><br>

## Instructions: <br>
1. Enter the path of the directory of your files:<br>
<img width="1226" alt="demo1" src="https://user-images.githubusercontent.com/24948460/46902893-ada42c00-ceff-11e8-92b2-a18f776b0391.png">

<br>
2. If you want to obtain the updated product lists, enter y, otherwise n (see point 4) <br>
   After entering y, input the date and the date will automatically be added to csv files (csv files be seperated according to the category of insurances)<br>
<img width="1099" alt="demo2" src="https://user-images.githubusercontent.com/24948460/46902904-e2b07e80-ceff-11e8-81c5-735ece2ffca6.png">

<br>
3. Enter the dates of the files to be compared, and the result would display the products new launched/ discontinued or sales channel changes within the period. <br>
<img width="851" alt="demo3" src="https://user-images.githubusercontent.com/24948460/46902908-ea702300-ceff-11e8-9dcc-f5ac2eb5bf00.png">

<br>
4. (continued with point 2) user can directly compare lists of two dates or simply two csv files without renewing product lists.<br> 
To compare all lists (i.e all kinds of insurance) of two dates, enter 1  <br>
To compare only two csv files, enter 2 (see point 6) <br>
<img width="1138" alt="demo4" src="https://user-images.githubusercontent.com/24948460/46902909-ea702300-ceff-11e8-9c3f-d35bd38c2eee.png">

<br>
5. The result of comparison would be displayed <br>
<img width="1131" alt="demo5" src="https://user-images.githubusercontent.com/24948460/46902910-eb08b980-ceff-11e8-93f3-9022ab6e2a61.png">

<br>
6. (continued with point 4) Enter the two file names to be compared, and Tthe result of comparison would be displayed <br>
<img width="1076" alt="demo6" src="https://user-images.githubusercontent.com/24948460/46902966-d37e0080-cf00-11e8-8fc5-846aafc5cd93.png">








   

