-- Tatyana Romanova 
-- 08/04/2023
-- 10.3 Module / Assignment: WhatABook: Database and Table Creation


-- Create Role - due update on MySQL Role is prefered and preventing to trow unknown error due difrance from MySQL 5.6 and Lover from MySQL 8.0 And above  
-- Drop Role if exist 
DROP ROLE IF EXISTS 'Admin';  
-- Create Role 
CREATE ROLE 'Admin';
-- Grant ALL Role on whatabook 
GRANT ALL ON whatabook.* to 'Admin';


-- DROP USER IF EXISTS 'whatabook_user'@localhost;
DROP USER IF EXISTS 'whatabook_user'@localhost;
-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost'
  IDENTIFIED BY 'MySQL8IsGreat!';
  -- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL
  ON whatabook.*
  TO 'whatabook_user'@'localhost' 
  WITH GRANT OPTION;

-- drop tables if they exist
USE whatabook;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;


--   Create Table(s)~

USE whatabook;
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
     REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
     REFERENCES user(user_Id)
);


--    Insert Wishlist Records~ 

INSERT INTO book(book_name, author, details)
    VALUES("The Hobit", "J.R.Tolkien", "First book in Order");

INSERT INTO book(book_name, author, details)
    VALUES("The Fellowship of the Ring", "J.R.Tolkien", "The Second book in Order");

INSERT INTO book(book_name, author, details)
    VALUES("The Silmarillion", "J.R.Tolkien", "The third book in Order");

INSERT INTO book(book_name, author)
    VALUES("King Kong", "Delos W. Lovelace");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Sorcerer's Stone", "Joanne Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Prisoner of Azkaban", "Joanne Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Deathly Hallows", "Joanne Rowling");

INSERT INTO book(book_name, author)
    VALUES("A Clash of Kings", "George R. R. Martin");

INSERT INTO book(book_name, author)
    VALUES("Young Sherlock Holmes", "Andrew Lane");



--    Insert User~
INSERT INTO user(first_name, last_name) 
    VALUES("Peter", "Jackson");
-- Peter Jackson Directed Lord of the rings and King kong 4
INSERT INTO user(first_name, last_name)
    VALUES("Chris", "Columbus");
-- Chris Columbus Directed Harry Potter and Young Sherlock Holmes
INSERT INTO user(first_name, last_name)
    VALUES("Sean", "Bean");
-- Acting in Lotr and Game of thrones

-- insert Store recod location
-- Added location from Peer review 
INSERT INTO store(locale)
    VALUES("828 Broadway, New York, NY 10003")    

-- insert wishlist records~ 

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Peter"), 
        (SELECT book_id FROM book WHERE book_name = "The Fellowship of the Ring")
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Chris"),
        (SELECT book_id FROM book WHERE book_name = "Harry Potter and the Prisoner of Azkaban")
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = "Sean"),
        (SELECT book_id FROM book WHERE book_name = "A Clash of Kings")
    );
