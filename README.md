## Issues:

12/26/2017: The site has an index url (home) with a form that sends a get request with the gene symbol to Django. I've gotten Django configured to properly query the database and create a url that takes the query data and returns a JSON response suitable to be parsed by the D3 parser. I can't get the graph to load though. The svg element gets created, and there are no errors in the JavaScript console, so I am very confused.
