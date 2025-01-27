
# !Input :-
''' myinfo = {
            "server1" : {
                    "IBM": {
                        "datacenter":"Bangalore",
                        "env": {
                                "PR": "192.168.1.1",
                                "DR": "192.168.1.2"
                                }
                            }
                    }
            } '''

# !Output should be like:-
# Bangalore datacenter PR address is : 192.168.1.1
# Bangalore datacenter DR address is : 192.168.1.2

myinfo = {
    "server1": {
        "IBM": {
            "datacenter": "Bangalore",
            "env": {
                "PR": "192.168.1.1",
                "DR": "192.168.1.2"
            }
        }
    }
}

bangalore_PR = myinfo["server1"]["IBM"]["env"]['PR']
bangalore_DR = myinfo["server1"]["IBM"]["env"]['DR']

print(f"Bangalore datacenter PR address is : {bangalore_PR}")
print(f"Bangalore datacenter DR address is : {bangalore_DR}")


#! Task 1: Student Grade Tracker
#! Create a dictionary of student grades where:

#! Add grades for 3 students with their names as keys
#! Each student should have grades for "Math", "Science", and "English"
#! Print out each student's average grade
#! Use .get() to safely handle missing subjects

grades = {
    "Alice": {"Math": 85, "Science": 92, "English": 88},
    "Bob": {"Math": 90, "Science": 85, "English": 95},
    "Charlie": {"Math": 78, "Science": 88, "English": 82}
}

for student, subjects in grades.items():
    print(student, subjects)
    # Divide by the number of subjects for each student
    average = sum(subjects.values()) / len(subjects)
    print(f"{student}'s average grade: {average:.2f}")


#! Task 2: Dictionary Update Exercise
#! Create a program that:

#! Start with a basic user profile dictionary containing name and age
#! Create a second dictionary with additional user information (email and city)
#! Use .update() to merge them
#! Add error handling to prevent KeyError when accessing values
#! Print the final dictionary with all user details sorted by keys

def get_user_info(user_dict, key):
    return user_dict.get(key, "Not found")

user_profile = {
    "name": "Hammad",
    "age": 25
}

additional_info = {
    "email": "itshammadofficial@gmail.com",
    "city": "Peshawar"
}

user_profile.update(additional_info)

try:
    age1 = user_profile["agee"]
    print(f"{age1}'s age")

except KeyError as e:
    print(f"The key {e} does not exist")


for key, value in sorted(user_profile.items()):
    print(f"{key}: {value}")


# Using safe access with get_user_info function
print("\nSafe Access Examples:")
print(f"Name: {get_user_info(user_profile, 'name')}")
print(f"Age: {get_user_info(user_profile, 'age')}")
print(f"Email: {get_user_info(user_profile, 'email')}")
print(f"Phone: {get_user_info(user_profile, 'phone')}")  # Non-existent key