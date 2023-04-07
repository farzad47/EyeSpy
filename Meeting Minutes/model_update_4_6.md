# Model Progress Update - 4/6/23
## Updated by:
Alex

## Notes / Comments
- Resolved the classifier issue I was having with facial recognition model
- Did some research into grabbing images from databases using Python
  - SQL to Python conversion can be done with mysql.connector library
  - I attempted to search AWS to Python conversion and found some library called boto3 that we can look into
  - Either way, it appears that the workflow is to use the library to connect to the database, then you have to execute a query on the database. This will return results in rows (from the resultant table).
  - We can parse through the results of the given query to find the images of the authorized individuals to use in our model
  - I believe the images are stored as blob data type which can be converted to png using a convert_data(blob, "image.png") function ~in mysql.connector library~

## Action Items
- Meeting with team tomorrow 4/7/23 @ 11:00 AM in Boffin Lab on campus
- Discuss these different methods and attempt to connect the model to the backend with the team
- We also need to connect the other parts of the project into the whole product
- Implement the distributed computing aspect
- Create the presentation