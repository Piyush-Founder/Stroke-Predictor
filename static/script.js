document.getElementById('submit1').onclick = async function (event) {
    event.preventDefault();

    let age = document.getElementById('age').value;
    let gender = document.getElementById('gender').value;
    let hypertension = document.getElementById('hypertension').value;
    let heart_disease = document.getElementById('heart_disease').value;
    let ever_married = document.getElementById('ever_married').value;
    let avg_glucose_level = document.getElementById('avg_glucose_level').value;
    let work_type = document.getElementById('work_type').value;
    let Residence_type = document.getElementById('Residence_type').value;
    let smoking_status = document.getElementById('smoking_status').value;

    let response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            age: Number(age),
            gender: gender,
            hypertension: Number(hypertension),
            heart_disease: Number(heart_disease),
            ever_married: ever_married,
            avg_glucose_level: Number(avg_glucose_level),
            work_type: work_type,
            Residence_type: Residence_type,
            smoking_status: smoking_status
        })
    });

    let data = await response.json();

    if (data.prediction === 1) {
        document.getElementById('result').innerText = 'Prediction: Stroke Risk';
    } else {
        document.getElementById('result').innerText = 'Prediction: No Stroke Risk';
    }
};
