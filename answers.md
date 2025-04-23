Reflection Questions

Q1.What were the biggest challenges you faced?

#Data cleaning issues (inconsistency data)
#Creating of API not getting proper output as needed.Had to explicitly cast all values to native Python types
#Creation of dashboard and filters since filters were important part 


Q2.What assumptions did you make about the data?

1.if there are some missing data we have drop it 
2.since the format of date and time was not in correct way converted it and drop invalids
3.convert all data in lowercase 
4.taken only positive transaction

Q3.How would you productionize this project?

1.Code & Architecture
#Refactor code into modular packages
#create logging files for error 
2.Deployment 
#Containerize using Docker for consistent deployment
#deploy on cloud eg: flask api-> aws
3.Data management
#since data was csv file can store in database eg mysql
4.Security
#provide security since the data is of transaction
5.Monitoring & Alerts
#Send email alerts if failure rate exceeds threshold
#monitor quaterly data volummne and plan for improvement.
6.Documentation 
#create a proper document about project and outcome of it 
#Auto-generate API docs and dashboards for business users

Q4.What would you improve if you had more time?

1.Advanced Data Validation
2.Migrate from CSV to a relational database
3. More  API Features
4. Enhanced Dashboard


