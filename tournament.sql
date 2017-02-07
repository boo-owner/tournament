-- Table definitions for the tournament project.
-- This file creates the tables for the tournament database. The tables are:
-- table: this is a table of players with their id and name.
-- matches: this table contains match information for the matches, with each
--     match described by a round and submatch number.
-- player_results: this table records the results of the matches, 
--     showing id number of the winner or loser, by match number.

create table players (
     playerid serial primary key,
     name text
     );


     
create table player_results (
     win integer CHECK (win = 1 or win = 0), 
     lost integer CHECK (lost = 1 or lost = 0),
     playerid serial references players,
     match_no serial primary key
     );


create table matches (
     match_no serial references player_results,
     round integer,
     submatch_no integer
     );   