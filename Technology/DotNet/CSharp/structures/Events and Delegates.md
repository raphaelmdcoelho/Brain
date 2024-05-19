### Concepts

**Good sumary**: Just a property that allow a channel to subscribers subscribe to a event. So the event don't know who will subscribe to it. So the publisher class just need to have a event from a delegate type and a check if is not null to running it in a OnMethod. Then the subscriber just need a handler method to be assigned to the event (subscribe).

#### Events

* A mechanism for communication between object.
* Used in building *Loosely Coupled Applications*.
* Helps extending applications.

#### Delegates

* Agreement / Contract between `Publisher` and `Subscriber`.
* Determines the signature of the `event handler` method in `Subscriber`.

```csharp

// Without events:
public class VideoEnconder
{
	public void Enconde(Vide video)
	{
		// ...
		
		_mailService.Send(new Mail());
		_messageService.Send(new Text()); // need to recompile code to be added =/
	}
}
```

![[csharp_event_1.png]]

```csharp
// With events:
public class Video
{
	public string Title { get; set; }
}

class Program
{
	var video = new Video() { Title = "Video 1" };
	var videoEncoder = new VideoEncoder(); // publisher
	var mailService = new MailService(); // subscriber

	// 4 -
	videoEncoder.VideoEncoded += mailService.OnVideoEncoded; // I'm applying a reference to the subscriber method to be run by publisher

	videoEncoder.Encode(video);
}

public class VideoEnconder
{
	// 1 - Define a delegate
	// 2 - Define an event based on that delegate
	// 3 - Raise the event
	// 4 - Subscribe

	// 1 -
	public delegate void VideoEncodedEventHandler(object source, EventArgs args);
	// 2 -
	public event VideoEncodedEventHandler VideoEncoded; // Name refering as finished

	public void Enconde(Vide video)
	{
		Console.WriteLine("Enconding...");
		Thread.Sleep(3000);
		
		OnVideoEncoded();
	}

	// 3 - should be protected, virtual and void
	protected virtual void OnVideoEncoded()
	{
		if(VideoEncoded != null)
			VideoEncoded(this, EventArgs.Empty);

		// Same thing as above:
		//VideoEncoded?.Invoke(this, EventArgs.Empty);
	}
}

public class MailService
{
	// This method is a contract needed to use events
	// Used to be in the subscriber and they are genericly called, EVENT HANDLERS
	public void OnVideoEncoded(object source, EventArgs e)
	{
		Console.WriteLine("Mail service called!");
	}
}
```

### Examples

```csharp
// DELEGATE

public class Test
{
		public delegate void Print(string message);

		public void PrintHandler(string message)
		{
				Console.WriteLine(message);
		}

		public void Run(Print handler)
		{
				handler.Invoke();
		}

		Run(PrintHandler(string message);
}
```

#csharp #dotnet 