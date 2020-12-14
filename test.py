import computing_final_project as f
import unittest

class TestRoster(unittest.TestCase):
    weeks = 4

    title = 'Exec'
    effort = 50
    wage = 45

    title2 = 'Employee'
    effort2 = 100
    wage2 = 21

    def test_create_person(self):
        """
        Test whether person gets created
        """
        title= 'Exec'
        wage = 10
        effort = 100
        person = f.Person(title, wage, effort)
        self.assertIsNotNone(person)
