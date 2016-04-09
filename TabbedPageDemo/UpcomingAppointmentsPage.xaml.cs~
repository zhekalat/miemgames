using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Xamarin.Forms;
using HSE_APP;
using System.Net.Http;
using Newtonsoft.Json;


namespace HSE_APP
{
	public partial class UpcomingAppointmentsPage : ContentPage
	{

		public class Status
		{
			public string message { get; set; }
			public int value { get; set; }
		}

		public class Example
		{
			public Status status { get; set; }
		}


		//запрос на получение данных
		async void SendRequest(string URL)
		{
			using (var httpClient = new HttpClient())
			{
				var json = await httpClient.GetStringAsync(URL);
				DescLabel.Text = json;
				Example res = JsonConvert.DeserializeObject<Example>(json);

				DescLabel.Text = res.status.message;
			}
		}

		public UpcomingAppointmentsPage ()
		{
			InitializeComponent ();	

			SendRequest("http://api.geonames.org/findNearByWeatherJSON?lat=");
		}

		//Кнопка назад
		async void OnBackButtonClicked (object sender, EventArgs e)
		{
			var modalPage = new HSE_APP.MPage ();
			await Navigation.PushModalAsync (modalPage);
		}

		//кнопка регистрации
		async void OnRegisterButtonClicked (object sender, EventArgs e)
		{
			/*Зарегать пользователя на мероприятие*/
			var modalPage = new HSE_APP.MPage ();
			await Navigation.PushModalAsync (modalPage);
		} 
	}
}

