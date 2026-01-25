import json
import requests

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "Content-type": "application/json",
    "Accept": "application/json"
}
animal_id= "d1"
nuovo_animale={
    "type":"dog",
    "animal_id":animal_id,
    "name":"Rex",
    "age_years":2,
    "weight_kg":18.5,
    "breed":"Border Collie",
    "is_trained":True
}
animal_id= "c1"
nuovo_animale2={
    "name":"Micia",
    "age_years":3,
    "weight_kg":4.2,
    "indoor_only":True,
    "favorite_toy":"Pallina di lana"
}

if __name__== '__main__':
    # Test GET/
    response=requests.get(f"{BASE_URL}/",headers=HEADERS)
    print(response.status_code)

    #Test GET /animals
    response=requests.get(f"{BASE_URL}/animals",headers=HEADERS)
    if response.status_code==200:
        animals=response.json()
        print(f"lista animali {len(animals)}")
    
    # Test GET /animals/d1
    response=requests.get(f"{BASE_URL}/animals/{animal_id}",headers=HEADERS)
    if response.status_code==200:
        print(response.status_code,response.json())
    
    # Test GET /animals/d1/food
    response = requests.get(f"{BASE_URL}/animals/{animal_id}/food", headers=HEADERS)
    print(f"cibo giornaliero {response.status_code}")

    #Test GET /animals/d1/adoption
    response =requests.get(f"{BASE_URL}/animals/{animal_id}/adoption",headers=HEADERS)
    print(f"adozione {response.status_code}")

    # Test POST /animals/add 
    response=requests.post(f"{BASE_URL}/animals/add",json=nuovo_animale,headers=HEADERS)
    if response.status_code ==201:
        print(f"animale creato {response.status_code}")
    else:
        print("test non superato")

    # Test POST /animals/add

    response = requests.post (f"{BASE_URL}/animals/add",json=nuovo_animale2,headers=HEADERS)
    if response.status_code==201:
        print(f"animale creato {response.status_code}")
    else:
        print("Test non superato")
    
    # Test POST /animals/<animal_id>/adopt
    response=requests.post(f"{BASE_URL}/animals/{animal_id}/adopt",json=nuovo_animale,headers=HEADERS)
    if response.status_code ==201:
        print (f"cane adottato {response.status_code}")
    else:
        print("cane non adottato")
    

    # Test GET /animals/<animal_id>/adoption
    response=requests.get(f"{BASE_URL}/animals/{animal_id}/adoption",headers=HEADERS)
    if response.status_code==200:
        print(f"animale adottato {response.status_code}")
    else:
        print("animale non adottato")

