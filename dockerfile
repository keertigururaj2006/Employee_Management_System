# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /employee_details

# Copy python file
COPY employee_details.py .

# Run the program
CMD ["python", "employee_details.py"]