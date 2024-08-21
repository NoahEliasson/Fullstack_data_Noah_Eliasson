emp_info = []
def add_employee(emp_id, name, dep, salary):
    
    emp_dict = {"emp_id": emp_id, "name": name, "department": dep, "salary": salary}
    emp_info.append(emp_dict)

add_employee(0, "alice", "HR", 31000)
add_employee(1, "Bob", "IT", 41000)
print(emp_info)
