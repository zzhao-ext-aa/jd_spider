# jd_spider
Scrapy Samsung all the smart phone's model name and pricing from http://www.jd.com/ and save them into CSV file

An asterisk being added after the model name if it's sold by JD 

Usage:

1.Make sure your mac has installed with Firefox(47.0.1) Python(2.6) Scrapy(1.3.3) Selenium(2.53.6)
  
2.Open iterm and go to the below directory
  
      /tutorial/tutorial/
      
3.Make sure your python path is correct. if not, run belowed command
      
      export PYTHONPATH=$(pwd)   
      
4.Run following command to start the project
      
      scrapy crawl jd_phone
      
  The Firefox browser will automatically open
  
5.Once the task finished, the Firefox browser will automatically shut down and the CSV file will save into the current directory, the file name is "result_phone.csv"
