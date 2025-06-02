# 🚗 Used‑Car Price Prediction
# *Please see the presentation branch for the implementation*
Predict the resale price of a used car in the Gulf region from its basic specs and listing description.

---

## 1 · Project Goal  
Provide a data‑driven tool that helps sellers and buyers **estimate a fair market price** for second‑hand cars, reducing negotiation time and spotting overpriced listings.

---

## 2 · Dataset  
Scraped **10 000 UAE listings** (`uae_used_cars_10k.csv`).  

| # | Feature | Example |
|---|---------|---------|
| 1 | Make | *Toyota* |
| 2 | Model | *Camry* |
| 3 | Year | 2020 |
| 4 | Price (AED) | 58 000 |
| 5 | Mileage (mi) | 75 000 |
| 6 | Body Type | Sedan |
| 7 | Cylinders | 4 |
| 8 | Transmission | Automatic |
| 9 | Fuel Type | Petrol |
|10 | Color | White |
|11 | Location | Dubai |
|12 | Description | “…with rear camera. **Condition:** Excellent.” |

---

## 3 · Exploratory Data Analysis 📊
* **Outliers** – ultra‑luxury cars inflate price distribution.  
* **Year** correlates positively with price; **Mileage** negatively after ≈150 k km.  
* SUVs show wider price variance than sedans/hatchbacks.  
---

## 4 · Feature Engineering ⚙️

| Step | Details |
|------|---------|
| **Currency & Units** | • Converted price **AED → SAR** × 1.02 &nbsp;• Mileage **mi → km** × 1.60934 |
| **Text Extraction** | Parsed `Description` with regex to get **Condition**, equipment list, and boolean **Rear Camera**. |
| **Segmentation** | Binned `Year`, `Mileage`, `Cylinders`, etc. into ordinal “segments” to capture non‑linear effects. |
| **Categorical Encoding** | Custom `one_hot_encoder()` → 14 categorical groups → 110 dummy columns (`drop_first=True`). |
| **Final Matrix** | `X_train` ≈ 8 100 × 120, `y_train` in SAR. |

---

## 5 · Modeling 🧠

| Model | R² | MAE (SAR) | MSE |
|-------|----|-----------|-----|
| **Random Forest Regressor** (best) | **0.81** | **≈ 89 678** | 3.15 × 10¹⁰ |


*Hyper‑parameters tuned with `RandomizedSearchCV` (n_estimators, max_depth, min_samples_split).*  
