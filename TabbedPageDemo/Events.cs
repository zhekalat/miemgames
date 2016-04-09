using System;
using System.Collections.Generic;

namespace HSE_APP
{
	public class Event
	{
		public string time { get; set; }
		public string place { get; set; }
		public string game { get; set; }
	}

	public class Events
	{
		public List<Event> events { get; set; }
	}
	/*public class Events
	{
		public string Name { private set; get; }
		public string Desription { private set; get; }
		public string Image { private set; get; }
		public Events (string name, string description, string image)

		{
			this.Name = name;
			this.Desription = description;
			this.Image = image;
		}
	}*/
}

