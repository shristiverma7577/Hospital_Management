# Hospital Management System

This is a simple Hospital Management System application built using Python's Tkinter library. The application allows for patient registration and displays a list of doctors available in the system.

## Features

- **Patient Registration:** 
  - Input fields for patient details including name, age, gender, and contact number.
  - Button to register a patient.
  - Patient information is stored in a list upon registration.

- **Doctor Information:**
  - Displays a list of doctors along with their specialization.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## How to Run

1. **Clone the repository or download the script**:
    ```bash
    git clone https://github.com/your-repo/hospital-management-system.git
    ```
    Or simply download the `hospital_management.py` script.

2. **Navigate to the directory**:
    ```bash
    cd hospital-management-system
    ```

3. **Run the application**:
    ```bash
    python hospital_management.py
    ```

## Usage

- **Patient Registration**: 
  - Enter the patient's name, age, gender, and contact number.
  - Click on the "Register Patient" button to add the patient to the system.

- **View Doctors**:
  - The list of doctors is displayed at the bottom of the window, showing their names and specializations.

## Application Structure

- `HospitalManagementApp`: The main class that initializes the Tkinter root window and sets up the UI components.
  - **Attributes**:
    - `self.patients`: A list to store registered patient information.
    - `self.doctors`: A list of dictionaries storing doctor names and specializations.
  - **Methods**:
    - `register_patient()`: Registers a new patient after validating the input fields.
    - `clear_patient_entries()`: Clears the input fields after successful patient registration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Tkinter documentation: https://docs.python.org/3/library/tkinter.html



This README.md provides a clear overview of the application, its features, requirements, and usage instructions. You can modify the content as needed to fit your specific repository or project structure.
