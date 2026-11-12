#Smart Health Diagnosis System
# Rule-Based Expert System with Bayes Probability

# Knowledge Base: Diseases with symptoms and probabilities
diseases = {
    "Flu": {
        "symptoms": ["fever", "cough", "body pain", "fatigue"],
        "prior": 0.3
s    },
    "Common Cold": {
        "symptoms": ["cough", "sneezing", "runny nose"],
        "prior": 0.4
    },
    "Malaria": {
        "symptoms": ["fever", "chills", "sweating", "headache"],
        "prior": 0.2
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "fatigue", "loss of taste"],
        "prior": 0.1
    }
}

# Function to calculate probability using Bayes Rule
def calculate_probability(user_symptoms, disease_data):
    match_count = 0
    total_symptoms = len(disease_data["symptoms"])

    for symptom in disease_data["symptoms"]:
        if symptom in user_symptoms:
            match_count += 1

    likelihood = match_count / total_symptoms

    # Bayes Formula (simplified)
    posterior = likelihood * disease_data["prior"]

    return posterior


# Forward Reasoning: Evaluate all diseases
def diagnose(user_symptoms):
    results = {}

    for disease, data in diseases.items():
        probability = calculate_probability(user_symptoms, data)
        results[disease] = probability

    # Sort by highest probability
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    return sorted_results


# Suggestions based on disease
def get_suggestion(disease):
    suggestions = {
        "Flu": "Take rest, drink fluids, and consult a doctor if severe.",
        "Common Cold": "Stay hydrated and take steam inhalation.",
        "Malaria": "Consult doctor immediately and get blood test.",
        "COVID-19": "Isolate yourself and consult a healthcare provider."
    }
    return suggestions.get(disease, "Consult a doctor.")


# Main Programsprint("=== Smart Health Diagnosis System ===")
print("Enter symptoms (comma separated): ")
user_input = input()

# Convert input to list
user_symptoms = [sym.strip().lower() for sym in user_input.split(",")]

# Diagnose
results = diagnose(user_symptoms)

# Output
print("\nPossible Diagnoses:\n")

for disease, prob in results:
    print(f"{disease} -> Probability: {round(prob, 2)}")

# Most probable disease
best_disease = results[0][0]

print("\nMost Probable Disease:", best_disease)
print("Suggestion:", get_suggestion(best_disease))
