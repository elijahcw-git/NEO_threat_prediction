from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
app.debug = True

# Load the pre-trained model
with open('knn_nasa.pkl', 'rb') as file:
    model = pickle.load(file)

def get_label(prediction):
    if prediction == 0:
        return "Non-hazardous"
    elif prediction == 1:
        return "Hazardous"
    else:
        return "Unknown"
    
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ''
    if request.method == 'POST':
        try:
            features = [float(x) for x in request.form.values()]
            prediction = model.predict([features])[0]
            label = get_label(prediction)
            prediction_text = f"Near Earth Object Classification: {label}"
        except ValueError:
            prediction_text = "Invalid input. Please enter valid numerical values."
    print(prediction_text)
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
