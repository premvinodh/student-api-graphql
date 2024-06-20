import unittest

from src.schema import schema


class TestQueryMethods(unittest.TestCase):

    def setUp(self):
        self.query_hello = """
            query {
              hello
            }
        """

        self.query_hello_with_name = """
            query {
              hello(name: "mickey")
            }
        """

        self.query_all_students_all_fields = """
            query {
              students {
                studentId
                name
                age
              }
            }
        """

        self.query_all_students_name_only = """
            query {
              students {
                name
              }
            }
        """

        self.query_all_students_name_age_only = """
            query {
              students {
                name,
                age
              }
            }
        """

        self.query_student_by_id = """
            query {
              student(studentId: 1) {
                studentId
                name
                age
              }
            }
        """

    def test_query_hello(self):
        result = schema.execute(self.query_hello)
        assert not result.errors
        assert result.data == {'hello': 'Hello graphql'}

    def test_query_hello_with_name(self):
        result = schema.execute(self.query_hello_with_name)
        assert not result.errors
        print(f"Yes : {result.data}")
        assert result.data == {'hello': 'Hello mickey'}

    def test_query_students(self):
        result = schema.execute(self.query_all_students_all_fields)
        assert not result.errors
        # print(f"Yes : {result.data}")
        assert result.data == {'students': [{'studentId': '1', 'name': 'Mickey Mouse', 'age': 16}, {'studentId': '2', 'name': 'Mini Mouse', 'age': 15}]}

    def test_query_students_display_name_only(self):
        result = schema.execute(self.query_all_students_name_only)
        assert not result.errors
        # print(f"Yes : {result.data}")
        assert result.data == {'students': [{'name': 'Mickey Mouse'}, {'name': 'Mini Mouse'}]}

    def test_query_students_display_name_and_age_only(self):
        result = schema.execute(self.query_all_students_name_age_only)
        assert not result.errors
        # print(f"Yes : {result.data}")
        assert result.data == {'students': [{'name': 'Mickey Mouse', 'age': 16}, {'name': 'Mini Mouse', 'age': 15}]}

    def test_query_student(self):
        result = schema.execute(self.query_student_by_id)
        assert not result.errors
        # print(f"Yes : {result.data}")
        assert result.data == {'student': {'studentId': '1', 'name': 'Mickey Mouse', 'age': 16}}