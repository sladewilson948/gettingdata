#the concept is to make a REST api that will create random credit cards numners check if they are valid or not generate random names emails and unique ids and then well store it in a mongo db as well all this will be done via flask application

from flask import Flask, jsonify
import random

data_dict = {}
app = Flask(__name__)
@app.route("/")
def random_data_here():
    fnames = ['Aman', 'Gaurav', 'Rachel', 'Tanushri', 'Salman', 'Peter']
    lanmes = ['Dubey', 'Singh', 'Sharma', 'Pandit', 'Malone', 'Sinaghania']
    cc_number = generate_valid_cards()
    name = random.choice(fnames)+' '+random.choice(lanmes)
    email = name.lower().replace(" ","_")+'@email.com'
    contact_number = f'{random.randint(000,999):03}-{random.randint(000,999):03}-{random.randint(0000,9999):04}'
    unique_id = f'{random.randint(00000,99999):05}'
    
    dict1 = {"name":name,
            "email":email,
            "contact_nmumber":contact_number,
            "card_number":cc_number,
            "unique_id":unique_id,
            "card_number":cc_number,
            "validity":"valid_card"
            }
    data_dict[len(data_dict.keys())]=dict1
    return jsonify(data_dict)

def absolute_sum(val):
    val = str(val)
    while len(val)!=1:
        val = list(val)
        val = [int(i) for i in val]
        val = sum(val)
        val = str(val)
    return int(val)
    

def generate_valid_cards():
    flag=True
    while flag==True:
        cc_number = f'{random.randint(0000,9999):04} {random.randint(0000,9999):04} {random.randint(0000,9999):04} {random.randint(0000,9999):04}'
        card_number = cc_number
        card_number = card_number.replace(" ","")
        part1 = list(card_number[-1::-2])
        part2 = list(card_number[-2::-2])
        part1 = [int(i) for i in part1]
        part2 = [2*int(i) for i in part2]
        part2 = [absolute_sum(i) for i in part2]
        sum_val = sum(part1)+sum(part2)
        if sum_val%10==0:
            flag=False
            return cc_number
        else:
            pass
            

    
    


if __name__ == '__main__':
    app.run()
