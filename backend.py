import requests
APIkey ='08f8b2ae06822219e793333####3dldfs'
def get_data(place,days):

     url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
     response =requests.get(url)
     context = response.json()
     filtered_context = context['list']
     nr_values = 8 * days
     filtered_context = filtered_context[:nr_values]
     return filtered_context




if __name__ == '__main__':
     print(get_data(place='Accra',days=2,option='Sky'))
