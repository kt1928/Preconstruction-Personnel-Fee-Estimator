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

    def test_calc_hours(self):
        """
        Tests whether the hours are calculated properly
        """
        wage = 45

        person = f.Person(self.title, wage, self.effort)
        self.assertEqual(person.calc_hours(self.weeks, self.effort), 80)

        person2 = f.Person(self.title2, wage, self.effort2)
        self.assertEqual(person2.calc_hours(self.weeks, self.effort2), 160)

    def test_calc_pay(self):
        """
        Tests whether pay is calculated properly
        """

        person = f.Person(self.title, self.wage, self.effort)
        self.assertEqual(person.calc_pay(self.wage, self.weeks, self.effort), 3600)

        person2 = f.Person(self.title2, self.wage2, self.effort2)
        self.assertEqual(person2.calc_pay(self.wage2, self.weeks, self.effort2), 3360)
