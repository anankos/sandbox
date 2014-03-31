import unittest
import datetime

from context import sandbox

class TestSanity(unittest.TestCase):

    def test_new_goal(self):
        created = datetime.datetime.now()
        title = 'test goal'
        goal = sandbox.Goal(title, created = created)

        self.assertEqual(goal.title, title)
        self.assertEqual(goal.created, created)
        self.assertFalse(goal.closed)

    def test_new_item(self):
        created = datetime.datetime.now()
        title = 'test item'
        item = sandbox.Item(title, created = created)

        self.assertEqual(item.title, title)
        self.assertEqual(item.created, created)
        self.assertFalse(item.closed)
