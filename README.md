# EvohomeTemperatureSite
Log Evohome temperature and host graph on own site

- Simple Guide

  - First set up your webserver and create a mysql database.
  - You need to have a column with the name "Time" and default value CURRENT_TIMESTAMP
  - You also need to have a column for each room in your house (it's easy if you name the columns the same like you did for the rooms in the evohome system)
  
  - Then you need to edit 3 files
    - DataLoader.php
      - line 3: correct username, password, name of the database, port,...
      - line 13: correct tablename
    - TemperatureLogging.py
      - line 12: evohome username and password
      - line 14: database information
      - line 22 to ...: fill in correct room names, you can add more rooms if you want (also add them on line 32)
      - line 32: correct room names and table name (rename EvohomeTemperatures to the correct name in your SQL server)
    - index.html
      - line 19: correct http adress for DataLoader.php
      - line 39 to ...: fill in correct room names (title and valueField), also add the rooms here and choose different color (lineColor)
  
  - Last thing you need to do is make a cron job for TemperatureLogging.py that runs every 5 minutes
  


That's it. Have fun!

TIP: You can click on the names in the graph, then you can see the different graphs separately
