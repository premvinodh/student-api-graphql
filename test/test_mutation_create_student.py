import unittest

from src.schema import schema


class TestCreateStudent(unittest.TestCase):

    def setUp(self):
        self.create_student = """
            mutation {
                 createStudent(age: 17, name: "Donald Duck") {
                    student {
                         studentId,
                         name,
                         age
                     }
                 }
             }
        """

    def test_mutation_create_student(self):
        result = schema.execute(self.create_student)
        assert not result.errors
        # print(f"Yes : {result.data}")
        assert result.data == {'createStudent': {'student': {'studentId': '3', 'name': 'Donald Duck', 'age': 17}}}
