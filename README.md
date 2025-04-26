# Concentration and Complexation Calculator

## Description:
This Python application helps you calculate the volumes of various compounds required for a complex formation based on their concentrations, molar masses, and binding ratios. The user can input data for a complex and its constituent compounds, and the application will calculate the required volumes to be pipetted and the necessary buffer volume.

The application also supports **importing data from a JSON file** and **exporting results to a log file**. 

## Features:
- Input data for complex and compounds.
- Calculate volumes of compounds and buffer.
- Import compound data from a **JSON** file.
- Automatically save calculations and results to a **log file**.

## Requirements:
- Python 3.x
- `tkinter` (usually pre-installed with Python)
- JSON library (also included with Python standard library)

## Installation:
1. Clone the repository:
    ```bash
    git clone https://github.com/joerloeffler/complexing_calculations.git
    ```
2. Navigate into the project directory:
    ```bash
    cd concentration-complexation-calculator
    ```

## Usage:
1. Run the Python script:
    ```bash
    python concentration_calculator.py
    ```

2. **Input Fields**:
   - **Complex Concentration (mg/ml)**: The concentration of the complex in mg/ml.
   - **Complex Molar Mass (g/mol)**: The molar mass of the complex in g/mol.
   - **Final Volume (µL)**: The desired final volume in µL.
   
3. **Compound Data**:
   - Add compounds with concentration, molar mass, and binding ratio.
   - The application will calculate the volumes of compounds and buffer required.

4. **Load from JSON**:
   - You can import a JSON file with compound and complex data using the "Load from JSON" button.

5. **View Results**:
   - Once the data is entered, click "Calculate" to see the volumes for each compound and the buffer, as well as the intermediate calculations.

6. **Export**:
   - Results are written to a `concentrations.log` file.

## Example JSON format:
```json
{
    "complex": {
        "concentration": 0.98,
        "molar_mass": 50000,
        "final_volume": 21
    },
    "compounds": [
        {
            "name": "AB",
            "concentration": 0.98,
            "molar_mass": 50000,
            "ratio": 3
        },
        {
            "name": "AG",
            "concentration": 4.01,
            "molar_mass": 180000,
            "ratio": 1
        }
    ]
}
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.
