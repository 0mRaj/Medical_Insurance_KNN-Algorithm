import pickle
import json
import Config
import numpy as np

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_' + region

    def load_model(self):
        with open(Config.MODEL_FILE_PATH,'rb') as f:
            self.KNN_model = pickle.load(f)

        with open(Config.SCALAR_FILE_PATH,'rb') as f:
            self.std_scalar = pickle.load(f)

        with open(Config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_charges(self):
        self.load_model()

        region_index = self.json_data["columns"].index(self.region)

        test_array = np.zeros(len(self.json_data['columns']))
        
        test_array[0] = self.age
        test_array[1] = self.json_data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data['smoker'][self.smoker]
        test_array[region_index] = 1

        Scaled_array = self.std_scalar.transform([test_array])


        print("Scaled Test array:",Scaled_array)  # 9 values
        predicted_charges  = self.KNN_model.predict(Scaled_array)
        return predicted_charges