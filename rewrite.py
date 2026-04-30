import os

with open('d:/WorkSpace/Work/WorkSpace/MicroSaas/HomeLoanSite/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

css_new = """\t\t:root {
\t\t\t--mui-primary: #4a3b8c;
\t\t\t--mui-primary-dark: #3a2b7c;
\t\t\t--mui-secondary: #f26b4d;
\t\t\t--mui-bg: #f8f9ff;
\t\t\t--mui-text-primary: #2d2d42;
\t\t\t--mui-text-secondary: rgba(0, 0, 0, 0.6);
\t\t\t--mui-card: #ffffff;
\t\t\t--mui-divider: rgba(0, 0, 0, 0.12);
\t\t\t--mui-elevation-1: 0px 4px 20px rgba(0, 0, 0, 0.05);
\t\t\t--mui-elevation-2: 0px 8px 30px rgba(0, 0, 0, 0.08);
\t\t\t--mui-elevation-4: 0px 12px 40px rgba(0, 0, 0, 0.12);
\t\t}
\t\t* { box-sizing: border-box; }
\t\thtml { scroll-behavior: smooth; }
\t\tbody {
\t\t\tmargin: 0;
\t\t\tfont-family: "Roboto", "Helvetica", "Arial", sans-serif;
\t\t\tbackground: linear-gradient(135deg, #f5f3fa 0%, #fff6f4 100%);
\t\t\tcolor: var(--mui-text-primary);
\t\t\tline-height: 1.5;
\t\t\tletter-spacing: 0.00938em;
\t\t\tmin-height: 100vh;
\t\t}
\t\t.mui-appbar {
\t\t\tposition: sticky; top: 0; z-index: 1100; background-color: #fff;
\t\t\tcolor: var(--mui-text-primary); box-shadow: 0 1px 10px rgba(0,0,0,0.05);
\t\t\tdisplay: flex; justify-content: center; align-items: center; min-height: 72px;
\t\t}
\t\t.header-btn {
\t\t\tdisplay: inline-flex; align-items: center; gap: 8px; padding: 8px 16px;
\t\t\tborder: 1px solid #c0c6cc; border-radius: 4px; color: var(--mui-text-primary);
\t\t\tfont-weight: 500; font-size: 0.875rem; text-decoration: none; background: #fff;
\t\t}
\t\t.mui-container {
\t\t\twidth: 100%; max-width: 1200px; margin-left: auto; margin-right: auto;
\t\t\tpadding: 48px 24px; display: grid; grid-template-columns: 1fr 420px;
\t\t\tgap: 48px; align-items: start;
\t\t}
\t\t.mui-container>section { grid-column: 1 / -1; }
\t\t.mui-hero {
\t\t\tgrid-column: 1 / 2; grid-row: 1 / 2; background: transparent; padding: 24px 0;
\t\t\ttext-align: left; display: flex; flex-direction: column;
\t\t}
\t\t.mui-hero h1 {
\t\t\tmargin: 0 0 24px; font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700;
\t\t\tletter-spacing: -0.02em; line-height: 1.2; color: #2d2d42;
\t\t}
\t\t.mui-hero h1 span.highlight { color: var(--mui-secondary); }
\t\t.hero-content-wrapper { display: flex; align-items: center; gap: 24px; margin-top: 32px; flex-wrap: wrap; }
\t\t.hero-image { max-width: 300px; width: 100%; object-fit: contain; }
\t\t.mui-hero .hero-features { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 16px; }
\t\t.mui-hero .hero-features li { display: flex; align-items: center; gap: 12px; font-size: 0.9375rem; font-weight: 500; color: var(--mui-text-primary); }
\t\t.mui-hero .hero-features .material-icons { color: #00e676; font-size: 20px; background: rgba(0, 230, 118, 0.1); border-radius: 50%; padding: 2px; }
\t\t.mui-section-title { margin: 0 0 8px; font-size: 2.125rem; font-weight: 400; color: var(--mui-text-primary); text-align: center; }
\t\t.mui-section-subtext { margin: 0 0 32px; font-size: 1.125rem; color: var(--mui-text-secondary); text-align: center; font-weight: 400; }
\t\t.mui-grid { display: grid; gap: 24px; }
\t\t.bank-section-wrapper { background: #fff; border-radius: 12px; padding: 48px; box-shadow: var(--mui-elevation-1); margin-bottom: 48px; }
\t\t.bank-grid { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 16px; }
\t\t.feature-grid { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
\t\t.blog-grid { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
\t\t.mui-card { background-color: var(--mui-card); border-radius: 8px; box-shadow: var(--mui-elevation-1); overflow: hidden; transition: box-shadow 300ms; display: flex; flex-direction: column; }
\t\t.mui-card:hover { box-shadow: var(--mui-elevation-4); }
\t\t.mui-card-content { padding: 16px; flex-grow: 1; }
\t\t.bank-card { padding: 16px; display: flex; flex-direction: column; justify-content: space-between; min-height: 140px; border: 1px solid var(--mui-divider); box-shadow: none; background: #fff; }
\t\t.bank-card:hover { box-shadow: var(--mui-elevation-2); border-color: var(--mui-primary); }
\t\t.bank-logo { max-width: 100%; height: 32px; width: auto; object-fit: contain; margin-bottom: 16px; align-self: flex-start; display: block; }
\t\t.bank-rates { display: flex; justify-content: space-between; margin-top: auto; padding-top: 12px; border-top: 1px dashed var(--mui-divider); }
\t\t.rate-col { display: flex; flex-direction: column; }
\t\t.rate-col:last-child { text-align: right; }
\t\t.rate-label { font-size: 0.65rem; color: var(--mui-text-secondary); text-transform: uppercase; }
\t\t.rate-val { font-size: 0.75rem; font-weight: 700; color: var(--mui-text-primary); }
\t\t.feature-card { text-align: center; padding: 32px 24px; }
\t\t.kpi-icon-wrapper { display: inline-flex; align-items: center; justify-content: center; width: 64px; height: 64px; border-radius: 50%; background-color: rgba(74, 59, 140, 0.08); color: var(--mui-primary); margin-bottom: 16px; }
\t\t.kpi-icon-wrapper .material-icons { font-size: 32px; }
\t\t.kpi-title { font-size: 1.25rem; font-weight: 500; margin: 0 0 8px; color: var(--mui-text-primary); }
\t\t.kpi-desc { font-size: 0.875rem; color: var(--mui-text-secondary); margin: 0; }
\t\t.blog-image { width: 100%; height: 160px; object-fit: cover; }
\t\t.blog-title { margin: 0 0 8px; font-size: 1.25rem; font-weight: 500; color: var(--mui-text-primary); }
\t\t.blog-text { margin: 0 0 16px; font-size: 0.875rem; color: var(--mui-text-secondary); }
\t\t.mui-card-actions { padding: 8px; display: flex; align-items: center; }
\t\t.read-more { color: var(--mui-primary); font-weight: 500; font-size: 0.875rem; text-decoration: none; text-transform: uppercase; padding: 6px 8px; border-radius: 4px; transition: background-color 250ms; }
\t\t.read-more:hover { background-color: rgba(74, 59, 140, 0.04); }
\t\t.form-section { grid-column: 2 / 3; grid-row: 1 / 2; background-color: #fff; border-radius: 16px; padding: 32px 24px; box-shadow: var(--mui-elevation-4); margin: 0; position: relative; }
\t\t.form-section-title { font-size: 1.25rem; font-weight: 700; margin: 0 0 24px; color: var(--mui-text-primary); text-align: left; }
\t\t.form-shell { display: flex; justify-content: center; margin-top: 0; }
\t\t#crmWebToEntityForm { width: 100%; }
\t\t@media (max-width: 1024px) { .mui-container { grid-template-columns: 1fr; } .mui-hero { grid-column: 1 / -1; grid-row: auto; } .form-section { grid-column: 1 / -1; grid-row: auto; } }
\t\t@media (max-width: 600px) { .mui-container { padding: 16px; gap: 32px; } .mui-hero { padding: 24px 0; } .form-section { padding: 24px 16px; } }
\n"""

header_hero_new = """\t<header class="mui-appbar">
\t\t<div style="width: 100%; max-width: 1200px; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
\t\t\t<div style="display: flex; align-items: center; gap: 12px;">
\t\t\t\t<span class="material-icons" style="color: #4a3b8c; font-size: 32px;">change_history</span>
\t\t\t\t<span style="font-weight: 900; font-size: 1.5rem; letter-spacing: 0.5px; color: #2d2d42; text-transform: uppercase;">TrueHome</span>
\t\t\t</div>
\t\t\t<div style="padding: 8px 0; margin: 0;">
\t\t\t\t<a href="tel:8247354529" class="header-btn">
\t\t\t\t\t<span class="material-icons" style="font-size: 18px;">phone_in_talk</span>
\t\t\t\t\tTalk to Expert
\t\t\t\t</a>
\t\t\t</div>
\t\t</div>
\t</header>

\t<main class="mui-container">
\t\t<section class="mui-hero">
\t\t\t<h1>Get Your Dream Home Loan<br>at 7.1% <span class="highlight">Compare 70+ Banks</span><br><span class="highlight">Now</span></h1>
\t\t\t
\t\t\t<div class="hero-content-wrapper">
\t\t\t\t<img src="https://illustrations.popsy.co/amber/home-office.svg" alt="House Illustration" class="hero-image" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=400&q=80'; this.style.borderRadius='12px'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.1)'">
\t\t\t\t<ul class="hero-features">
\t\t\t\t\t<li><span class="material-icons">check</span> Easy Digital Process</li>
\t\t\t\t\t<li><span class="material-icons">check</span> Lowest Interest Rates</li>
\t\t\t\t\t<li><span class="material-icons">check</span> Doorstep Document Collection</li>
\t\t\t\t\t<li><span class="material-icons">check</span> Exciting Vouchers on Disbursement</li>
\t\t\t\t</ul>
\t\t\t</div>
\t\t</section>\n"""

form_new = """\t\t<section class="form-section">
\t\t\t<h2 class="form-section-title">Check Your Home Loan Eligibility- Free!</h2>
\t\t\t<div class="form-shell">
\t\t\t\t<div id='crmWebToEntityForm' class='zcwf_lblLeft crmWebToEntityForm'>
\t\t\t\t\t<META HTTP-EQUIV='content-type' CONTENT='text/html;charset=UTF-8'>
\t\t\t\t\t<form id='webform1261711000000451827' action='https://crm.zoho.in/crm/WebToLeadForm'
\t\t\t\t\t\tname=WebToLeads1261711000000451827 method='POST'
\t\t\t\t\t\tonSubmit='javascript:document.charset="UTF-8"; return checkMandatory1261711000000451827()'
\t\t\t\t\t\taccept-charset='UTF-8'>
\t\t\t\t\t\t<input type='text' style='display:none;' name='xnQsjsdp' value='76c9cf840c00ae837ce800e1639d91aa44aa924aa79b6e124e0391aa69b47990'></input>
\t\t\t\t\t\t<input type='hidden' name='zc_gad' id='zc_gad' value=''></input>
\t\t\t\t\t\t<input type='text' style='display:none;' name='xmIwtLD' value='0c5c444af1d55db0a934af7f9a9c727694cae06845dffe1f24cdce9480578afb6920c38106f97a298b0d77da126cc99c'></input>
\t\t\t\t\t\t<input type='text' style='display:none;' name='actionType' value='TGVhZHM='></input>
\t\t\t\t\t\t<input type='text' style='display:none;' name='returnURL' value='null'></input>
\t\t\t\t\t\t<style>
\t\t\t\t\t\t\t.formsubmit.zcwf_button { color: white !important; background: #4a3b8c !important; border-radius: 8px !important; font-weight: 500 !important; font-size: 1rem !important; padding: 14px 24px !important; width: 100% !important; text-transform: none !important; border: none !important; cursor: pointer !important; margin-top: 24px !important; transition: all 0.3s ease !important; }
\t\t\t\t\t\t\t.formsubmit.zcwf_button:hover { background: #3a2b7c !important; }
\t\t\t\t\t\t\t#crmWebToEntityForm.zcwf_lblLeft { width: 100%; padding: 0; margin: 0; box-sizing: border-box; }
\t\t\t\t\t\t\t#crmWebToEntityForm.zcwf_lblLeft * { box-sizing: border-box; }
\t\t\t\t\t\t\t#crmWebToEntityForm { text-align: left; }
\t\t\t\t\t\t\t#crmWebToEntityForm * { direction: ltr; }
\t\t\t\t\t\t\t.zcwf_lblLeft .zcwf_col_fld input[type=text] { width: 100% !important; border: 1px solid #e0e0e0 !important; border-radius: 8px !important; padding: 12px 12px 12px 40px !important; font-size: 0.875rem !important; font-family: "Roboto", "Helvetica", "Arial", sans-serif !important; transition: border-color 200ms !important; box-sizing: border-box !important; }
\t\t\t\t\t\t\t.zcwf_lblLeft .zcwf_col_fld input[type=text]:focus { outline: none !important; border-color: #4a3b8c !important; }
\t\t\t\t\t\t\t.zcwf_lblLeft .zcwf_col_lab { display: none !important; }
\t\t\t\t\t\t\t.zcwf_lblLeft .zcwf_col_fld { width: 100% !important; position: relative; }
\t\t\t\t\t\t\t.zcwf_lblLeft .zcwf_row { margin: 16px 0px !important; display: flex; flex-direction: column; }
\t\t\t\t\t\t\t.input-icon { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: #9e9e9e; font-size: 20px !important; pointer-events: none; }
\t\t\t\t\t\t\t.spam-badge { position: absolute; right: -10px; bottom: -15px; background: #e8f5e9; color: #2e7d32; font-size: 11px; padding: 4px 8px; border-radius: 12px; display: inline-flex; align-items: center; gap: 4px; font-weight: 500; }
\t\t\t\t\t\t\t.custom-label { font-size: 0.75rem; color: var(--mui-text-secondary); margin-bottom: 8px; display: block; font-weight: 500; }
\t\t\t\t\t\t\t.custom-label span { color: red; }
\t\t\t\t\t\t\t.pill-group { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
\t\t\t\t\t\t\t.pill { border: 1px solid #e0e0e0; background: #fff; border-radius: 20px; padding: 6px 12px; font-size: 0.75rem; color: var(--mui-text-secondary); cursor: pointer; transition: all 0.2s; }
\t\t\t\t\t\t\t.pill.active { border-color: #4a3b8c; color: #4a3b8c; background: rgba(74, 59, 140, 0.05); font-weight: 500; }
\t\t\t\t\t\t\t.form-footer-subtext { text-align: center; font-size: 0.75rem; color: var(--mui-text-secondary); margin-top: 8px; margin-bottom: 24px; }
\t\t\t\t\t\t\t.whatsapp-toggle-wrapper { display: flex; align-items: center; justify-content: space-between; padding-top: 16px; border-top: 1px dashed #e0e0e0; font-size: 0.75rem; }
\t\t\t\t\t\t\t.whatsapp-toggle { display: flex; align-items: center; gap: 8px; color: var(--mui-text-primary); font-weight: 500; }
\t\t\t\t\t\t\t.switch { position: relative; display: inline-block; width: 34px; height: 20px; }
\t\t\t\t\t\t\t.switch input { opacity: 0; width: 0; height: 0; }
\t\t\t\t\t\t\t.slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: .4s; border-radius: 34px; }
\t\t\t\t\t\t\t.slider:before { position: absolute; content: ""; height: 16px; width: 16px; left: 2px; bottom: 2px; background-color: white; transition: .4s; border-radius: 50%; }
\t\t\t\t\t\t\tinput:checked + .slider { background-color: #4a3b8c; }
\t\t\t\t\t\t\tinput:checked + .slider:before { transform: translateX(14px); }
\t\t\t\t\t\t</style>

\t\t\t\t\t\t<div class='zcwf_row'>
\t\t\t\t\t\t\t<div class='zcwf_col_fld'>
\t\t\t\t\t\t\t\t<span class="material-icons input-icon">person_outline</span>
\t\t\t\t\t\t\t\t<input type='text' id='Last_Name' aria-required='true' aria-label='Last Name' name='Last Name' aria-valuemax='80' maxlength='80' placeholder="Full Name*">
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t
\t\t\t\t\t\t<div class='zcwf_row' style="margin-bottom: 32px !important;">
\t\t\t\t\t\t\t<div class='zcwf_col_fld'>
\t\t\t\t\t\t\t\t<span class="material-icons input-icon">phone_android</span>
\t\t\t\t\t\t\t\t<input type='text' id='Mobile' aria-required='true' aria-label='Mobile' name='Mobile' aria-valuemax='30' maxlength='30' placeholder="Contact No*">
\t\t\t\t\t\t\t\t<div class="spam-badge"><span class="material-icons" style="font-size: 12px;">verified_user</span> We don't spam!</div>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>

\t\t\t\t\t\t<label class="custom-label">Required Loan Amount <span>*</span></label>
\t\t\t\t\t\t<div class="pill-group">
\t\t\t\t\t\t\t<div class="pill active" onclick="togglePill(this)">Less than 20 Lakh</div>
\t\t\t\t\t\t\t<div class="pill" onclick="togglePill(this)">20 Lakh - 50 Lakh</div>
\t\t\t\t\t\t\t<div class="pill" onclick="togglePill(this)">50 Lakh - 1 Crore</div>
\t\t\t\t\t\t\t<div class="pill" onclick="togglePill(this)">1 Crore+</div>
\t\t\t\t\t\t</div>

\t\t\t\t\t\t<label class="custom-label">Employment Type <span>*</span></label>
\t\t\t\t\t\t<div class="pill-group">
\t\t\t\t\t\t\t<div class="pill active" onclick="togglePill(this)">Salaried</div>
\t\t\t\t\t\t\t<div class="pill" onclick="togglePill(this)">Self Employed</div>
\t\t\t\t\t\t</div>

\t\t\t\t\t\t<label class="custom-label">Monthly Income (Your monthly in hand income) <span>*</span></label>
\t\t\t\t\t\t<div class="pill-group">
\t\t\t\t\t\t\t<div class="pill active" onclick="togglePill(this)">Less than 50,000</div>
\t\t\t\t\t\t\t<div class="pill" onclick="togglePill(this)">50,000 - 1 Lakh</div>
\t\t\t\t\t\t\t<div class="pill" onclick="togglePill(this)">1 Lakh - 1.5 Lakh</div>
\t\t\t\t\t\t\t<div class="pill" onclick="togglePill(this)">1.5 Lakh+</div>
\t\t\t\t\t\t</div>

\t\t\t\t\t\t<div style="display: none;">
\t\t\t\t\t\t\t<input type='text' ftype='email' autocomplete='false' id='Email' aria-required='false' aria-label='Email' name='Email' aria-valuemax='100' crmlabel='' maxlength='100' value='dummy@example.com'>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<div style="display: none;">
\t\t\t\t\t\t\t<input type='text' id='First_Name' aria-required='false' aria-label='First Name' name='First Name' aria-valuemax='40' maxlength='40'>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<input type='text' type='hidden' style='display: none;' name='aG9uZXlwb3Q' value='' />
\t\t\t\t\t\t
\t\t\t\t\t\t<div class='zcwf_row' style="margin-bottom: 0 !important;">
\t\t\t\t\t\t\t<div class='zcwf_col_fld'>
\t\t\t\t\t\t\t\t<button type='submit' id='formsubmit' class='formsubmit zcwf_button'>Check Eligible Offers</button>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t
\t\t\t\t\t\t<div class="form-footer-subtext">
\t\t\t\t\t\t\tGet Call In 02 Minutes | No Impact on CIBIL | Safe &amp; Secure | Served to one million customers
\t\t\t\t\t\t</div>
\t\t\t\t\t\t
\t\t\t\t\t\t<div class="whatsapp-toggle-wrapper">
\t\t\t\t\t\t\t<div class="whatsapp-toggle">
\t\t\t\t\t\t\t\t<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" width="16" height="16">
\t\t\t\t\t\t\t\tGet updates on Whatsapp
\t\t\t\t\t\t\t\t<label class="switch">
\t\t\t\t\t\t\t\t\t<input type="checkbox" checked>
\t\t\t\t\t\t\t\t\t<span class="slider"></span>
\t\t\t\t\t\t\t\t</label>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div>T&amp;C Apply*</div>
\t\t\t\t\t\t</div>

\t\t\t\t\t\t<script>
\t\t\t\t\t\t\tfunction togglePill(el) {
\t\t\t\t\t\t\t\tvar siblings = el.parentElement.children;
\t\t\t\t\t\t\t\tfor(var i=0; i<siblings.length; i++){
\t\t\t\t\t\t\t\t\tsiblings[i].classList.remove('active');
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tel.classList.add('active');
\t\t\t\t\t\t\t}
\t\t\t\t\t\t\tfunction checkMandatory1261711000000451827() {
\t\t\t\t\t\t\t\tvar mndFileds = new Array('Last Name', 'Mobile');
\t\t\t\t\t\t\t\tvar fldLangVal = new Array('Full Name', 'Contact No');
\t\t\t\t\t\t\t\tfor (i = 0; i < mndFileds.length; i++) {
\t\t\t\t\t\t\t\t\tvar fieldObj = document.forms['WebToLeads1261711000000451827'][mndFileds[i]];
\t\t\t\t\t\t\t\t\tif (fieldObj) {
\t\t\t\t\t\t\t\t\t\tif (((fieldObj.value).replace(/^\s+|\s+$/g, '')).length == 0) {
\t\t\t\t\t\t\t\t\t\t\talert(fldLangVal[i] + ' cannot be empty.');
\t\t\t\t\t\t\t\t\t\t\tfieldObj.focus();
\t\t\t\t\t\t\t\t\t\t\treturn false;
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\tdocument.querySelector('.crmWebToEntityForm .formsubmit').setAttribute('disabled', true);
\t\t\t\t\t\t\t\treturn true;
\t\t\t\t\t\t\t}
\t\t\t\t\t\t</script>
\t\t\t\t\t</form>
\t\t\t\t</div>
\t\t\t</div>
\t\t</section>\n"""

# Find boundaries
css_start = -1
css_end = -1
for i, line in enumerate(lines):
    if '<style>' in line and i < 50:
        css_start = i
    if '</style>' in line and css_start != -1 and i < 500:
        css_end = i
        break

header_start = -1
hero_end = -1
for i, line in enumerate(lines):
    if '<header' in line:
        header_start = i
    if '</section>' in line and header_start != -1 and i > header_start and i < 500:
        hero_end = i
        break

form_start = -1
form_end = -1
for i, line in enumerate(lines):
    if '<section class="form-section">' in line:
        form_start = i
    if '</section>' in line and form_start != -1 and i > 1000:
        form_end = i
        break

print(f"css {css_start}-{css_end}, header {header_start}-{hero_end}, form {form_start}-{form_end}")

if css_start != -1 and css_end != -1:
    lines = lines[:css_start+1] + [css_new] + lines[css_end:]

# Re-calculate after length changed
header_start = -1
hero_end = -1
for i, line in enumerate(lines):
    if '<header' in line:
        header_start = i
    if '</section>' in line and header_start != -1 and i > header_start and i < 500:
        hero_end = i
        break

if header_start != -1 and hero_end != -1:
    lines = lines[:header_start] + [header_hero_new] + lines[hero_end+1:]

# Re-calculate
form_start = -1
form_end = -1
for i, line in enumerate(lines):
    if '<section class="form-section">' in line:
        form_start = i
    if '</section>' in line and form_start != -1 and i > 500:
        form_end = i
        break

if form_start != -1 and form_end != -1:
    lines = lines[:form_start] + [form_new] + lines[form_end+1:]

with open('d:/WorkSpace/Work/WorkSpace/MicroSaas/HomeLoanSite/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Rewrite successful!')
