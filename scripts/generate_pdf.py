import os
import sys
import asyncio
from playwright.async_api import async_playwright

async def generate_pdf():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print_html_path = os.path.join(base_dir, 'site', 'print_page', 'index.html')
    output_pdf_path = os.path.join(base_dir, 'Agentic_Engineering_Handbook_KR.pdf')
    
    if not os.path.exists(print_html_path):
        print("Site print_page not found. Building site first...")
        build_script = os.path.join(base_dir, 'scripts', 'build_docs.py')
        os.system(f'"{sys.executable}" "{build_script}"')
        os.system('mkdocs build')
        
    print(f"Loading print HTML from {print_html_path}...")
    file_url = f"file:///{print_html_path.replace(os.sep, '/')}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(file_url, wait_until="networkidle")
        await page.wait_for_timeout(2000)  # Ensure all styles & math render
        
        print("Exporting PDF...")
        await page.pdf(
            path=output_pdf_path,
            format="A4",
            print_background=True,
            margin={
                "top": "20mm",
                "bottom": "20mm",
                "left": "15mm",
                "right": "15mm"
            }
        )
        await browser.close()
        
    print(f"[SUCCESS] PDF generated: {output_pdf_path}")

if __name__ == '__main__':
    asyncio.run(generate_pdf())
