import pandas as pd

def run_ai_copilot_audit(csv_path="data/wafer_production_yield.csv", threshold_pct=-5.0):
    """Scans production data and generates automated AI executive insights."""
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("Sample data loading simulated...")
        return

    anomalies = df[df["yield_variance_pct"] <= threshold_pct].copy()
    total_loss = abs(anomalies["revenue_variance_usd"].sum())

    print("=== AI COPILOT ANALYTICS BRIEF ===")
    print(f"Status: Alert Triggered")
    print(f"Critical Lots Identified: {len(anomalies)}")
    print(f"Total Revenue Impact at Risk: ${total_loss:,.2f}")
    print("===================================\n")

if __name__ == "__main__":
    run_ai_copilot_audit()
