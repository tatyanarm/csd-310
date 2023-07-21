-- Tatyana Romanova 
-- 07/20/2023
-- 8.2 Module / 3.MySQL Instruction


-- drop test user if exits
drop USER if exists 'pysports_user'@'localhost';

-- create pysports_user and grant them all privileges to the pysports database
create USER 'pysports_user'@'localhost' IDENTIFIED with mysql_native_password by 'MySQLpassword!!';

-- grant all privileges to the pysports database to user pysports_user on localhost
grant ALL PRIVILEGES on pysports.* to'pysports_user'@'localhost';

-- drop tables if they are present
drop table if exists player;
drop table if exists team;



-- create the team table
create table team (
    team_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    team_name varchar(75) NOT NULL,
    mascot varchar(75) NOT NULL, 
);

-- create the player table and set the foreign key
create table player (
    player_id   int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name          varchar(75) NOT NULL,
    last_name           varchar(75) NOT NULL,
    team_id             int  NOT NULL,
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
            REFERENCES team(team_id)
);




-- insert team records
INSERT INTO team (team_name, mascot)
    VALUES('Team Sauron', 'White Hand');

INSERT INTO team (team_name, mascot)
    VALUES('Team Gandalf', 'Eagle');

-- insert player records
INSERT INTO player (first_name, last_name, team_id)
    VALUES('Mannish', 'The White', (select team_id from team where team_name = 'Team Sauron'));

INSERT INTO player (first_name, last_name, team_id)
    VALUES('Angmar', 'Witch-King', (select team_id from team where team_name = 'Team Sauron'));

INSERT INTO player (first_name, last_name, team_id)
    VALUES('Azog', 'The Defiler', (select team_id from team where team_name = 'Team Sauron'));

INSERT INTO player (first_name, last_name, team_id)
    VALUES('Thorin', 'OakenShield', (select team_id from team where team_name = 'Team Gandalf'));

INSERT INTO player (first_name, last_name, team_id)
    VALUES('Bilbo', 'Baggins', (select team_id from team where team_name = 'Team Gandalf'));

INSERT INTO player (first_name, last_name, team_id)
    VALUES('Frodo', 'Baggins', (select team_id from team where team_name = 'Team Gandalf'));