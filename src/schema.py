import graphene
from graphene import Int


################################################################
# Reference Urls
# https://github.com/graphql-python/graphene/blob/master/examples/simple_example.py
# https://github.com/graphql-python/graphene/blob/master/examples/complex_example.py
################################################################


class Student(graphene.ObjectType):
    student_id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()

students_data = [{'student_id': 1, 'name': 'Mickey Mouse', 'age': 16}, {'student_id': 2, 'name': 'Mini Mouse', 'age': 15}]

################################################################
# http://127.0.0.1:8000/graphql/    # Use this url on the browser - normal url
# http://127.0.0.1:8000/graphql-p/  # Use this url on the browser - playground url


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="graphql"))
    student = graphene.Field(Student, student_id=Int(required=True))
    students = graphene.List(Student)

    # {
    #   hello(name: "mickey")
    # }
    #
    # {
    #   hello
    # }
    #
    def resolve_hello(root, info, name):
        return f"Hello {name}"

    # query {
    #   student(studentId: 1) {
    #     studentId
    #     name
    #     age
    #   }
    # }
    def resolve_student(root, info, student_id):
        # return students_data[0]
        for student in students_data:
            if student['student_id'] == int(student_id):
                return student

        raise Exception(f"Student {student_id} not found")



    # query {
    #     students {
    #         studentId
    #         name
    #         age
    #     }
    # }
    def resolve_students(root, info, limit=None):
        return students_data
################################################################
# mutation {
#     createStudent(age: 17, name: "Donald Duck") {
#        student {
#             studentId,
#             name,
#             age
#         }
#     }
# }

class CreateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()

    student = graphene.Field(Student)

    def mutate(root, info, name, age):
        student = {'student_id': len(students_data)+1, 'name': name, 'age': age}
        students_data.append(student)
        return CreateStudent(student=student)

################################################################

class UpdateStudent(graphene.Mutation):
    class Arguments:
        student_id = graphene.ID(required=True)
        name = graphene.String()
        age = graphene.Int()

    student = graphene.Field(Student)

    def mutate(root, info, student_id: int, name=None, age=None):
        for student in students_data:
            if student['student_id'] == int(student_id):
                if name:
                    student['name'] = name
                if age:
                    student['age'] = age
                return UpdateStudent(student=student)

        raise Exception(f"Student {student_id} not found")

################################################################

# mutation {
#     deleteStudent(studentId: 4) {
#          success
#     }
# }
#
# mutation {
#     deleteStudent(studentId: 4) {
#         success
#     }
# }

class DeleteStudent(graphene.Mutation):
    class Arguments:
        student_id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, student_id: int):
        for student in students_data:
            if student['student_id'] == int(student_id):
                students_data.remove(student)
                return DeleteStudent(success=True)

        raise Exception(f"Student {student_id} not found")


################################################################

class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()

################################################################

schema = graphene.Schema(query=Query, mutation=Mutation)
