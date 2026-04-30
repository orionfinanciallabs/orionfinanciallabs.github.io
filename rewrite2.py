import re

with open('d:/WorkSpace/Work/WorkSpace/MicroSaas/HomeLoanSite/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. CSS changes
text = re.sub(
    r'\.mui-container \{.*?\n\t\t\}',
    '.mui-container {\\n\\t\\t\\twidth: 100%; max-width: 1200px; margin-left: auto; margin-right: auto;\\n\\t\\t\\tpadding: 48px 24px; display: flex; flex-direction: column; gap: 48px;\\n\\t\\t}',
    text, flags=re.DOTALL
)

text = re.sub(
    r'\.mui-container>section \{ grid-column: 1 / -1; \}',
    '',
    text
)

text = re.sub(
    r'\.mui-hero \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)

text = re.sub(
    r'\.mui-hero h1 \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)
text = re.sub(
    r'\.mui-hero h1 span\.highlight \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)
text = re.sub(
    r'\.hero-content-wrapper \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)
text = re.sub(
    r'\.hero-image \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)
text = re.sub(
    r'\.mui-hero \.hero-features \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)
text = re.sub(
    r'\.mui-hero \.hero-features li \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)
text = re.sub(
    r'\.mui-hero \.hero-features \.material-icons \{.*?\n\t\t\}',
    '',
    text, flags=re.DOTALL
)
text = re.sub(
    r'\.form-section \{.*?\n\t\t\}',
    '.form-section {\\n\\t\\t\\tbackground-color: #fff; border-radius: 24px; padding: 48px; box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08); margin: 0; display: grid; grid-template-columns: 1.2fr 1fr; gap: 64px; align-items: center;\\n\\t\\t}\\n\\t\\t.form-left { display: flex; flex-direction: column; }\\n\\t\\t.form-left h1 { margin: 0 0 40px; font-size: clamp(2rem, 3.5vw, 3rem); font-weight: 700; letter-spacing: -0.02em; line-height: 1.2; color: #2d2d42; }\\n\\t\\t.form-left h1 span.highlight { color: var(--mui-secondary); }\\n\\t\\t.form-left-content { display: flex; align-items: center; gap: 32px; flex-wrap: wrap; }\\n\\t\\t.form-left-image { max-width: 340px; width: 100%; object-fit: contain; }\\n\\t\\t.form-features { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 20px; }\\n\\t\\t.form-features li { display: flex; align-items: center; gap: 16px; font-size: 1.0625rem; font-weight: 500; color: var(--mui-text-primary); }\\n\\t\\t.form-features .material-icons { color: #fff; font-size: 20px; background: #00e676; border-radius: 50%; padding: 4px; }\\n\\t\\t.form-right { background: #fff; }',
    text, flags=re.DOTALL
)

text = re.sub(
    r'@media \(max-width: 1024px\) \{.*?\n\t\t\}',
    '@media (max-width: 1024px) {\\n\\t\\t\\t.form-section { grid-template-columns: 1fr; padding: 32px 24px; gap: 48px; }\\n\\t\\t}',
    text, flags=re.DOTALL
)
text = re.sub(
    r'@media \(max-width: 600px\) \{.*?\n\t\t\}',
    '@media (max-width: 600px) {\\n\\t\\t\\t.mui-container { padding: 16px; gap: 32px; }\\n\\t\\t\\t.form-section { padding: 24px 16px; gap: 32px; }\\n\\t\\t}',
    text, flags=re.DOTALL
)

# 2. HTML changes
# Delete old mui-hero
text = re.sub(
    r'<section class="mui-hero">.*?</section>',
    '',
    text, flags=re.DOTALL
)

# Move form section to top, and inject form-left
form_match = re.search(r'<section class="form-section">.*?</section>', text, flags=re.DOTALL)
if form_match:
    form_html = form_match.group(0)
    text = text.replace(form_html, '') # Remove it from bottom
    
    # Rebuild form section
    form_inner = re.sub(r'<section class="form-section">\n\t\t\t<h2 class="form-section-title">Check Your Home Loan Eligibility- Free!</h2>', '', form_html)
    form_inner = re.sub(r'</section>$', '', form_inner)
    
    new_form_html = """<section class="form-section">
\t\t\t<div class="form-left">
\t\t\t\t<h1>Compare 70+ Banks Now and <span class="highlight">Choose the Cheapest One</span></h1>
\t\t\t\t<div class="form-left-content">
\t\t\t\t\t<img src="https://illustrations.popsy.co/amber/home-office.svg" alt="House Illustration" class="form-left-image" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=400&q=80'; this.style.borderRadius='12px'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.1)'">
\t\t\t\t\t<ul class="form-features">
\t\t\t\t\t\t<li><span class="material-icons">check</span> Easy Digital Process</li>
\t\t\t\t\t\t<li><span class="material-icons">check</span> Lowest Interest Rates</li>
\t\t\t\t\t\t<li><span class="material-icons">check</span> Doorstep Document Collection</li>
\t\t\t\t\t\t<li><span class="material-icons">check</span> Exciting Vouchers on Disbursement</li>
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t\t<div class="form-right">
\t\t\t\t<h2 class="form-section-title" style="margin-top: 0;">Check Your Home Loan Eligibility- Free!</h2>
""" + form_inner + """
\t\t\t</div>
\t\t</section>"""

    # Insert right after <main class="mui-container">
    text = text.replace('<main class="mui-container">', '<main class="mui-container">\n' + new_form_html)

with open('d:/WorkSpace/Work/WorkSpace/MicroSaas/HomeLoanSite/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html successfully')
