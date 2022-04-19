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

    def count_norway(self):
        """
        Counts points of Norway
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Norway`) FROM `scoreboard`").fetchall()

    def count_ukraine(self):
        """
        Counts points of Ukraine
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Ukraine`) FROM `scoreboard`").fetchall()

    def count_netherlands(self):
        """
        Counts points of the Netherlands
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`The Netherlands`) FROM `scoreboard`").fetchall()

    def count_greece(self):
        """
        Counts points of Greece
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Greece`) FROM `scoreboard`").fetchall()

    def count_albania(self):
        """
        Counts points of Albania
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Albania`) FROM `scoreboard`").fetchall()

    def count_armenia(self):
        """
        Counts points of Armenia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Armenia`) FROM `scoreboard`").fetchall()

    def count_moldova(self):
        """
        Counts points of Moldova
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Moldova`) FROM `scoreboard`").fetchall()

    def count_portugal(self):
        """
        Counts points of Portugal
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Portugal`) FROM `scoreboard`").fetchall()

    def count_swiss(self):
        """
        Counts points of Switzerland
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Switzerland`) FROM `scoreboard`").fetchall()

    def count_austria(self):
        """
        Counts points of Austria
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Austria`) FROM `scoreboard`").fetchall()

    def count_lithuania(self):
        """
        Counts points of Lithuania
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Lithuania`) FROM `scoreboard`").fetchall()

    def count_latvia(self):
        """
        Counts points of Latvia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Latvia`) FROM `scoreboard`").fetchall()

    def count_croatia(self):
        """
        Counts points of Croatia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Croatia`) FROM `scoreboard`").fetchall()

    def count_iceland(self):
        """
        Counts points of Iceland
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Iceland`) FROM `scoreboard`").fetchall()

    def count_slovenia(self):
        """
        Counts points of Slovenia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Slovenia`) FROM `scoreboard`").fetchall()

    def count_denmark(self):
        """
        Counts points of Denmark
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Denmark`) FROM `scoreboard`").fetchall()

    def count_bulgaria(self):
        """
        Counts points of Bulgaria
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Bulgaria`) FROM `scoreboard`").fetchall()

    def count_sweden(self):
        """
        Counts points of Sweden
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Sweden`) FROM `scoreboard`").fetchall()

    def count_poland(self):
        """
        Counts points of Poland
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Poland`) FROM `scoreboard`").fetchall()

    def count_estonia(self):
        """
        Counts points of Estonia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Estonia`) FROM `scoreboard`").fetchall()

    def count_finland(self):
        """
        Counts points of Finland
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Finland`) FROM `scoreboard`").fetchall()

    def count_azerbaijan(self):
        """
        Counts points of Azerbaijan
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Azerbaijan`) FROM `scoreboard`").fetchall()

    def count_australia(self):
        """
        Counts points of Australia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Australia`) FROM `scoreboard`").fetchall()

    def count_serbia(self):
        """
        Counts points of Serbia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Serbia`) FROM `scoreboard`").fetchall()

    def count_belgium(self):
        """
        Counts points of Belgium
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Belgium`) FROM `scoreboard`").fetchall()

    def count_czech(self):
        """
        Counts points of Czech Republic
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Czech Republic`) FROM `scoreboard`").fetchall()

    def count_cyprus(self):
        """
        Counts points of Cyprus
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Cyprus`) FROM `scoreboard`").fetchall()

    def count_malta(self):
        """
        Counts points of Malta
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Malta`) FROM `scoreboard`").fetchall()

    def count_romania(self):
        """
        Counts points of Romania
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Romania`) FROM `scoreboard`").fetchall()

    def count_marino(self):
        """
        Counts points of San Marino
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`San Marino`) FROM `scoreboard`").fetchall()

    def count_montenegro(self):
        """
        Counts points of Montenegro
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Montenegro`) FROM `scoreboard`").fetchall()

    def count_israel(self):
        """
        Counts points of Israel
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Israel`) FROM `scoreboard`").fetchall()

    def count_macedonia(self):
        """
        Counts points of North Macedonia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`North Macedonia`) FROM `scoreboard`").fetchall()

    def count_ireland(self):
        """
        Counts points of Ireland
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Ireland`) FROM `scoreboard`").fetchall()

    def count_georgia(self):
        """
        Counts points of Georgia
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Georgia`) FROM `scoreboard`").fetchall()

    def count_italy(self):
        """
        Counts points of Italy
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Italy`) FROM `scoreboard`").fetchall()

    def count_uk(self):
        """
        Counts points of the UK
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`The UK`) FROM `scoreboard`").fetchall()

    def count_spain(self):
        """
        Counts points of Spain
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Spain`) FROM `scoreboard`").fetchall()

    def count_france(self):
        """
        Counts points of France
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`France`) FROM `scoreboard`").fetchall()

    def count_germany(self):
        """
        Counts points of Germany
        """
        with self.connection:
            return self.cursor.execute("SELECT SUM(`Germany`) FROM `scoreboard`").fetchall()

