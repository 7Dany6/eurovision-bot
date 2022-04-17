import sqlite3

class SQL:
    def __init__(self, database_file):
        """
        Connecting to the database
        """
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, id):
        """
        Searching a given person in the database
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `id` = ?", (id,)).fetchall()
        return bool(len(result))

    def register(self, id):
        """
        Appending a user into `users` table
        """
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` VALUES (?)", (id,))

    def insert_voter(self, id):
        """
        Add a voter into table `scoreboard`
        """
        with self.connection:
            return self.cursor.execute("INSERT INTO `scoreboard` VALUES (?, 0)", (id, )).fetchall()

    def voter_exists(self, id):
        """
        Searching a given voter in the database
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `scoreboard` WHERE `id` = ?", (id,)).fetchall()
        return bool(len(result))

    def remove_vote(self, id):
        """
        Conceals votes from a person
        """
        with self.connection:
            self.cursor.execute("DELETE FROM `scoreboard` WHERE `id` = ?", (id,)).fetchall()

    def give_norway_12_points(self, id):
        """
        Gives 12 points to Norway
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Norway` = `Norway` + 12 WHERE `id` = ?", (id,)).fetchall()