# **README.MD**

## **TOURNAMENT Module**

This readme file describes the steps to using the tournament module. The tournament module creates and maintains the PostgreSQL database that keeps track of players and matches in a swiss-style game tournament. One set of functions within the module will create the database using PostgreSQL. The other set of functions manages and updates the database using Python.

### I. **INSTALLATION**

#### 1. Dependencies

  a. PostgreSQL

The user will need to install PostgreSQL to create and maintain the database.

  b. Python 2.7

The user will use Python to run the commands that manage the database.

  c. psycopg2 Python module

In order to run the module, the user will need to download the Python module psycopg2, available here: https://pypi.python.org/pypi/psycopg2.



### II. **USAGE**
### 1. Running the app:
                
  a. Install the necessary python libraries:
  $ pip install psycopg2                 
  b. Git clone this repository: https://github.com/boo-owner/tournament.git
  
### 2. Create database called tournament:
  a. Start PostgreSQL
  b. Run tournament.sql. This will create the database tournament with three tables, players, player_results, matches.
  
### 3. Test Python file
  To test the files, on the command line, type this command: python tournament_test.py
### 4. Populate Database
  a. use registerPlayer(name_str) function to add player names to the database. This will assign a userid to each player.
  b. Use reportMatch(winner id, loser id) to add match results to the player_results database
  c. use recordMatchinfo(matchno,round,submatchno)to describe the match (which round and submatch number)

### 5. Check Standings
  a. Use playerStandings() to see how players stand after each round.
  
### 6. Assign pairings for next round.
  a. After each round, run swissPairings() to see who will play whom in the next round.
  
#### **2. Files**

**tournament.sql**

This is a PostgreSQL file that creates three tables within your tournament database for tracking tournament results:

players  
player_results  
matches

**tournament.py**

This is a Python file that includes the functions needed to update and maintain the PostgreSQL tournament database. The file contains the following functions:

**connect():** This function connects to the PostgreSQL database and returns a database connection.

**deleteMatches():** This function removes all the match records from the database.

**deletePlayers():** This function removes all the player records from the database.

**countPlayers():** This function returns the number of players currently registered.

**registerPlayer(name\_str):** This function adds a player to the tournament database. The database assigns a unique serial id number for the player.

**playerStandings():** This function returns a list of the players and their win records, sorted by wins.

**reportMatch(winner, loser):** This function records the outcome of a single match between two players.

**reportMatch\_enhanced(winner, loser, matchno):** This function records the outcome of a single match between two players and can be used if the tournament keeps track of match numbers.

**pair(list,start\_val,num\_ints):** This function returns a new list of two consecutive items in a list, starting with index n (list[n]). This function is used in the swissPairings() function.

**swissPairings():** This function returns a list of pairs of players for the next round of a match.

**recordMatchinfo(matchno,round,submatchno):** This function adds match description information to the tournament database.
