import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats

# Load data from CSV
data = pd.read_csv('Smoking Drinking Dataset 1000 data 10 var.csv', delimiter=',')

# Daftar variabel yang ingin dianalisis
variable_combinations = [
    ('age', ['height', 'weight', 'sight_left', 'sight_right', 'SBP', 'DBP', 'BLDS', 'HDL_chole', 'LDL_chole', 'triglyceride']),

    # Tambahkan kombinasi variabel lainnya sesuai kebutuhan
]

for dependent_var, independent_var in variable_combinations:
    print("🟰" * 55)
    print(f"\nAnalisis Regresi untuk {dependent_var} dan {independent_var}:\n")

    # Variabel dependen dan independen
    y = data[dependent_var]
    X = data[independent_var]

    # Tambahkan konstanta ke variabel independen
    X = sm.add_constant(X)

    # Fit model regresi
    model = sm.OLS(y, X).fit()

    # Tampilkan ringkasan hasil regresi
    print(model.summary())

    # Uji Simultan Regresi (F-statistik)
    f_statistic, f_p_value = sm.stats.linear_rainbow(model)
    print()
    print(f"F-statistic: {f_statistic}, p-value: {f_p_value}")
    if f_p_value < 0.05:
        print("Kesimpulan: Setidaknya satu variabel independen memiliki efek yang signifikan terhadap variabel dependen")
    else:
        print("Kesimpulan: Tidak ada bukti signifikansi keseluruhan model regresi")

    # Uji Kebaikan Model menggunakan R2
    r_squared = model.rsquared
    print()
    print(f"R-squared: {r_squared}\n")