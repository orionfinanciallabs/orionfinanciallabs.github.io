import os

with open('d:/WorkSpace/Work/WorkSpace/MicroSaas/HomeLoanSite/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<main class="mui-container">' in l:
        print(f'MAIN START at {i}')
    if '<section class="bank-section-wrapper">' in l:
        print(f'BANK START at {i}')
    if '<section class="form-section">' in l:
        print(f'FORM START at {i}')
    if '</form>' in l:
        print(f'FORM END at {i}')
