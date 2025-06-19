# Gemstone Price Prediction

This project predicts gemstone prices using machine learning.  
Follow these steps to set up your environment and run the code.

---

## 1. Clone the Repository

```sh
git clone https://github.com/your-username/Gemstone-Price-Prediction.git
cd Gemstone-Price-Prediction
```

---

## 2. Install Miniconda (if not already installed)

Download and install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

---

## 3. Create a Conda Environment

```sh
conda create --prefix ./env python=3.8 -y
```

---

## 4. Activate the Environment

**On Windows Command Prompt:**
```sh
conda activate %cd%\env
```
**Or (from project root):**
```sh
conda activate ./env
```

---

## 5. Install Dependencies

```sh
pip install -r requirements_dev.txt
```

---

## 6. Run the Template Script

```sh
python template.py
```

---

## 7. Deactivate the Environment (when done)

```sh
conda deactivate
```

---

## Notes

- If you use Jupyter notebooks, install Jupyter in your environment:
  ```sh
  pip install notebook
  ```
- If you encounter issues with environment activation, ensure Miniconda is added to your PATH and you have run `conda init` for your shell.


**Enjoy predicting gemstone