## Log:
01/07/2017: The precision issue in the graph in the graph has been fixed by specifying it in \Lib\site-packages\nvd3\discreteBarChart.py. Still need to fix the overlapping x labels. 

My next ideas are to :
- add a table at the index page that allows navigation of the data
- resize the graph on resize of the page. Currently the graph stretches the page if it doesn't fit inside the window. 
- make all elements on the page responsive. 

Alot of this would be made easier if I was more fluent in javascript. I'm really grateful for the django-nvd3 wrapper, but I've been wrangling with it for days trying to do things that should only take a few hours. 
- I will learn to work with d3, and become fluent in javascript. 

12/31/2017: The graph works. Several responsivity issues, and an issue with bar chart scale not showing all decimal places. Next steps are to fix these issues, deploy, and start working on more features, i.e. dashboard view, more visulizations, less redundant database design. 

12/26/2017: The site has an index url (home) with a form that sends a get request with the gene symbol to Django. I've gotten Django configured to properly query the database and create a url that takes the query data and returns a JSON response suitable to be parsed by the D3 parser. I can't get the graph to load though. The svg element gets created, and there are no errors in the JavaScript console, so I am very confused.

## Dependencies:

Before running pip install the following:
- django-bower 
- django-nvd3
- mysqlclient


These may be furthermore dependent on other packages. See requirements.txt. 
