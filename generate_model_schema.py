from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# File path for the output PDF
output_path = "model_schema.pdf"

# Create a canvas
c = canvas.Canvas(output_path, pagesize=letter)
width, height = letter

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 50, "Crowdfunding Model Relationships")

# Draw CustomUser
c.setFont("Helvetica-Bold", 12)
c.drawString(100, height - 100, "CustomUser (users app)")
c.setFont("Helvetica", 10)
c.drawString(120, height - 120, "- username, email, ...")

# Draw Fundraiser
c.setFont("Helvetica-Bold", 12)
c.drawString(100, height - 170, "Fundraiser (fundraisers app)")
c.setFont("Helvetica", 10)
c.drawString(120, height - 190, "- owner: ForeignKey to CustomUser")
c.drawString(120, height - 205, "- title, description, goal, ...")

# Draw Pledge
c.setFont("Helvetica-Bold", 12)
c.drawString(100, height - 250, "Pledge (fundraisers app)")
c.setFont("Helvetica", 10)
c.drawString(120, height - 270, "- supporter: ForeignKey to CustomUser")
c.drawString(120, height - 285, "- fundraiser: ForeignKey to Fundraiser")
c.drawString(120, height - 300, "- amount, comment, anonymous, ...")

# Draw arrows (simple lines for relationships)
c.line(180, height - 120, 180, height - 190)  # CustomUser to Fundraiser owner
c.line(180, height - 120, 180, height - 270)  # CustomUser to Pledge supporter
c.line(180, height - 205, 180, height - 285)  # Fundraiser to Pledge fundraiser

c.setFont("Helvetica-Oblique", 9)
c.drawString(100, height - 340, "Arrows indicate ForeignKey relationships.")

# Save the PDF
c.save()

print(f"PDF schema generated: {output_path}")
