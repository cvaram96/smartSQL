# smartSQL
A new solution which is named as smartSQL has been introduced here for converting natural language query into mySQL query. Most of the developers as well as end users have benefits from this solution. 
The solution is a web application which has basic facilities and some advance
facilities. SmartSQl takes the mysql database schema which is preferred by user and allows to convert user’s natural language query into mysql query based on preferred sql schema. SmartSQL gives many facilities such as creating users, storing schemas, default user settings as well as other basic web application features. More than that, user can view the database schema as table and columns.
Entire smartSQL has been developed in python environment. User can able to build Simple queries as well some complex queries using smartSQL. SmartSQL web application has been developed using Flask framework and basic python class concepts. GUI of the system is very simple and attractive.
The development of the project has been carried out under the Rational Unified Process
methodology with several iterations. The architecture of the application follows a 3-tier architecture which consists of a Presentation layer, a control layer and a database layer.
Software engineering good practices have been adopted in the development process for scheduling, requirement specification, coding and testing. python had been used as languages for coding. Testing had been carried out with pytest and sellenium testing tool.
The main constraint of smartSQL is, users should have correct tables name and columns name in their natural language query.


follow the instructions
from linux versions
open the terminal
enter the smartsql folder
if you want create an virtual enviroment then you can download all dependencies using requirements.txt
pip3 install -r requirements.txt
then run the run.py
python run.py
open your browser go to localhost:5000 to see this web application

    • When a new User enters the home page of the smartSQL.
    • User will see the all reviews of  smartSQL users 
    • It will help them to understand the sql to their problems.
    •  Person can register  a new account to become a user Using register page. 
    • After registration the user will be redirected to profile page. 

    • In the profile page, users can change their the information simple way and  database schemas which has been uploaded by user will have been displayed. User can clicks the schema to view the tables and columns in new page which as referred as schema page.

    •  In the schema page, user can type the natural language query and submit to the system. System will send this to the ln2sql. Ln2sql takes the natural language query and parses it  using database schema. The result which has been produced by ln2sql will be displayed in the same window. 

    • User can rate the product and it will be displayed in homepage and all users using review page


The images of the user interface
![Sign Up page of the smartSQL](https://github.com/cvaram96/smartSQL/blob/master/Resource%20Folder/UserInterfaces/Signup%20page.png)

![Login Up page of the smartSQL](https://github.com/cvaram96/smartSQL/blob/master/Resource%20Folder/UserInterfaces/LoginPage.png)

![Home page of the smartSQL](https://github.com/cvaram96/smartSQL/blob/master/Resource%20Folder/UserInterfaces/HomePage.png)

![New schema added to the page](https://github.com/cvaram96/smartSQL/blob/master/Resource%20Folder/UserInterfaces/upload%20new%20schema%20page.png)
![Added Database query holder page](https://github.com/cvaram96/smartSQL/blob/master/Resource%20Folder/UserInterfaces/database%20page.png)


![Query added database page](https://github.com/cvaram96/smartSQL/blob/master/Resource%20Folder/UserInterfaces/retrive%20query%20page.png)
