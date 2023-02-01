import datetime

appointments = []

def schedule_appointment(date, time, description):
    appointment = {'date': date, 'time': time, 'description': description}
    appointments.append(appointment)
    print("Appointment successfully scheduled at {} on {} for: {}".format(time, date, description))

def check_appointments():
    if not appointments:
        print("No appointments scheduled.")
    else:
        print("Here are your appointments:")
        for appointment in appointments:
            print("Date: {} Time: {} Description: {}".format(appointment['date'], appointment['time'], appointment['description']))

def prompt_appointment():
    date = input("Enter the appointment date (YYYY-MM-DD): ")
    time = input("Enter the appointment time (HH:MM): ")
    description = input("Enter a brief description of the appointment: ")
    schedule_appointment(date, time, description)

def handle_command(command):
    if command == 'schedule':
        prompt_appointment()
    elif command == 'check':
        check_appointments()
    else:
        print("Unknown command. Please use 'schedule' or 'check'.")

def run_chatbot():
    print("Welcome to the appointment scheduler chatbot!")
    while True:
        command = input("Enter 'schedule' to schedule an appointment or 'check' to view your appointments: ")
        handle_command(command)

if __name__ == '__main__':
    run_chatbot()
