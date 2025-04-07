PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE notes(author TEXT, note TEXT);
INSERT INTO notes VALUES('Duad','Commit suicide.');
INSERT INTO notes VALUES('Hadan','Deez nuts.');
INSERT INTO notes VALUES('Candice','Who is candice.');
INSERT INTO notes VALUES('Andy','Everything is dandy.');
COMMIT;
