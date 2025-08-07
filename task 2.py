import csv
from fpdf import FPDF

def read_and_analyze(filename):
    data=[]
    with open(filename,newline='') as csvfile:
        reader= csv.DictReader(csvfile)
        reader.filenames=[field.strip() for field in reader.filenames]
        for row in reader:
            row={k.strip():v.strip() for k,v in row.items()}
            try:
                row['Salary']=int(row.get('Salary',0))
            except ValueError:
                row['Salary']=0
            data.append(row)
    return data

def summarize(data):
    summary={}
    for row in data:
        dept=row['Department']
        salary=row['Salary']
        if dept not in summary:
            summary[dept]={'count':0,'total_salary':0}
        summary[dept]['count']+=1
        summary[dept]['total_salary']+= salary
    return summary

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial","B",16)
        self.cell(0,10,"Employee Salary Report",ln=True,align="C")
        self.ln(10)

    def add_summary_table(self,summary):
        self.set_font("Arial","B",12)
        self.cell(60,10,"Department")
        self.cell(40,10,"Employees")
        self.cell(60,10,"Total Salary")
        self.ln()
        self.set_font("Arial","",12)
        for dept,stats in summary.items():
            self.cell(60,10,dept,1)
            self.cell(40,10,str(stats['count']),1)
            self.cell(60,10,str(stats['total_salary']),1)
            self.ln()

    def add_employee_table(self,data):
        self.set_font("Arial","B",12)
        self.cell(50,10,"Name",1)
        self.cell(50,10,"Department",1)
        self.cell(50,10,"Salary",1)
        self.ln()
        for row in data:
            self.cell(50,10,row['Name'])
            self.cell(50,10,row['Department'])
            self.cell(50,10,str(row['Salary']),1)
            self.ln()

def generate_pdf(data,summary="report.pdf"):
    pdf=PDFReport()
    pdf.add_page()
    pdf.add_summary_table(summary)
    pdf.ln(10)
    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"Employee Details",ln=True)
    pdf.add_employee_table(data)
    pdf.output('C:\\Users\\acraj\\OneDrive\\Desktop\\Bathri Codtech tasks\\data.csv')
    print("PDF report saved as :{'C:\\Users\\acraj\\OneDrive\\Desktop\\Bathri Codtech tasks\\data.csv")

if __name__=="__main__":
##    filename=('data.csv')
    data= read_and_analyze("C:\\Users\\acraj\\OneDrive\\Desktop\\Bathri Codtech tasks\\data.csv")
    summary=summarize(data)
    generate_pdf(data,summary)

    
