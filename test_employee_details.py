from employee_details import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Keerti\n"
        "Employee ID: 284\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    assert employee_details("Keerti", "284", "IT", 50000) == expected_output