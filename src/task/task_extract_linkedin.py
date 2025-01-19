import requests
from bs4 import BeautifulSoup
from prefect import task


@task(name="task_extract_linkedin")
def task_extract_linkedin():
    jobs = []
    url = 'https://www.linkedin.com/jobs/search/?currentJobId=4112400001&keywords=python'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    
    response = requests.get(url, headers=headers)


    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
        job_cards = soup.find_all('div', class_='base-card')    
        # Extraer la información para cada empleo
        for job_card in job_cards:
            # Descripción del empleo
            description_tag = job_card.find('h3', class_='base-search-card__title')
            description = description_tag.get_text(strip=True) if description_tag else "No disponible"

            # Empresa
            company_tag = job_card.find('h4', class_='base-search-card__subtitle')
            company = company_tag.get_text(strip=True) if company_tag else "No disponible"

            # Localización
            location_tag = job_card.find('span', class_='job-search-card__location')
            location = location_tag.get_text(strip=True) if location_tag else "No disponible"

            # Fecha de publicación
            date_tag = job_card.find('time')
            date = date_tag.get_text(strip=True) if date_tag else "No disponible"

            # URL del empleo
            url_tag = job_card.find('a', class_='base-card__full-link')
            job_url = url_tag['href'] if url_tag else "No disponible"

            # Agregar a la lista
            jobs.append({
                'description': description,
                'company': company,
                'location': location,
                'date': date,
                'url': job_url
            })
            
    else:
        print(f'Error {response.status_code} {response.reason}')
    return jobs
