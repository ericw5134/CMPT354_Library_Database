import sqlite3

def connect_db():
    return sqlite3.connect('library.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Create Item table
    cursor.execute('''
    CREATE TABLE Item (
        itemID INTEGER NOT NULL,
        itemType VARCHAR(30),
        title VARCHAR(30),
        author VARCHAR(30),
        publisher VARCHAR(30),
        releaseDate DATE CHECK ( releaseDate NOT NULL ),
        PRIMARY KEY (itemID),
        CHECK ( itemType IN ('Print Book', 'Online Book', 'Magazine', 'Scientific Journal', 'CD', 'Record') )
    )
    ''')

    # Create Person table
    cursor.execute('''
    CREATE TABLE Person (
        personID INTEGER NOT NULL,
        firstName VARCHAR(20),
        lastName VARCHAR(20),
        contactNumber VARCHAR(20) UNIQUE,
        email VARCHAR(30),
        PRIMARY KEY (personID)
    )
    ''')

    # Create BorrowTransaction table
    cursor.execute('''
        CREATE TABLE BorrowTransaction (
        transactionID INTEGER NOT NULL,
        itemID INTEGER,
        personID INTEGER,
        borrowDate DATE,
        returnDate DATE,
        fineAmount INTEGER,
        PRIMARY KEY (transactionID),
        FOREIGN KEY(itemID) REFERENCES Item(itemID),
        FOREIGN KEY(personID) REFERENCES Person(personID)
        CHECK (borrowDate NOT NULL)
    )
    ''')

    # Create Event table
    cursor.execute('''
    CREATE TABLE Event (
        eventID INTEGER NOT NULL,
        eventType VARCHAR(20),
        eventPrice INTEGER CHECK (eventPrice >= 0),
        socialRoom VARCHAR(20),
        PRIMARY KEY (eventID)
    )
    ''')

    # Create eventAudiences table
    cursor.execute('''
    CREATE TABLE eventAudiences (
        eventID INTEGER NOT NULL,
        audienceID INTEGER,
        FOREIGN KEY(audienceID) REFERENCES Person(PersonID),
        FOREIGN KEY(eventID) REFERENCES Event(eventID),
        PRIMARY KEY (eventID, audienceID)
    )
    ''')

    # Create Personnel table
    cursor.execute('''
    CREATE TABLE Personnel (
        personnelID INTEGER,
        jobTitle VARCHAR(20),
        PRIMARY KEY (personnelID),
        FOREIGN KEY(personnelID) REFERENCES Person(personID)
    )
    ''')

    # Create FutureItem table
    cursor.execute('''
    CREATE TABLE FutureItem (
        futureItemID INTEGER NOT NULL,
        PRIMARY KEY (futureItemID),
        FOREIGN KEY(futureItemID) REFERENCES Item(itemID)
    )
    ''')

    cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS SetReturnDate
        AFTER INSERT ON BorrowTransaction
        FOR EACH ROW
        BEGIN
            UPDATE BorrowTransaction
            SET returnDate = DATE(borrowDate, '+1 month')
            WHERE transactionID = NEW.transactionID;
        END;
    ''')

    cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS SetFineAmount
        AFTER INSERT ON BorrowTransaction
        FOR EACH ROW
        BEGIN
            UPDATE BorrowTransaction
            SET fineAmount = 26
            WHERE transactionID = NEW.transactionID;
        END;
    ''')

    conn.commit()
    conn.close()

def insert_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Insert example tuples into Item table
    cursor.executemany('''
    INSERT INTO Item VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Print Book', 'Sample Book 1', 'John Doe', 'Publisher A', '2023-01-01'),
        (2, 'Online Book', 'Sample Book 2', 'Jane Smith', 'Publisher B', '2023-02-15'),
        (3, 'Magazine', 'Sample Magazine 1', 'Magazine Author', 'Publisher C', '2023-03-10'),
        (4, 'Scientific Journal', 'Sample Journal 1', 'Researcher X', 'Publisher D', '2023-04-20'),
        (5, 'CD', 'Sample CD 1', 'Artist A', 'Music Label E', '2023-05-05'),
        (6, 'Record', 'Sample Record 1', 'Artist B', 'Music Label F', '2023-06-30'),
        (7, 'Print Book', 'Sample Book 3', 'Author Y', 'Publisher G', '2023-07-12'),
        (8, 'Online Book', 'Sample Book 4', 'Author Z', 'Publisher H', '2023-08-25'),
        (9, 'CD', 'Sample CD 2', 'Artist C', 'Music Label I', '2023-09-18'),
        (10, 'Magazine', 'Sample Magazine 2', 'Magazine Author 2', 'Publisher J', '2023-10-05'),
        (11, 'Print Book', 'Sample Book 5', 'Author X', 'Publisher K', '2023-11-15'),
        (12, 'Online Book', 'Sample Book 6', 'Author Y', 'Publisher L', '2023-12-20'),
        (13, 'CD', 'Sample CD 3', 'Artist B', 'Music Label F', '2024-01-10'),
        (14, 'Magazine', 'Sample Magazine 3', 'Magazine Author 3', 'Publisher M', '2024-02-05'),
        (15, 'Record', 'Sample Record 2', 'Artist C', 'Music Label I', '2024-03-25'),
        (16, 'Print Book', 'Sample Book 7', 'Author Z', 'Publisher N', '2024-04-12'),
        (17, 'Online Book', 'Sample Book 8', 'Author X', 'Publisher K', '2024-05-30'),
        (18, 'CD', 'Sample CD 4', 'Artist A', 'Music Label E', '2024-06-18'),
        (19, 'Magazine', 'Sample Magazine 4', 'Magazine Author 4', 'Publisher O', '2024-07-08'),
        (20, 'Record', 'Sample Record 3', 'Artist B', 'Music Label F', '2024-08-15'),
        (21, 'Print Book', 'Sample Book 9', 'Author Y', 'Publisher L', '2024-09-20'),
        (22, 'Online Book', 'Sample Book 10', 'Author Z', 'Publisher N', '2024-10-05'),
        (23, 'CD', 'Sample CD 5', 'Artist C', 'Music Label I', '2024-11-15'),
        (24, 'Magazine', 'Sample Magazine 5', 'Magazine Author 5', 'Publisher O', '2024-12-02'),
        (25, 'Record', 'Sample Record 4', 'Artist A', 'Music Label E', '2025-01-08'),
        (26, 'Print Book', 'Sample Book 11', 'Author X', 'Publisher K', '2025-02-18'),
        (27, 'Online Book', 'Sample Book 12', 'Author Y', 'Publisher L', '2025-03-25'),
        (28, 'CD', 'Sample CD 6', 'Artist B', 'Music Label F', '2025-04-12'),
        (29, 'Magazine', 'Sample Magazine 6', 'Magazine Author 6', 'Publisher M', '2025-05-22'),
        (30, 'Record', 'Sample Record 5', 'Artist C', 'Music Label I', '2025-06-05'),
        (31, 'Print Book', 'Sample Book 13', 'Author Z', 'Publisher N', '2025-07-10'),
        (32, 'Online Book', 'Sample Book 14', 'Author X', 'Publisher K', '2025-08-15'),
        (33, 'CD', 'Sample CD 7', 'Artist A', 'Music Label E', '2025-09-18'),
        (34, 'Magazine', 'Sample Magazine 7', 'Magazine Author 7', 'Publisher O', '2025-10-25'),
        (35, 'Record', 'Sample Record 6', 'Artist B', 'Music Label F', '2025-11-30'),
        (36, 'Print Book', 'Sample Book 15', 'Author Y', 'Publisher L', '2025-12-15'),
        (37, 'Online Book', 'Sample Book 16', 'Author Z', 'Publisher N', '2026-01-22'),
        (38, 'CD', 'Sample CD 8', 'Artist C', 'Music Label I', '2026-02-08'),
        (39, 'Magazine', 'Sample Magazine 8', 'Magazine Author 8', 'Publisher M', '2026-03-12'),
        (40, 'Record', 'Sample Record 7', 'Artist A', 'Music Label E', '2026-04-18')
    ])

    # Insert example tuples into Person table
    cursor.executemany('''
    INSERT INTO Person VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, 'John', 'Doe', '545-109-1896', 'john.doe@example.com'),
        (2, 'Jane', 'Smith', '256-744-2185', 'jane.smith@example.com'),
        (3, 'Alice', 'Johnson', '823-168-9374', 'alice.johnson@example.com'),
        (4, 'Bob', 'Anderson', '780-537-4179', 'bob.anderson@example.com'),
        (5, 'David', 'Williams', '621-936-6840', 'david.williams@example.com'),
        (6, 'Emily', 'Brown', '879-045-9671', 'emily.brown@example.com'),
        (7, 'Michael', 'Jones', '354-512-0802', 'michael.jones@example.com'),
        (8, 'Olivia', 'Davis', '434-995-1321', 'olivia.davis@example.com'),
        (9, 'Sophia', 'Miller', '013-850-7696', 'sophia.miller@example.com'),
        (10, 'William', 'Wilson', '516-358-3485', 'william.wilson@example.com'),
        (11, 'James', 'Brown', '925-603-6759', 'james.brown@example.com'),
        (12, 'Emma', 'Clark', '357-932-5631', 'emma.clark@example.com'),
        (13, 'Liam', 'Martinez', '259-684-2010', 'liam.martinez@example.com'),
        (14, 'Ava', 'Thompson', '851-168-3657', 'ava.thompson@example.com'),
        (15, 'Noah', 'Wright', '905-181-7086', 'noah.wright@example.com'),
        (16, 'Isabella', 'Lee', '326-539-3842', 'isabella.lee@example.com'),
        (17, 'Ethan', 'Scott', '384-049-7120', 'ethan.scott@example.com'),
        (18, 'Mia', 'Lopez', '990-870-3281', 'mia.lopez@example.com'),
        (19, 'Lucas', 'Hill', '721-468-5739', 'lucas.hill@example.com'),
        (20, 'Avery', 'Green', '841-502-7636', 'avery.green@example.com')
    ])

    # Insert example tuples into BorrowTransaction table
    cursor.executemany('''
    INSERT INTO BorrowTransaction VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        (1, 1, 1, '2023-07-01', None, None),
        (2, 2, 3, '2023-07-10', None, None),
        (3, 5, 2, '2023-07-15', None, None),
        (4, 3, 4, '2023-07-20', None, None),
        (5, 6, 6, '2023-07-25', None, None),
        (6, 4, 7, '2023-07-30', None, None),
        (7, 9, 5, '2023-08-01', None, None),
        (8, 10, 8, '2023-08-05', None, None),
        (9, 7, 9, '2023-08-10', None, None),
        (10, 8, 10, '2023-08-15', None, None)
    ])

    # Insert example tuples into Event table
    cursor.executemany('''
    INSERT INTO Event VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Story Telling Session', 0, 'Hall A'),
        (2, 'Elementry Math Seminar', 0, 'Hall C'),
        (3, 'Indigenous Culture Learning Day', 0, 'Hall A'),
        (4, 'College Calculus Workshop', 0, 'Hall C'),
        (5, 'High School Chemistry Tutoring', 0, 'Hall c'),
        (6, 'High School Physics Tutoring', 0, 'Hall C'),
        (7, 'Monthly Employee Meeting', 0, 'Hall F'),
        (8, 'Woodworking Workshop', 0, 'Hall C'),
        (9, 'Drawing Competition', 0, 'Hall G'),
        (10, 'Poetry Competition', 0, 'Hall G')
    ])

    # Insert example tuples into eventAudiences table
    cursor.executemany('''
    INSERT INTO eventAudiences VALUES (?, ?)
    ''', [
        (1, 11),
        (1, 12),
        (1, 13),
        (1, 14),
        (1, 15),
        (1, 16),
        (1, 17),
        (1, 18),
        (1, 19),
        (2, 20)
    ])

    # Insert example tuples into Personnel table
    cursor.executemany('''
    INSERT INTO Personnel VALUES (?, ?)
    ''', [
        (1, 'Manager'),
        (2, 'Assistant'),
        (3, 'Coordinator'),
        (4, 'Technician'),
        (5, 'Intern'),
        (6, 'Manager'),
        (7, 'Assistant'),
        (8, 'Coordinator'),
        (9, 'Technician'),
        (10, 'Intern')
    ])

    # Insert example tuples into FutureItem table
    cursor.executemany('''
    INSERT INTO FutureItem VALUES (?)
    ''', [
        (1,),
        (2,),
        (5,),
        (3,),
        (6,),
        (4,),
        (9,),
        (10,),
        (7,),
        (8,)
    ])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_data()
