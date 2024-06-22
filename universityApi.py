from concurrent.futures import ThreadPoolExecutor
import requests

URL = 'http://universities.hipolabs.com/search?country='
COUNTRIES = [
    'Poland',
    'Japan',
    'Germany',
    'France',
    'Italy',
    'Spain',
    'Norway',
    'Sweden',
    'Austria',
    'Hungary',
    'Canada',
    'Australia',
    'India',
    'Argentina',
    'Portugal'
]

def fetch_universities(country):
    return requests.get(URL + country).json()

if __name__ == '__main__':
    country_university_dict = dict()
    with ThreadPoolExecutor(max_workers=15) as executor:
        country_universities = executor.map(fetch_universities, COUNTRIES)
        for i in country_universities:
            for uni_obj in i:
                university_name = uni_obj['name']
                university_country = uni_obj['country']
                
                if country_university_dict.get(university_country) is not None:
                    country_university_dict[university_country].append(university_name)
                else:
                    country_university_dict[university_country] = [university_name]

    print(country_university_dict)       
