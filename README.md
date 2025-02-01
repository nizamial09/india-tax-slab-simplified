# India Tax Slabs Simplified FY 2025-26

A simple tax slab calculator to compute income tax based on predefined tax slabs announced for 2025-26. The calculator takes an input of income and outputs the applicable tax according to the specified tax rates. Tax percentages are fixed according to the 2025-26 tax rates.

![Simple Tax Slab Calculator](https://raw.githubusercontent.com/nizamial09/india-tax-slab-simplified/refs/heads/main/templates/stc_img.png)


## Features
- Calculates tax based on income input.
- Shows you tax percentage in each slab.

## Usage
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/tax-slab-calculator.git

2. Install the required dependencies
    ```bash
    pip install -r requirements.txt

3. Run the fastapi server
    ```bash
    python -m uvicorn main:app
    ```

    That will present an output like
    ```bash
    INFO:     Started server process [16780]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```

    Open the URL on a browser

4. Enter the amount and it gives the tax and break-ups
