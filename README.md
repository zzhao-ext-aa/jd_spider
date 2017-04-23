# jd_spider
Scrapy all the smart phone's model name and pricing from http://www.jd.com/ and save them into CSV file
An asterisk being added after the model name if it's sold by JD 

Usage:
1.Make sure your mac has installed with Firefox(47.0.1) Python(2.7) Scrapy(1.3.3) Selenium(2.53.6) Pycharm
2.Open the project with Pycharm,make sure your virtualenv has including Python Scrapy and Selenium packages:
      Perference-->Project:tutorial-->Project Interpreter 
  choose the correct virtualenv
  you can add these packages by clicking the "+"  
3.Open iterm and go to the below directory
      /tutorial/tutorial/
4.Make sure your python path is correct. if not, run belowed command
      export PYTHONPATH=$(pwd)   
5.Run below command to start the project
      scrapy crawl jd_phone
  you can see the Firefox browser automatically open
6.If the project finished, the Firefox browser automatically shuts down and the CSV file will saved into the current directory,the file is "result_phone.csv"
