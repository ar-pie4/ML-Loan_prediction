from flask import Flask, render_template, request
import utils
from utils import predict
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict/', methods=['POST'])
def predict():

    gender = request.form.get('Gender')
    married = request.form.get('Married')
    education = request.form.get('Education')
    self_employed = request.form.get('Self_Employed')
    applicant_income = request.form.get('ApplicantIncome')
    coapplicant_income = request.form.get('CoapplicantIncome')
    loan_amount = request.form.get('LoanAmount')
    loan_amount_term = request.form.get('Loan_Amount_Term')
    credit_history = request.form.get('Credit_History')
    property_area = request.form.get('Property_Area')

    prediction = utils.predict(gender, married, education, self_employed, applicant_income,
   coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)

    return render_template('predict.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)