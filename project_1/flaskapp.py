from flask import Flask, request, jsonify
from mongoengine import connect
from mongoengine import Document, StringField, IntField

client=connect("Flask_rest_crud")

app = Flask(__name__)

class Employee(Document):
    name=StringField()
    no=IntField()
    add=StringField()
    mobile=IntField()

@app.route('/add_emp',methods=["POST"])
def hello_world():
    if request.method == "POST":
        name = request.json['name']
        no = request.json['no']
        add = request.json['add']
        mobile = request.json['mobile']
        emp = Employee(
            name=name,
            no=no,
            add=add,
            mobile=mobile
        )
        emp.save()
        return jsonify("saved successfully")

#read all employees
@app.route("/get_all_emp",methods=['GET'])
def get_all_emp():
    data_response = {"result":""}
    emp_list=[]
    emps=Employee.objects.all()
    for emp in emps:
        new_emp = {
            "id":str(emp.id),
            "name":emp.name,
            "no":emp.no,
            "add":emp.add,
            "mobile":emp.mobile
        }
        emp_list.append(new_emp)
    data_response["all_emp"] = emp_list
    return data_response

@app.route("/get_emp/<emp_id>",methods=["GET"])
def get_emp(emp_id):
    emp=Employee.objects.get(id=emp_id)
    new_emp = {
        "name" : emp.name,
        "no" : emp.no,
        "add" : emp.add,
        "mobile" : emp.mobile
    }
    return new_emp

#update
@app.route("/update_emp/<emp_id>",methods=['PUT'])
def update_emp(emp_id):
    name = request.json['name']
    no = request.json['no']
    add = request.json['add']
    mobile = request.json['mobile']
    emp=Employee.objects.get(id=emp_id)
    emp.update(
        name=name,
        no=no,
        add=add,
        mobile=mobile
    )
    return jsonify("employee record updated")

#delete
@app.route("/delete_emp/<emp_id>",methods=['DELETE'])
def delete_emp(emp_id):
    try:
        emp=Employee.objects.get(id=emp_id)
        emp.delete()
        return jsonify("Employee record deleted")
    except Employee.DoesNotExist :
        return jsonify("Employee does not exist")

if __name__ == '__main__':
    app.run()
