This program originally started as a way to look at data for HWY 44 in Bullitt county.  This road is a 2 lane highway and has a lot of traffic, with a lot of accidents.  As i worked on the program more, I decided it would be more interesting to be able to look at any road in any county in the state of Kentucy.  Unfortunately the crash databse 
is only legally required to keep records going back 10 years.  So we will go back to 2013, and see how accidents, including injuries and fatalies have trended in this 10 year 
range.

One note of caution with this program, due to the nature of the crash database, there are quite a few pauses in the program to give the databse time to complete its current 
task. 


For this program you will need to install the following modules:
    
	Pandas
    Time
    Selenium
    Webbrowser
    Zipfile
    Glob
    OS
    Matplotlib
    
This project is done in a virutal enviroment. You can find the exact versions of each module in the requirement.txt file

*****IMPORTANT****

1. The program will download a zip file to your computer, to extract the relevent incident data.  The program will also delete the zip file once the data has been extracted.

2. Line 130 searches for the downloaded file.  The download folder will be specific to your computer, as such you will need to change the path in the parentheses

3. Line 135 extracts the file to a specific location.  Once again you will need to change this to a valid drive and folder for your computer

4. Line 143 converts the file into a data frame, and 144 then removes the file.  The file name itself will not be changed, but the path will need to be changed to the same path used in #3

5.  This project utilizes Chrome Browser.  As such, if you do not have chrome it will not work properly.  If you do not have chrome you will need to change the service variable on Line 33.



The criteria that I met for this project are as follows
    
		1. Category 1 -Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 
    
		2. Category 2 - Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.
    
		3. Category 3 - Visualize data in a graph, chart, or other visual representation of data.
    
		4. Category 4 - The program should utilize a virtual environment and document library dependencies in a requirements.txt file.
    
		5. Stretch -  Implement a web scraper
    
To run the program, you just need to run WebCrashData.py, then fill in the prompted County, and roadway number.

One last note, Some highways have a lot of accidents on them. For example, Shelbyville road (HWY 60) in Jefferson county has over 15,000 accidents.  The database will not generate a usable data set at all after around 5,000 accidents. If you try HWY 60 in Shelby county though, you get a result that is usable. 
