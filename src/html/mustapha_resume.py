from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Create document
doc = SimpleDocTemplate("resume.pdf", pagesize=A4,
                        rightMargin=30, leftMargin=30,
                        topMargin=30, bottomMargin=18)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CustomHeading1',
                          fontSize=16, leading=20, spaceAfter=10,
                          textColor="#5a3dff", fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name='CustomHeading2',
                          fontSize=12, leading=14, spaceAfter=6,
                          textColor="#5a3dff", fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name='CustomNormal',
                          fontSize=10, leading=14, fontName="Helvetica"))

content = []

# Header
content.append(Paragraph("<b>MUSTAPHA B. GARBA</b>", styles['CustomHeading1']))
content.append(Paragraph("SRE | DevOps Engineer | Cloud Engineer", styles['CustomNormal']))
content.append(Paragraph("Atlanta, GA | Email: garbamus2@gmail.com | Phone: 678-670-0769", styles['CustomNormal']))
content.append(Paragraph("LinkedIn: linkedin.com/in/mus-b-garba-789659294", styles['CustomNormal']))
content.append(Spacer(1, 12))

# Profile
content.append(Paragraph("Profile", styles['CustomHeading2']))
content.append(Paragraph(
    "Dedicated DevOps Engineer with expertise in CI/CD, cloud computing (AWS, Azure), "
    "automation (Terraform, Ansible, Python), and scalable infrastructure. "
    "Proven success streamlining workflows, reducing time-to-market, and improving system reliability.",
    styles['CustomNormal']))
content.append(Spacer(1, 12))

# Skills
content.append(Paragraph("Technical Skills", styles['CustomHeading2']))
skills = [
    ["Cloud Platforms:", "AWS, Azure"],
    ["Containerization & Orchestration:", "Docker, Kubernetes (EKS, GKE)"],
    ["Automation:", "Terraform, Ansible, Helm, Chef"],
    ["CI/CD:", "Jenkins, GitHub Actions, ArgoCD"],
    ["Monitoring:", "Prometheus, Grafana, ELK, CloudWatch"],
    ["Scripting:", "Python, Bash, Groovy"],
    ["Databases:", "MySQL, PostgreSQL, MongoDB"]
]
table = Table(skills, colWidths=[150, 320])
table.setStyle(TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
content.append(table)
content.append(Spacer(1, 12))

# Experience
content.append(Paragraph("Professional Experience", styles['CustomHeading2']))

experience = [
    ("DevOps Engineer, The Coca-Cola Company (Remote, Atlanta GA) — Jan 2024–Present",
     [
         "Optimized CI/CD pipelines, reducing deployment time by 30%.",
         "Automated AWS infrastructure with Terraform & CloudFormation.",
         "Implemented Docker & Kubernetes for microservices.",
         "Built & deployed AI agents for production environments."
     ]),
    ("DevOps Engineer Lead, Dominion Systems Inc (ONT) — Aug 2017–Jan 2024",
     [
         "Built complex CI/CD pipelines with Jenkins & GitHub.",
         "Migrated apps to microservices architecture.",
         "Automated infrastructure with Terraform & Ansible.",
         "Improved release cycle time by 30%."
     ]),
    ("AWS Cloud Engineer, Dominion Systems Inc (ONT) — Sep 2016–Jul 2017",
     [
         "Configured AWS DevOps services (CloudFormation, CodePipeline).",
         "Managed RDS, DynamoDB, Aurora, and hybrid networks."
     ]),
    ("Database Admin, First Data Inc (Atlanta GA) — Oct 2012–Aug 2016",
     [
         "Installed & configured Oracle 11g databases.",
         "Designed & implemented backup strategies (EXPDP/IMPDP).",
         "Optimized database performance & handled migrations."
     ]),
]

for job, bullets in experience:
    content.append(Paragraph(f"<b>{job}</b>", styles['CustomNormal']))
    for b in bullets:
        content.append(Paragraph(f"• {b}", styles['CustomNormal']))
    content.append(Spacer(1, 8))

# Education & Certifications
content.append(Spacer(1, 12))
content.append(Paragraph("Education & Certifications", styles['CustomHeading2']))
content.append(Paragraph("BSc, University of Buea", styles['CustomNormal']))
content.append(Paragraph("AWS Solutions Architect Associate", styles['CustomNormal']))

# Build PDF
doc.build(content)
