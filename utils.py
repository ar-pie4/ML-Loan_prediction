import pickle


def predict(gender, married, education, self_employed, applicant_income,
       coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area):
    gender_dict = {'Male':0, 'Female':1}
    married_dict = {'No':0, 'Yes':1}
    education_dict = {'Not Graduate':0, 'Graduate':1}
    self_employed_dict = {'No':0, 'Yes':1}
    property_area_dict = {'Urban':0, 'Rural':1, 'Semiurban':2}
    credit_history_dict = {'No':0, 'Yes':1}
    test_data = [[gender_dict[gender], married_dict[married], education_dict[education], self_employed_dict[self_employed], applicant_income,
       coapplicant_income, loan_amount, loan_amount_term, credit_history_dict[credit_history], property_area_dict[property_area]]]
    print(test_data)
    model = pickle.load(open('model.pkl','rb'))

    result = model.predict(test_data)
    print(result)
    if result[0] == 1:
        return 'Yes'
    else:
        return 'No'

