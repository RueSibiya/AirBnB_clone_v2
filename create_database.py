#!/usr/bin/env python3

import unittest
import MySQLdb

class TestMySQLDatabase(unittest.TestCase):
    def setUp(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="kathy2470",
            passwd="kathylenemukisa",
            db="hbtn_Oe_testing"
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.db.close()

    def test_create_record(self):
        initial_count = self.get_record_count()
        final_count = self.get_record_count()

        self.assertEqual(final_count - initial_count, 1)

    def get_record_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

if __name__ == '__main__':
    unittest.main()
