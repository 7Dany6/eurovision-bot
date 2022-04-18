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
            return self.cursor.execute("INSERT INTO `scoreboard` VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)", (id, )).fetchall()

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

    def give_ukraine_12_points(self, id):
        """
        Gives 12 points to Ukraine
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Ukraine` = `Ukraine` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_netherlands_12_points(self, id):
        """
        Gives 12 points to the Netherlands
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `The Netherlands` = `The Netherlands` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_greece_12_points(self, id):
        """
        Gives 12 points to Greece
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Greece` = `Greece` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_albania_12_points(self, id):
        """
        Gives 12 points to Albania
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Albania` = `Albania` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_armenia_12_points(self, id):
        """
        Gives 12 points to Armenia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Armenia` = `Armenia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_moldova_12_points(self, id):
        """
        Gives 12 points to Moldova
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Moldova` = `Moldova` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_portugal_12_points(self, id):
        """
        Gives 12 points to Portugal
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Portugal` = `Portugal` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_swiss_12_points(self, id):
        """
        Gives 12 points to Switzerland
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Switzerland` = `Switzerland` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_austria_12_points(self, id):
        """
        Gives 12 points to Austria
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Austria` = `Austria` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_lithuania_12_points(self, id):
        """
        Gives 12 points to Lithuania
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Lithuania` = `Lithuania` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_latvia_12_points(self, id):
        """
        Gives 12 points to Latvia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Latvia` = `Latvia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_croatia_12_points(self, id):
        """
        Gives 12 points to Croatia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Croatia` = `Croatia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_iceland_12_points(self, id):
        """
        Gives 12 points to Iceland
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Iceland` = `Iceland` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_slovenia_12_points(self, id):
        """
        Gives 12 points to Slovenia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Slovenia` = `Slovenia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_denmark_12_points(self, id):
        """
        Gives 12 points to Denmark
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Denmark` = `Denmark` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_bulgaria_12_points(self, id):
        """
        Gives 12 points to Bulgaria
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Bulgaria` = `Bulgaria` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_sweden_12_points(self, id):
        """
        Gives 12 points to Sweden
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Sweden` = `Sweden` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_poland_12_points(self, id):
        """
        Gives 12 points to Poland
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Poland` = `Poland` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_estonia_12_points(self, id):
        """
        Gives 12 points to Estonia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Estonia` = `Estonia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_finland_12_points(self, id):
        """
        Gives 12 points to Finland
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Finland` = `Finland` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_azerbaijan_12_points(self, id):
        """
        Gives 12 points to Azerbaijan
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Azerbaijan` = `Azerbaijan` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_australia_12_points(self, id):
        """
        Gives 12 points to Australia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Australia` = `Australia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_serbia_12_points(self, id):
        """
        Gives 12 points to Serbia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Serbia` = `Serbia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_belgium_12_points(self, id):
        """
        Gives 12 points to Belgium
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Belgium` = `Belgium` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_czech_12_points(self, id):
        """
        Gives 12 points to Czech Republic
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Czech Republic` = `Czech Republic` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_cyprus_12_points(self, id):
        """
        Gives 12 points to Cyprus
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Cyprus` = `Cyprus` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_malta_12_points(self, id):
        """
        Gives 12 points to Malta
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Malta` = `Malta` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_romania_12_points(self, id):
        """
        Gives 12 points to Romania
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Romania` = `Romania` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_marino_12_points(self, id):
        """
        Gives 12 points to San Marino
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `San Marino` = `San Marino` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_montenegro_12_points(self, id):
        """
        Gives 12 points to Montenegro
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Montenegro` = `Montenegro` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_israel_12_points(self, id):
        """
        Gives 12 points to Israel
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Israel` = `Israel` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_macedonia_12_points(self, id):
        """
        Gives 12 points to North Macedonia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `North Macedonia` = `North Macedonia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_ireland_12_points(self, id):
        """
        Gives 12 points to Ireland
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Ireland` = `Ireland` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_georgia_12_points(self, id):
        """
        Gives 12 points to Georgia
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Georgia` = `Georgia` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_italy_12_points(self, id):
        """
        Gives 12 points to Italy
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Italy` = `Italy` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_uk_12_points(self, id):
        """
        Gives 12 points to The UK
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `The UK` = `The UK` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_spain_12_points(self, id):
        """
        Gives 12 points to Spain
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Spain` = `Spain` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_france_12_points(self, id):
        """
        Gives 12 points to France
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `France` = `France` + 12 WHERE `id` = ?", (id,)).fetchall()

    def give_germany_12_points(self, id):
        """
        Gives 12 points to Germany
        """
        with self.connection:
            return self.cursor.execute("UPDATE `scoreboard` SET `Germany` = `Germany` + 12 WHERE `id` = ?", (id,)).fetchall()

