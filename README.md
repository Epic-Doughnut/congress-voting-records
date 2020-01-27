# congress-voting-records
A script to access public voting records of US Senators and Representatives

In order to use the script, you must replaced the string "REPLACE_WITH_YOUR_KEY" with your ProPublica API key, found here: https://www.propublica.org/datastore/api/propublica-congress-api

You can replace the list 'accessing' with whichever Congress you want, as outlined here: https://projects.propublica.org/api-docs/congress-api/endpoints/#lists-of-members
(102-116 for House, 80-116 for Senate)

The contents of those votes will be saved to a file in the format ###\_senate.csv or ###\_house.csv in the same directory as the .py script
