#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """This function connects to the PostgreSQL database and returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """This function removes all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE from player_results")
    c.execute("DELETE from matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """This function removes all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE from players")
    DB.commit()
    DB.close()

def countPlayers():
    """This function returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(*) from players")
    fetchone_output = c.fetchone()
    DB.commit()
    DB.close()
    return fetchone_output[0]


def registerPlayer(name_str):
    """This function adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player. 
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT into players (name) values (%s)", (name_str,))
    DB.commit()
    DB.close()


def playerStandings():
    """This function returns a list of the players and their win records, sorted by wins.

    The first entry in the list is the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()

    c.execute("""
        SELECT p.playerid, p.name, 
        COALESCE(SUM(re.win),0) as wins,
        COALESCE(COUNT(re.match_no),0) tot_matches 
        FROM players p LEFT JOIN player_results re 
        ON p.playerid = re.playerid
        GROUP By p.playerid ORDER by wins DESC
        """)
    result = c.fetchall()
    DB.commit()
    DB.close()
    return result

def reportMatch(winner, loser):
    """This function records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT into player_results values (1,0,(%s))", (winner,))
    c.execute("INSERT into player_results values (0,1,(%s))", (loser,))
    DB.commit()
    DB.close()

def pair(list,start_val,num_ints):
    """
    This function returns a new list of two consecutive items in a list, 
    starting with index n. This function is used in the swissPairings() function.
    
    Inputs: a list and a starting value (n)
    outputs: a new list with two items, list[n:n+1]
    """
    final_list=[]
    pair_iter1 = list[start_val][0:num_ints]
    pair_iter2 = list[start_val+1][0:num_ints]
    final_list = pair_iter1 + pair_iter2
    return final_list

def swissPairings():
    """This function returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    tuple_results = sorted(playerStandings(),key = lambda l: (-l[2], l[3]))
    list_pairs = []
    for pr in range(0,len(tuple_results)-1,2):    
        result=pair(tuple_results,pr,2)
        list_pairs.append(result)
    return list_pairs

"""
There are additional functions I think would enhance the database. These are:
1) Function to assign a unique matchno for each match
and keep match description information (Round, Submatch number)
2) Enhanced reportMatch function that allows for match number to be collected in the
player result record-keeping. 
I did not include these as part of the regular project submission because the 
enhanced reportMatch function (which takes 3 arguments instead of 2)
did not pass the unit tests. 
"""

def recordMatchinfo(matchno,round,submatchno):
    """Adds match description information to the tournament database.
    Args:
      matchno: the unique match number, created in player_results table
      when match results are recorded by reportMatch()
      round: the match round
      submatchno: the number of match played within the round. This number is unique
        within each round.
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT into matches (round,submatch_no) values ((%s),(%s))", (round,submatchno,))
    DB.commit()
    DB.close()

def reportMatch_enhanced(winner, loser, matchno):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT into player_results values (1,0,(%s),(%s))", (winner,matchno,))
    c.execute("INSERT into player_results values (0,1,(%s),(%s))", (loser,matchno,))
    DB.commit()
    DB.close()




