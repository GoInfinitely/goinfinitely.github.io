"""Generate the portfolio's two-page PDF from the supplied career information."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'docs/assets/jose-cabral-resume.pdf'
GREEN = colors.HexColor('#315b48')
INK = colors.HexColor('#202b27')
MUTED = colors.HexColor('#58645b')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', fontName='Helvetica-Bold', fontSize=27, leading=31, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle(name='Role', fontName='Helvetica', fontSize=12, leading=17, textColor=GREEN, spaceAfter=8))
styles.add(ParagraphStyle(name='ContactLine', fontName='Helvetica', fontSize=8.5, leading=13, textColor=MUTED, spaceAfter=15))
styles.add(ParagraphStyle(name='SectionLabel', fontName='Helvetica-Bold', fontSize=9, leading=14, textColor=GREEN, spaceBefore=15, spaceAfter=9))
styles.add(ParagraphStyle(name='Company', fontName='Helvetica-Bold', fontSize=11.5, leading=15, textColor=INK, spaceBefore=9, spaceAfter=3, keepWithNext=True))
styles.add(ParagraphStyle(name='JobMeta', fontName='Helvetica', fontSize=8.5, leading=13, textColor=MUTED, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name='Copy', fontName='Helvetica', fontSize=9, leading=14, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name='BulletCopy', fontName='Helvetica', fontSize=9, leading=13, textColor=INK, leftIndent=10, firstLineIndent=-8, spaceAfter=4))

story = []
def para(text, style='Copy'):
    story.append(Paragraph(text, styles[style]))

def job(company, role, dates, bullets):
    para(company, 'Company')
    para(f'{role} &nbsp; | &nbsp; {dates}', 'JobMeta')
    for bullet in bullets:
        para(f'&#8226; &nbsp; {bullet}', 'BulletCopy')

para('JOSE CABRAL', 'Name')
para('Senior Full Stack Python Engineer', 'Role')
para('Bronx, New York &nbsp; | &nbsp; <link href="mailto:josecabral.info@gmail.com">josecabral.info@gmail.com</link><br/><link href="https://goinfinitely.github.io/">goinfinitely.github.io</link> &nbsp; | &nbsp; <link href="https://github.com/GoInfinitely">github.com/GoInfinitely</link> &nbsp; | &nbsp; <link href="https://www.linkedin.com/in/jc-mtd/">linkedin.com/in/jc-mtd</link>', 'ContactLine')
para('PROFILE', 'SectionLabel')
para('Senior engineer building high-throughput backend systems, REST and GraphQL APIs, and event-driven microservices for SaaS, e-commerce, FinTech, and mobility platforms. Deep expertise in Python, asynchronous processing, real-time systems, and distributed architecture. Experienced delivering production services on AWS, Azure, and Google Cloud with Docker, Kubernetes, and Terraform.')
para('PROFESSIONAL EXPERIENCE', 'SectionLabel')
job('Curb Mobility', 'Senior Full Stack Python Engineer', 'Oct 2025 - Apr 2026', [
    'Engineered Python booking and dispatch services handling thousands of daily trips, with FastAPI, Django, WebSockets, and Redis.',
    'Reduced driver-rider matching time by 40% and improved API response time by 45% through PostgreSQL query optimization and caching.',
    'Built geolocation APIs, asynchronous Celery and RabbitMQ workflows, and Stripe payment and payout integrations.',
    'Delivered React rider and driver interfaces and deployed booking, dispatch, pricing, and payment microservices on AWS with Kubernetes.'
])
job('ELEKS', 'Senior Full Stack Python Engineer', 'Aug 2024 - Aug 2025', [
    'Built enterprise SaaS microservices and REST/GraphQL APIs using FastAPI, Django, Flask, React, Kafka, and Celery.',
    'Shortened release lead time by 55% using GitLab CI, Docker, and Terraform across AWS and Google Cloud.',
    'Accelerated terabyte-scale ETL pipelines by 60% through Pandas tuning and asynchronous workflows.',
    'Raised test coverage to 90% with PyTest suites integrated into CI/CD; deployed APIs to Cloud Run and Azure App Services.'
])
job('Peiko', 'Senior Backend &amp; MLOps Engineer', 'Feb 2022 - Mar 2024', [
    'Migrated a monolith to Django REST Framework and gRPC microservices, increasing release frequency by 45%.',
    'Improved reliability by 40% with Docker and Kubernetes, and streamlined data ingestion by 30% using caching and asynchronous streaming.',
    'Delivered FinTech backend services, Stripe billing, and event-driven pipelines with RabbitMQ and Google Cloud Pub/Sub; provisioned multi-cloud infrastructure with Terraform.'
])
story.append(PageBreak())
para('JOSE CABRAL', 'Name')
para('Experience & technical foundations', 'Role')
job('Amazon', 'Lead Backend Developer', 'Oct 2018 - Oct 2021', [
    'Architected Django and Flask APIs serving millions of requests per day for e-commerce applications.',
    'Led a cross-functional team of eight developers modernizing legacy Python services into Flask microservices.',
    'Cut p95 latency by 45% using Redis caching and Nginx rate limiting; implemented OAuth and JWT authentication.',
    'Built Airflow ETL pipelines, Celery order-processing and inventory queues, React dashboards, and zero-downtime deployment pipelines.'
])
job('Vention', 'Python Developer', 'May 2017 - Aug 2018', [
    'Built full stack applications and real-time telemetry APIs with Django, Flask, and React.',
    'Improved deployment speed by 50% through service decomposition and database performance by 40% through SQL and NoSQL query tuning.',
    'Delivered cloud infrastructure on Azure and Google Cloud, automated reporting with BigQuery, and coached junior developers on Flask and Django.'
])
para('TECHNICAL SKILLS', 'SectionLabel')
for title, text in [
    ('Backend &amp; APIs', 'Python, FastAPI, Django, Django REST Framework, Flask, REST, GraphQL, gRPC, WebSockets, OAuth, JWT, asynchronous processing'),
    ('Data &amp; messaging', 'SQL, PostgreSQL, Redis, Kafka, Celery, RabbitMQ, Pandas, NumPy, Dask, Airflow, BigQuery, ETL pipelines'),
    ('Cloud &amp; delivery', 'AWS, Azure, Google Cloud, Docker, Kubernetes, Terraform, GitLab CI, Jenkins, Nginx, PyTest, TDD, SonarQube'),
    ('Frontend', 'React, JavaScript, Redux, Plotly Dash, responsive interfaces'),
    ('ML tooling', 'MLflow, Kubeflow, DVC, Azure Machine Learning, experiment tracking, CI/CD for ML'),
]:
    para(f'<b>{title}</b> - {text}')
para('EDUCATION', 'SectionLabel')
para('<b>Master of Arts, Web Development &amp; Web Design</b><br/>Touro College | 2020 - 2022')
para('<b>Bachelor of Science, Computer Science</b><br/>DeVry College of New York | 2014 - 2017')

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#dfe4db'))
    canvas.line(42, 35, letter[0] - 42, 35)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(42, 23, 'Jose Cabral | goinfinitely.github.io')
    canvas.drawRightString(letter[0] - 42, 23, str(doc.page))
    canvas.restoreState()

doc = SimpleDocTemplate(str(DEST), pagesize=letter, rightMargin=42, leftMargin=42, topMargin=35, bottomMargin=48, title='Jose Cabral - Senior Full Stack Python Engineer', author='Jose Cabral')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f'Generated {DEST}')
