from flask import Flask, render_template, request
app = Flask(__name__)

symptoms = {
    'Back Pain': {
        'Symptoms': ['Symptom 1', 'Symptom 2', 'Symptom 3'],
        'Red Flags': ['Red Flag 1', 'Red Flag 2', 'Red Flag 3']
    },
    'Headache': {
        'Symptoms': ['Symptom 4', 'Symptom 5', 'Symptom 6'],
        'Red Flags': ['Red Flag 4', 'Red Flag 5', 'Red Flag 6']
    },
    # Add more symptoms and conditions here
}


@app.route('/', methods=['GET', 'POST'])
def symptom_check():
    if request.method == 'POST':
        selected_symptoms = request.form.getlist('symptoms')
        condition = request.form.get('condition')


        if condition and condition in symptoms:
            red_flags = symptoms[condition]['Red Flags']
            return render_template('red_flags.html', red_flags=red_flags)

        if selected_symptoms:
            possible_conditions = []
            for condition, data in symptoms.items():
                if any(symptom in selected_symptoms for symptom in data['Symptoms']):
                    possible_conditions.append(condition)

            return render_template('possible_conditions.html', conditions=possible_conditions)

    return render_template('symptom_check.html', symptoms=symptoms)


if __name__ == '__main__':
    app.run(debug=True)
