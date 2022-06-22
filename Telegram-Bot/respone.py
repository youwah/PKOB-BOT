import psycopg2
from datetime import datetime, timedelta



def sample_responses(input_text):
    #ic_text= input_text.split(" ")[0]
   # phone_text = input_text.split(" ")[1]
    input_text = str(input_text).lower()

    if "know about victim" in input_text:
            message = f"""Hi,please enter Ic Number and Phone Number to get victim's information. \n(Example:990302014356 0136754893). \n \n """
            return message
    if "know about pkob" in input_text:
            message = f"""Pusat Kawalan Operasi Bencana (PKOB) is a system to help victims that suffered from floods disaster in the village Mukim Bujang Merbok, Kedah. """
            return message
    if "know about website" in input_text:
            message = f"""Hi, this is our website link: \n(https://pkob272043.herokuapp.com)"""
            return message

    if " " in input_text:
        ic_text,phone_text = input_text.split(" ")
    else:
        message = "ERROR, Please enter in this format:990112025434 0137676123"
        return message

    try:
        conn = psycopg2.connect("postgres://ugcrqwfxdhbhrd:1599564401d654a2811bf3100c1c3cd294992daceffaa20d83aadfc2825f0e1c@ec2-54-145-9-12.compute-1.amazonaws.com:5432/d1bkdpd3pmbpfd")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM \"App_Soc_question\" WHERE ic_text = '{}' and \"phone_text\"= '{}'".format(ic_text,phone_text))
        conn.commit()
        result = cursor.fetchall()
        print(result)
        output = ''
        for x in result:

            birthday = str(x[1])[:6]
            date_time_obj = datetime.strptime(birthday, '%y%m%d')
            if date_time_obj > datetime.now():
                date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.now() - date_time_obj
            ageYears = int(age.days / 365)

            output = "This is victim's information: " + "\n" + "\n" + \
                     "Kad Pengenalan: " + output + str(x[1]) + "\n" + \
                     "Nombor Telefon: " + output + str(x[2]) + "\n" + \
                     "Nama: " + output + str(x[0]) + "\n" + \
                     "Umur: " + output + str(ageYears) + "\n"

            output = output.replace("'", "")
            output = output.replace(")", "")
            output = output.replace("(", "")
            output = output.replace(",", "")

        message = output
        if result==[]:
            message ="Detail no found! Please enter again Ic Number and Phone Number."
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        message = "Sorry no matching data"

    return message
