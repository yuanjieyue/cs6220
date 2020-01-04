"""
To run this app, in your terminal:
> python iris_classification_api.py
"""

import connexion
# from sklearn.externals import joblib
from joblib import load

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

# Load our pre-trained model
clf = load('./model/steel_plate_fault_classifier.joblib')

# Implement a simple health check function (GET)
def health():
    # Test to make sure our service is actually healthy
    try:
        predict(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}

# Implement our predict function
def predict(X_Minimum, X_Maximum, Y_Minimum, Y_Maximum, Pixels_Areas,
       X_Perimeter, Y_Perimeter, Sum_of_Luminosity,
       Minimum_of_Luminosity, Maximum_of_Luminosity, Length_of_Conveyer,
       TypeOfSteel_A300, TypeOfSteel_A400, Steel_Plate_Thickness,
       Edges_Index, Empty_Index, Square_Index, Outside_X_Index,
       Edges_X_Index, Edges_Y_Index, Outside_Global_Index, LogOfAreas,
       Log_X_Index, Log_Y_Index, Orientation_Index, Luminosity_Index,
       SigmoidOfAreas):
    # Accept the feature values provided as part of our POST
    # Use these as input to clf.predict()
    prediction = clf.predict([[X_Minimum, X_Maximum, Y_Minimum, Y_Maximum, Pixels_Areas,
       X_Perimeter, Y_Perimeter, Sum_of_Luminosity,
       Minimum_of_Luminosity, Maximum_of_Luminosity, Length_of_Conveyer,
       TypeOfSteel_A300, TypeOfSteel_A400, Steel_Plate_Thickness,
       Edges_Index, Empty_Index, Square_Index, Outside_X_Index,
       Edges_X_Index, Edges_Y_Index, Outside_Global_Index, LogOfAreas,
       Log_X_Index, Log_Y_Index, Orientation_Index, Luminosity_Index,
       SigmoidOfAreas]])

    # {0: 'Bumps', 1: 'Dirtiness', 2: 'K_Scatch', 3: 'Other_Faults', 4: 'Pastry', 5: 'Stains', 6: 'Z_Scratch'}
    # Map the predicted value to an actual class
    if prediction[0] == 0:
        predicted_class = "Bumps"
    elif prediction[0] == 1:
        predicted_class = "Dirtiness"
    elif prediction[0] == 2:
        predicted_class = "K_Scatch"
    elif prediction[0] == 3:
        predicted_class = "Other_Faults"
    elif prediction[0] == 4:
        predicted_class = "Pastry"
    elif prediction[0] == 5:
        predicted_class = "Stains"
    else:
        predicted_class = "Z_Scratch"
    
    # Return the prediction as a json
    return {"prediction" : predicted_class}

# Read the API definition for our service from the yaml file
app.add_api("steel_plate_fault_classification_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()