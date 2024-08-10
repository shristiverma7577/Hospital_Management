import tkinter as tk
from tkinter import messagebox

class HospitalManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("400x500")  # Set a window size
        
        # Sample data structures for storing patient and doctor info
        self.patients = []
        self.doctors = [
            {"name": "Dr. John Doe", "specialization": "General Physician"},
            {"name": "Dr. Jane Smith", "specialization": "Pediatrician"}
        ]
        
        # Labels and entries for patient registration
        tk.Label(root, text="Patient Registration", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack()
        tk.Label(root, text="Age:").pack()
        self.age_entry = tk.Entry(root, width=30)
        self.age_entry.pack()
        tk.Label(root, text="Gender:").pack()
        self.gender_entry = tk.Entry(root, width=30)
        self.gender_entry.pack()
        tk.Label(root, text="Contact No.:").pack()
        self.contact_entry = tk.Entry(root, width=30)
        self.contact_entry.pack()
        
        register_btn = tk.Button(root, text="Register Patient", command=self.register_patient)
        register_btn.pack(pady=20)
        
        # Display doctor information
        tk.Label(root, text="Doctors", font=("Helvetica", 16)).pack(pady=10)
        self.doctor_listbox = tk.Listbox(root, width=50)
        self.doctor_listbox.pack()
        for doctor in self.doctors:
            self.doctor_listbox.insert(tk.END, f"{doctor['name']} - {doctor['specialization']}")
        
    def register_patient(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        contact = self.contact_entry.get()
        
        if name and age and gender and contact:
            patient_info = {
                "name": name,
                "age": age,
                "gender": gender,
                "contact": contact
            }
            self.patients.append(patient_info)
            messagebox.showinfo("Success", "Patient registered successfully.")
            self.clear_patient_entries()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")
    
    def clear_patient_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementApp(root)
    root.mainloop()
