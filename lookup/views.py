from django.shortcuts import render
import creds
# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+""&distance=10&API_KEY="+creds.api_key)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['AQI'] >= 0 and api[0]['AQI'] <= 50:
            category_color = "good"
            category_description = "(0 to 50): Air quality is satisfactory, and air pollution poses little or no risk."
        elif api[0]['AQI'] >= 51 and api[0]['AQI'] <= 100:
            category_color = "moderate"
            category_description = "(51 to 100): Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        elif api[0]['AQI'] >= 101 and api[0]['AQI'] <= 150:
            category_color = "usg"
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
        elif api[0]['AQI'] >= 151 and api[0]['AQI'] <= 200:
            category_color = "unhealthy"
            category_description= "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['AQI'] >= 201 and api[0]['AQI'] <= 300:
            category_color = "veryunhealthy"
            category_description = "Health alert: The risk of health effects is increased for everyone."
        elif api[0]['AQI'] >= 301:
            category_color = "hazardous"
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."


        return render(request, 'home.html', {'api': api, 'category_description':category_description, 'category_color':category_color})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=43229&distance=25&API_KEY=BB342B6F-E557-4007-AC17-E0CB4B645C4D")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['AQI'] >= 0 and api[0]['AQI'] <= 50:
            category_color = "good"
            category_description = "(0 to 50): Air quality is satisfactory, and air pollution poses little or no risk."
        elif api[0]['AQI'] >= 51 and api[0]['AQI'] <= 100:
            category_color = "moderate"
            category_description = "(51 to 100): Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        elif api[0]['AQI'] >= 101 and api[0]['AQI'] <= 150:
            category_color = "usg"
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
        elif api[0]['AQI'] >= 151 and api[0]['AQI'] <= 200:
            category_color = "unhealthy"
            category_description= "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['AQI'] >= 201 and api[0]['AQI'] <= 300:
            category_color = "veryunhealthy"
            category_description = "Health alert: The risk of health effects is increased for everyone."
        elif api[0]['AQI'] >= 301:
            category_color = "hazardous"
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."


        return render(request, 'home.html', {'api': api, 'category_description':category_description, 'category_color':category_color})

def about(request):
    return render(request, 'about.html', {})
