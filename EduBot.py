from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Initialize the user_names dictionary.
user_names = {}

# Initialize a dictionary to track user states.
user_states = {}


@app.route("/sms", methods=['POST'])
def sms_reply():
    # Get the user's message from the request.
    user_message = request.form.get('Body')
    user_phone = request.form.get('From')  # Get the user's phone number (sender's phone number)

    # Create a response object.
    response = MessagingResponse()

    print("Received user message:", user_message)  # Debugging line

    if user_phone not in user_names:
        # If the user's phone number is not in the dictionary, ask for their name and store it.
        user_names[user_phone] = user_message
        user_states[user_phone] = "name_prompt"
        response.message("Hi there, My name is EduBot. I'm your Virtual Assistant for today! What's your name?")
    else:
        # Handle user interactions based on their current state.
        if user_phone in user_states:
            state = user_states[user_phone]

            if state == "name_prompt":
                # Store the user's name and present the menu.
                user_names[user_phone] = user_message
                user_states[user_phone] = "menu"
                print("Updated user name:", user_names[user_phone])  # Debugging line
                response.message(f"Hello {user_names[user_phone]}, how can I assist you today? ")
                present_menu_and_handle_user_message(response)
            elif state == "menu":
                # Handle the user's user_message.
                handle_user_message(user_message, user_phone, response)
        else:
            response.message("Hi there, My name is EduBot. I'm your Virtual Assistant for today! What's your name?")
            user_states[user_phone] = "name_prompt"

    return str(response)


@app.route('/')
def home():
    # Define the response for the root URL
    return "Welcome to EduBot!"

# Define a function to handle user user_messages.
def handle_user_message(user_message, user_phone, response):
    # Get the user's user_message and respond accordingly.
    if user_message == '1':
        s_user_message(user_phone, response, user_message)
    elif user_message == '2':
        f_user_message(user_phone, response, user_message)
    elif user_message == '3':
        v_user_message(user_phone, response, user_message)
    elif user_message == '4':
        m_user_message(user_phone, response, user_message)
    else:
        response.message("Invalid option. Please choose a valid option.")

# Define a function to present the menu and handle user user_messages.
def present_menu_and_handle_user_message(response):
    response.message("1-> STUDENT SECTION")
    response.message("2-> FACULTY SECTION")
    response.message("3-> VISITOR SECTION")
    response.message("4-> MISCELLANEOUS SECTION")
    response.message("5-> EXIT")
    
    if response.message == '1':
        response.message(f"Hello! Welcome to our Student portal. How may I help you, {user_names}?")
        s_user_message()
    
    elif response.message == '2':
        response.message(f"Hello! Welcome to our Faculty portal. How may I help you, {user_names}?")
        f_user_message()

    elif response.message == '3':
        response.message(f"Hello! Welcome to our Visitor portal. How may I help you, {user_names}?")
        v_user_message()

    elif response.message == '4':
        response.message(f"Hello! Welcome to our Miscellaneous portal. How may I help you, {user_names}?")
        m_user_message()

    elif response.message == '5':
        response.message(f"THANK YOU, {user_names} for connecting with us. Have a great day!"
                  " For any other query, you can connect with me anytime.")
        response.message(f"THANK YOU, {user_names} for connecting with us. Have a great day!")

    else:
        response.message(f"Oops!! You have entered the wrong option, {user_names}. Please Select Again.")


def s_user_message(user_phone, response, user_message):
    print("Received user message:", user_message)  # Add this line to print the user's message.
    response.message("SELECT YOUR GRADUATION LEVEL")
    response.message("1-> UnderGraduation")
    response.message("2-> PostGraduation")

    if response.message == '1':
        response.message("UnderGraduation Courses are: ")
        response.message("1. BBA")
        response.message("2. BCA")
        response.message("3. BA-HONS")
        response.message("4. B.COM")
        response.message("5. B.COM-HONS")
        response.message("6. BA-LLB")

        response.message("Please select your Course: ")

        if response.message == 1:
            response.message("Visit to BBA")
            url = "https://www.smsvaranasi.com/bba.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        elif response.message == 2:
            response.message("Visit to BCA")
            url = "https://www.smsvaranasi.com/bca.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        elif response.message == 3:
            response.message("Visit to BA-HONS")
            url = "https://www.smsvaranasi.com/bahonsmasscomm.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        elif response.message == 4:
            response.message("Visit to B-COM")
            url = "https://www.smsvaranasi.com/bcom.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        elif response.message == 5:
            response.message("Visit to B.COM-HONS")
            url = "https://www.smsvaranasi.com/bcomhons.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        elif response.message == 6:
            response.message("Visit to BA-LLB")
            url = "http://smslawcollege.com/ba-llb.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        else:
            print("User entered an invalid choice:", user_message)
            response.message("No course Found!. Please select again->")
            response.message("Thank you for connecting with us ")
            
    elif user_message == '2':
        response.message("PostGraduation courses are: ")
        response.message("1. MBA")
        response.message("2. MCA")
        response.message("3. M.COM")

        response.message("Please select your course: ")
        
        if user_message == 1:
            response.message("Visit to MBA")
            url = "https://www.smsvaranasi.com/mba.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        elif user_message == 2:
            response.message("Visit to MCA")
            url = "https://www.smsvaranasi.com/mca.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        elif user_message == 3:
            response.message("Visit to MCOM")
            url = "https://www.smsvaranasi.com/mcom.html"
            response.message(url)
            response.message("Thank you for connecting with us ")
            
        else:
            response.message("No course Found!. Please select again->")
            response.message("Thank you for connecting with us ")
            
    else:
        response.message("Opps! You entered wrong option. Please enter a valid option.")
        response.message("Thank you for connecting with us ")
        #response.message("This is the response for Student option.")

def f_user_message(user_phone, response, user_message):
    response.message("CHOOSE YOUR DEPARTMENT: ")
    response.message("1. Computer Applications department")
    response.message("2. Management department")
    response.message("3. Visiting Faculty Industrial department")
    response.message("4. Visiting Faculty International department")
    response.message("5. Visiting Faculty Academic department")

    if user_message == '1':
        response.message("COMPUTER APPLICATIONS FACULTIES: ")
        response.message("Dr.Kamal Sheel Mishra - Head of Department")
        url1 = "https://www.smsvaranasi.com/view-faculty-details/40.html"
        response.message("Visit:" + url1)
        
        response.message("Mr.Shambhu Sharan Srivastava - (Associate Professor)")
        url2 = "https://www.smsvaranasi.com/view-faculty-details/41.html"
        response.message("Visit:" + url2)
        
        response.message("Mr.Anand Praksh Dubey - (Associate Professor)")
        url3 = "https://www.smsvaranasi.com/view-faculty-details/42.html"
        response.message("Visit:" + url3)
        
        response.message("Mr.Ram Gopal Gupta - (Associate Professor)")
        url4 = "https://www.smsvaranasi.com/view-faculty-details/43.html"
        response.message("Visit:" + url4)
        
        response.message("Dr.Aditya Kumar Gupta - (Associate Professor)")
        url5 = "https://www.smsvaranasi.com/view-faculty-details/44.html"
        response.message("Visit:" + url5)
        
        response.message("Mr.Vikash Chandra Sharma - (Associate Professor)")
        url6 = "https://www.smsvaranasi.com/view-faculty-details/46.html"
        response.message("Visit:" + url6)
        
        response.message("Dr.Radha Raman Chandan - (Associate Professor)")
        url7 = "https://www.smsvaranasi.com/view-faculty-details/55.html"
        response.message("Visit:" + url7)
        response.message("Thank you for connecting with us ")
        
    elif user_message == '2':
        response.message("2.MANAGEMENT FACULTIES: ")
        response.message("Prof.Pinak Nath Jha - Director")
        url1 = "https://www.smsvaranasi.com/view-faculty-details/1.html"
        response.message("Visit:" + url1)
        
        response.message("Mr.Sandeep Singh - (Professor)")
        url2 = "https://www.smsvaranasi.com/view-faculty-details/2.html"
        response.message("Visit:" + url2)
        
        response.message("Dr.Raj Kumar Singh - (Professor)")
        url3 = "https://www.smsvaranasi.com/view-faculty-details/3.html"
        response.message("Visit:" + url3)
        
        response.message("Dr.Sanjay Saxena - (Professor)")
        url4 = "https://www.smsvaranasi.com/view-faculty-details/4.html"
        response.message("Visit:" + url4)
        
        response.message("Dr.Avinash Chandra Supkar - (Professor)")
        url5 = "https://www.smsvaranasi.com/view-faculty-details/5.html"
        response.message("Visit:" + url5)
        
        response.message("Dr.Pallavi Pathak - (Professor)")
        url6 = "https://www.smsvaranasi.com/view-faculty-details/6.html"
        response.message("Visit:" + url6)
        
        response.message("Dr.Amitabh Pandey - (Professor)")
        url7 = "https://www.smsvaranasi.com/view-faculty-details/7.html"
        response.message("Visit:" + url7)
        
        response.message("Dr.Amit Kishore Sinha - (Professor)")
        url8 = "https://www.smsvaranasi.com/view-faculty-details/8.html"
        response.message("Visit:" + url8)
        
        response.message("Mr.Atish Khadse - (Associate Professor)")
        url9 = "https://www.smsvaranasi.com/view-faculty-details/9.html"
        response.message("Visit:" + url9)

        response.message("Dr.Bhavana Singh - (Associate Professor)")
        url10 = "https://www.smsvaranasi.com/view-faculty-details/10.html"
        response.message("Visit:" + url10)
        response.message("Thank you for connecting with us ")
        
    elif user_message == '3':
        response.message("3.VISITING FACULTIES INDUSTRIAL: ")
        response.message("Mr.Yogesh Kumar - (Ex.VP-HR, Bhartiya International, New Delhi)")
        response.message("Mr.K. Gopal - (Vice President- Finance, Price Water House Coopers)")
        response.message("Mr. Alok Agrawal - (Ex. Executive Director, Polar Industries, Noida)")
        response.message("Mr.D.V. Singh - (Director, NOV SARRA India Pvt. Ltd. Dehradun)")
        response.message("Mr. Ramesh Singh - Technical Director, NIC, New Delhi")
        response.message("Mr. Rajeev Chandola - (Head-HR & Admin, ColdEx, Gurgaon)")
        response.message("Mr. B. Sudhakar - (Head-HR, Tata Chemicals, Mumbai)")
        response.message("Mr. Rajeev Gupta - (Head-HR, Kajaria Group, New Delhi)")
        response.message("Thank you for connecting with us ")
        

    elif user_message == '4':
        response.message("4.VISITING FACULTIES INTERNATIONAL: ")
        response.message("Prof. Benjamin Yumol, Director, Claffin University, USA")
        response.message("Prof. Roberto Biloslavo, University of Primoska, Slovenia")
        response.message("Mr. Arun Kumar, Sr. Manager, Hanson, Australia")
        response.message("Dr. Harriet Nettles, Educational Psyuser_messagelogist, USA")
        response.message("Prof. Michael De Wilde, Grand Valley State University Allendale, USA")
        response.message("Dr. Sant Kumar, University of Gondar, Ethiopia")
        response.message("Rev. Patrick McCollum, Patrick Foundation, USA")
        response.message("Prof. Graham Ward, Director, INSEAD, France")
        response.message("Thank you for connecting with us ")
        

    elif user_message == '5':
        response.message("5.VISITING FACULTIES ACADEMIC: ")
        response.message("Prof. S.K. Kak, Former VC, Mahamaya Technical University, Noida")
        response.message("Prof. M.S. Lakshmi, ICFAI, Gurgaon, Haryana")
        response.message("Dr. Reena Shrivastava, Lucknow University, Lucknow")
        response.message("Prof. H. Karnik, IIT, Kanpur")
        response.message("Prof. S.K.Singh, FMS, BHU, Varanasi")
        response.message("Prof. A.K. Tripathi, IIT, BHU, varanasi")
        response.message("Prof. Atul Tandon, Former Director-MICA, Ahmedabad")
        response.message("Thank you for connecting with us ")
        

    else:
        response.message("Opps! You entered wrong option. Please enter a valid option-> ")
        response.message("Thank you for connecting with us ")
        
    
def v_user_message(user_phone, response, user_message):
    
    response.message("SELECT YOUR OPTION: ")
    response.message("1. Admission")
    response.message("2. Examination")
    response.message("3. Placement")
    response.message("4. Contact us")
    response.message("5. About Edubot ")

    if user_message == '1':
        response.message("1. UnderGraduate Level")
        response.message("2. PostGraduate level")
        response.message("3. Admission Process/Details")
        user_message1 = "Choose Your Option:"

        if user_message1 == 1:
            response.message("On the below link you can proceed further for your UG Admission:\n")
            ur1 = "https://online.smsvaranasi.com/apply/index.php"
            response.message(ur1)
            response.message("Thank you for connecting with us ")
           

        elif user_message1 == 2:
            response.message("On the below link you can proceed further for your PG Admission:\n")
            ur2 = "https://online.smsvaranasi.com/apply/index.php"
            response.message(ur2)
            response.message("Thank you for connecting with us ")
           

        elif user_message1 == 3:
            response.message("This is Our Admission Process and Details:\n")
            ur3 = "https://online.smsvaranasi.com/"
            response.message(ur3)
            response.message("Thank you for connecting with us ")
           

        else:
            response.message("Please select the correct option! Try Again.")
           
    elif user_message == '2':
        response.message("WELCOME TO OUR EXAMINATION PORTAL\nPlease Visit: ")
        ur1 = "https://examination.smsvaranasi.com/"
        response.message(ur1)
        response.message("Thank you for connecting with us ")
        

    elif user_message == '3':
        
        response.message("WELCOME TO OUR PLACEMENT PORTAL")
        
        response.message("1.Placement Cell: ")
        response.message("2.Placement Process: ")
        response.message("3.Placement Track Record: ")
        response.message("4.Placement Recruiters: ")
        response.message("5.Placement for Current Year: ")

        
        if response.message == 1:
            response.message("Visit to our Placement cell: ")
            ur1 = "https://www.smsvaranasi.com/training-placement-cell.html"
            response.message(ur1)

        elif response.message == 2:
            response.message("Visit to our Placement Process: ")
            ur1 = "https://www.smsvaranasi.com/placement-process.html"
            response.message(ur1)

        elif response.message == 3:
            response.message("Visit to our Placement Track Record: ")
            ur1 = "https://www.smsvaranasi.com/placement-track-record.html"
            response.message(ur1)

        elif response.message == 4:
            response.message("Visit to our Placement Recruiters: ")
            ur1 = "https://www.smsvaranasi.com/list-of-recruiters.html"
            response.message(ur1)

        elif response.message == 5:
            response.message("Visit to our Current Year Placement Recruits: ")
            ur1 = "https://www.smsvaranasi.com/current-year-placement.html"
            response.message(ur1)
            response.message("Thank you for connecting with us ")
           

        else:
            response.message("Please select the correct option! Try Again")
           

    elif user_message == '4':
        response.message("Please connect us on: ")
        url1 = "https://www.smsvaranasi.com/contact-us.html"
        response.message(url1)
        response.message("Thank you for connecting with us ")
        

    elif user_message == '5':
        response.message("EDUBOT")
        response.message("Hello Everyone I am EduBot. \n")
        response.message("I am an AI bot, I am developed by Group of 4 members from SMS College of "
              "Varanasi.\nSUMIT KUMAR \nANAND GUPTA \nATUL MISHRA \nVIVEK RAGHUVANSHI. \n")
        response.message("I am here to help you all who wants to connect with me. I will be helping\n"
              "you to guide in your new journey to our college.")
        response.message("THANK YOU " + user_names + " for connecting with me.")
        response.message("SEE YOU SOON, BYE FOR NOW!! HAVE A NICE DAY")   

    else:
        response.message("THANK YOU " + user_names + " for connecting with us ")
        
    #response.message("This is the response for Visitor user_message.")

def m_user_message(user_phone, response, user_message):
    response.message("SELECT YOUR OPTION: ")
    response.message("1-> Examination Fees")
    response.message("2-> Scholarship")
    response.message("3-> Hostel Fees")
    response.message("4-> SMS Law College")

    if user_message == 1:
        response.message("Please visit to our Examination Fee Portal ")
        url = "https://epay.smsvaranasi.com/"
        response.message(url)
        response.message("THANK YOU " + user_names + " for connecting with us ")
        
    elif user_message == 2:
        response.message("Please visit to our Scholarship Portal ")
        url = "https://www.smsvaranasi.com/sms-scholarship-form.html"
        response.message(url)
        response.message("THANK YOU " + user_names + " for connecting with us ")
        
    elif user_message == 3:
        response.message("Please visit to our Hostel Portal ")
        url = "https://www.smsvaranasi.com/hostel-requistion-form.html"
        response.message(url)
        response.message("THANK YOU " + user_names + " for connecting with us ")
        
    elif user_message == 4:
        response.message("Please visit to our newly LAW College for SMS ")
        url = "http://smslawcollege.com/"
        response.message(url)
        response.message("THANK YOU " + user_names + " for connecting with us ")
        

    else:
        response.message("Please select the correct option! Try Again")
        
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)