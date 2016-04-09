using System;
using Xamarin.Forms;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using Newtonsoft.Json;

namespace HSE_APP
{
    public partial class MPage
    {


		//запрос на получение данных
		async void SendRequest(string URL)
		{
			using (var httpClient = new HttpClient())
			{
				List<Game> currGames = new List<Game> (); 
				var json = await httpClient.GetStringAsync(URL);
				//DescLabel.Text = json;
				currGames = JsonConvert.DeserializeObject<List<Game>>(json);

				ListView1.ItemsSource = currGames;

				//DescLabel.Text = res.status.message;
			}
		}

        public MPage()
        {
            InitializeComponent();
			SendRequest ("http://52.34.210.167:255/select_games");
		

			/*List<Events> currEvents = new List<Events> ();


		
			{
				new Events ("Мероприятие", "1", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "2", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "3", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "4", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "5", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "6", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "7", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "8", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "9", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "10", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "11", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "12", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "13", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "14", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
				new Events ("Мероприятие", "15", "https://nnov.hse.ru/data/2014/12/12/1104741612/20140825_hse_vorona.png"),
			};*/

			//ListView1.ItemsSource = currEvents;

			
        }

		async void ItemTapped (object sender, EventArgs e)
		{
			var modalPage = new HSE_APP.UpcomingAppointmentsPage ();
			await Navigation.PushModalAsync (modalPage);
		}
    }
}
