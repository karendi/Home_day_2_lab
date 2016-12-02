#its a HTTP library.helps interact with REST_APIS or any service exposed over HTTP
import requests

#interacts with the user and allows them to enter 'commands'
while True:
    command = input('command? ').strip()
    """if the user wants to get a list of names
     from ('https://kenyatta_university/'), where the endpoint is GET/names/ """
    if command == 'GET':
        results = requests.get('https://kenyatta_university/names/')
        #check if the communication went okay
        if results.status_code != 200:
            #the commnication failed
            print( "API Error/{}".format(results.status_code))
        for student in results.json():
            #put the json data in one dictionary with key value pairs
            print('{}'.format(student[s_id]=student[s_name]))
    #post command
    elif command == 'POST':
        #details of the student
        student_id = input('enter student_id').strip()
        first_name = input('enter the first name').strip()
        middle_name = input('enter the middle name').strip()
        sur_name = input('enter the surname').strip()
        #the data to be sent
        student = dict(s_id = student_id, f_name = first_name ,
                  m_name = middle_name , s_name = sur_name)
        results = requests.post('https://kenyatta_university/names/' ,json=student)
        if results.status_code != 201:
            print( "API Error/{}".format(results.status_code))
        print('Created student idnumber/ {}'.format(results.json()["s_id"]))

    elif command == 'quit':
        break
    else:
        print('Invalid Command.')
