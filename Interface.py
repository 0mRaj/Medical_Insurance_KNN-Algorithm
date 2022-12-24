from flask import Flask, render_template,request,jsonify
import Config
from Project_App.Utils import MedicalInsurance

app = Flask(__name__)

########################### HOME API ####################################
@app.route('/')
def hello_flask():
    print("WELCOME to Flask")
    return jsonify({'Model':"Sucessfully builded"})

##############################################################################################

@app.route("/predict_charges")
def get_insurance_charges():
    data = request.form
    age= eval(data['age'])
    sex= data['sex']
    bmi= eval(data['bmi'])
    children= eval(data['children'])
    smoker= data['smoker']
    region = data['region']

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predicted_charges()

    return jsonify({'Result':f"Predicted Medical insurance charges are :{charges}"})




if __name__ == '__main__':
    app.run()