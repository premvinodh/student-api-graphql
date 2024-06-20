import unittest

from src.schema import schema


class TestDeleteStudent(unittest.TestCase):

    def setUp(self):
        self.delete_student_by_id = """
            mutation {
                deleteStudent(studentId: 1) {
                    success
                }
            }
        """

        self.delete_non_existent_student_by_id = """
            mutation {
                deleteStudent(studentId: 4) {
                    success
                }
            }
        """

    def test_mutation_delete_existing_student_by_id(self):
        result = schema.execute(self.delete_student_by_id)
        assert not result.errors
        # print(f"Yes : {result.data}")
        assert result.data == {'deleteStudent': {'success': True}}

    def test_mutation_delete_non_existing_student_by_id(self):
        result = schema.execute(self.delete_non_existent_student_by_id)
        assert result.errors
        # print(f"Yes : {result.errors[0].message}")
        assert "result.errors[0].message == Student 4 not found"
