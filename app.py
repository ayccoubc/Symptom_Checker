from flask import Flask, render_template, request
app = Flask(__name__)
import symptoms_redflags


@app.route('/', methods=['GET', 'POST'])
def symptom_check():
    if request.method == 'POST':
        selected_symptoms = request.form.getlist('symptoms')
        condition = request.form.get('condition')


        if condition and condition in symptoms_redflags.symptoms:
            red_flags = symptoms_redflags.symptoms[condition]['Red Flags']
            return render_template('red_flags.html', red_flags=red_flags)

        if selected_symptoms:
            possible_conditions = []
            for condition, data in symptoms_redflags.symptoms.items():
                if any(symptom in selected_symptoms for symptom in data['Symptoms']):
                    possible_conditions.append(condition)

            return render_template('possible_conditions.html', conditions=possible_conditions)

    return render_template('symptom_check.html', symptoms=symptoms_redflags.symptoms)


if __name__ == '__main__':
    app.run(debug=True)
