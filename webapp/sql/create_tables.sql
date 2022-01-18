START TRANSACTION;

-- Use (swtich to) webapp_db 
USE webapp_db;

-- Drop the Persons table if it exists
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Mini_Collection;
DROP TABLE IF EXISTS Game_System;
DROP TABLE IF EXISTS Credentials;


-- Create the Credentias table and set the uniqe auto_incrementing ID
CREATE TABLE Credentials (
    credId int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    userpwd varchar(255) NOT NULL,

    PRIMARY KEY (credId)
);

-- Create the Persons table and set the uniqe auto_incrementing ID - this gives further personalisation options to the user account - TBD if being used on first release. 
CREATE TABLE Persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    email varchar(255) NOT NULL,
    credId int NOT NULL,

    PRIMARY KEY (PersonID)
--    FOREIGN KEY (credId) REFERENCES Credentials(credId)                   Come back to f_keys later when I work out how to make them work right. 
);

-- Create the Game_System table and set the uniqe auto_incrementing ID - May pull this later - But nice to have DB and relationships here now. 
CREATE TABLE Game_System (
    SystemID int NOT NULL AUTO_INCREMENT,
    Company VARCHAR(255) NOT NULL,
    Game_System VARCHAR(255) NOT NULL,
    Game_Faction VARCHAR(255) NOT NULL,
    Project_Name VARCHAR(255) NOT NULL,
    credId int NOT NULL,

    PRIMARY KEY (SystemID)
--    FOREIGN KEY (credId) REFERENCES Credentials(credId)                   Come back to f_keys later when I work out how to make them work right. 

);

-- Create the Collection table and set the uniqe auto_incrementing ID - This gives absolute 'core' level functions, in that we can add or remove items to a collection
CREATE TABLE Mini_Collection (
    MiniID int NOT NULL AUTO_INCREMENT,
    MiniName VARCHAR(255) NOT NULL,
    MiniType VARCHAR(255) NOT NULL,
    MiniNum int NOT NULL,
    MiniPoint int,
    MiniCost int,
    credId int NOT NULL,
    SystemID int NOT NULL,

    PRIMARY KEY (MiniID)
--    FOREIGN KEY (credId) REFERENCES Credentials(credId),                      Come back to f_keys later when I work out how to make them work right. 
--    FOREIGN KEY (SystemID) REFERENCES Game_System(SystemID)                   Come back to f_keys later when I work out how to make them work right. 

);


-- The below is for future expansion as the project develops. See Project Outlines

-- Create Paint_Progress table and set the Unique Auto_incrementing ID - NB - Need to investigate best approach before implementing - checkbox/drop down etc?
-- CREATE TABLE Paint_Progress (
   -- PaintID
   -- OnSprue
   -- Assembled
   -- Undercoat
   -- Tabletop
   -- Complete
   -- Images

   -- PRIMARY KEY (PaintID)
   -- FOREIGN KEY (CollectionID) REFERENCES Collection_List(CollectionID)

-- );

-- Create 40K_Stat table and set the Unique Auto_incrementing ID - NB - Need to investigate best approach before implementing - checkbox/drop down etc?
-- CREATE TABLE 40K_Stat (
   -- StatID
   -- Desc
   -- Options
   -- Move
   -- Wep_Skill
   -- Bal_Skill
   -- Strength
   -- Tough
   -- Wound
   -- Attack
   -- Lead
   -- Save
   -- Wargear
   -- Abilities
   -- Keywords
   -- Type

   -- PRIMARY KEY (StatID)
   -- FOREIGN KEY (CollectionID) REFERENCES Collection_List(CollectionID)

-- );

-- Create 40KGear table and set the Unique Auto_incrementing ID - NB - Need to investigate best approach before implementing - checkbox/drop down etc?
-- CREATE TABLE 40KGear (
   -- GearID
   -- Name
   -- Desc
   -- Type
   -- Strength
   -- ArmourPen
   -- Damage

   -- PRIMARY KEY (GearID)
   -- FOREIGN KEY (StatID) REFERENCES 40K_Stat(StatID)

-- );