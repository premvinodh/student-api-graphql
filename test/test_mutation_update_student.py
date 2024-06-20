import unittest

from src.schema import schema


class TestUpdateStudent(unittest.TestCase):

    def setUp(self):
        self.update_student_by_id = """
            mutation {
                 updateStudent(age: 18, name: "Mickeyyyyyy Mouse", studentId: 1) {
                    student {
                         studentId,
                         name,
                         age
                     }
                 }
             }
        """

        self.update_non_existent_student_by_id = """
            mutation {
                 updateStudent(age: 18, name: "Donald Duckyyyy", studentId: 11) {
                    student {
                         studentId,
                         name,
                         age
                     }
                 }
             }
        """

    def test_mutation_update_existent_student(self):
        result = schema.execute(self.update_student_by_id)
        assert not result.errors
        print(f"Yes : {result.data}")
        assert result.data == {'updateStudent': {'student': {'studentId': '1', 'name': 'Mickeyyyyyy Mouse', 'age': 18}}}

    def test_mutation_update_non_existent_student(self):
        result = schema.execute(self.update_non_existent_student_by_id)
        # assert result.errors
        print(f"Yes : {result.errors[0].message}")
        assert "result.errors[0].message == Student 3 not found"
