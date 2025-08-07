import pandas as pd
from fpdf import FPDF

# Step 1: Read data from the CSV file
def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Step 2: Analyze the data
def analyze_data(data):
    total_sales = data["Sales"].sum()
    total_profit = data["Profit"].sum()
    top_product = data.loc[data["Sales"].idxmax(), "Product"]
    return total_sales, total_profit, top_product

# Step 3: Generate a PDF report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", size=12, style="B")
        self.cell(0, 10, "Sales Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf_report(file_path, total_sales, total_profit, top_product):
    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"File Analyzed: {file_path}", ln=True)
    pdf.ln(10)

    pdf.cell(0, 10, f"Total Sales: ${total_sales}", ln=True)
    pdf.cell(0, 10, f"Total Profit: ${total_profit}", ln=True)
    pdf.cell(0, 10, f"Top-Selling Product: {top_product}", ln=True)

    pdf.ln(10)
    pdf.cell(0, 10, "Detailed Data:", ln=True)
    pdf.ln(5)

    # Add table headers
    pdf.set_font("Arial", size=10, style="B")
    pdf.cell(50, 10, "Product", 1)
    pdf.cell(50, 10, "Sales", 1)
    pdf.cell(50, 10, "Profit", 1)
    pdf.ln()

    # Add table data
    pdf.set_font("Arial", size=10)
    for _, row in data.iterrows():
        pdf.cell(50, 10, row["Product"], 1)
        pdf.cell(50, 10, str(row["Sales"]), 1)
        pdf.cell(50, 10, str(row["Profit"]), 1)
        pdf.ln()

    # Save the PDF
    pdf.output("Sales_Report.pdf")
    print("PDF report generated as 'Sales_Report.pdf'.")

# Main Function
if __name__ == "__main__":
    file_path = "sales_data.csv"

    # Read data
    print("Reading data...")
    data = read_data(file_path)

    if data is not None:
        # Analyze data
        print("Analyzing data...")
        total_sales, total_profit, top_product = analyze_data(data)

        # Generate PDF report
        print("Generating PDF report...")
        generate_pdf_report(file_path, total_sales, total_profit, top_product)
    else:
        print("Failed to analyze data.")
