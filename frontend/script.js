const form = document.getElementById("predictionForm");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const data = {
        Age: Number(document.getElementById("Age").value),

        Years_of_Experience:
            Number(document.getElementById("Years_of_Experience").value),

        Education:
            document.getElementById("Education").value,

        Job_Role:
            document.getElementById("Job_Role").value,

        Location:
            document.getElementById("Location").value,

        Previous_Salary:
            Number(document.getElementById("Previous_Salary").value)
    };


    const predictedSalary =
        document.getElementById("predictedSalary");

    const resultMessage =
        document.getElementById("resultMessage");


    predictedSalary.textContent = "Calculating...";

    resultMessage.textContent =
        "Please wait while the ML model predicts your salary.";


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        const result = await response.json();


        if (!response.ok) {
            throw new Error("Prediction failed");
        }


        predictedSalary.textContent =
            "₹ " +
            Number(result.predicted_salary)
                .toLocaleString("en-IN");


        resultMessage.textContent =
            "Salary predicted successfully!";


    } catch (error) {

        predictedSalary.textContent = "₹ 0";

        resultMessage.textContent =
            "Unable to connect to the prediction server.";

        console.error(error);
    }

});