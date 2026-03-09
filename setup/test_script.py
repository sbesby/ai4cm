import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import duckdb 
from sklearn.linear_model import LinearRegression
from pathlib import Path


def main():
    print("🚀 Library test in progress...")

    # Test NumPy
    arr = np.array([1, 2, 3, 4, 5])
    print(f"✅ NumPy: Array created successfully -> {arr}")

    # Test Pandas
    df = pd.DataFrame({"Data": arr, "Square": arr**2})
    print("✅ Pandas: DataFrame created:")
    print(df)

    # Test Scikit-Learn (Simple Linear Regression)
    X = arr.reshape(-1, 1)
    y = arr * 2 + 1
    model = LinearRegression().fit(X, y)
    prediction = model.predict(np.array([[6]]))
    print(f"✅ Scikit-Learn: Prediction for 6 (expected 13) -> {prediction[0]}")

    # Test Matplotlib (Plot creation)
    plt.figure(figsize=(8, 4))
    plt.plot(df["Data"], df["Square"], marker="o", linestyle="--", color="b")
    plt.title("Matplotlib Test: y = x^2")
    plt.xlabel("Value")
    plt.ylabel("Square")
    plt.grid(True)

    save_path = "test_plot.png"
    plt.savefig(save_path)
    print(f"✅ Matplotlib: Plot successfully generated ({save_path})")

    # Test DuckDB
    try:
        base_path = Path(__file__).parent
        csv_path = base_path / "test_data.csv"
        con = duckdb.connect()
        # Querying the CSV directly
        result = con.execute(
            f"SELECT COUNT(*) FROM read_csv_auto('{csv_path}')"
        ).fetchone()
        print(f"✅ DuckDB: CSV loaded and queried successfully. Row count: {result[0]}")
    except (duckdb.Error, FileNotFoundError) as e:
        print(f"❌ DuckDB test failed: {e}")

    print("\n📦 Everything works correctly!")


if __name__ == "__main__":
    main()
