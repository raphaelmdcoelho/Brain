
Asynchronous programming in .NET allows a program to perform tasks without blocking the main thread, enabling the program to remain responsive.

The keyword `await` is used to pause the execution of an async method until the awaited task completes.

`Tasks` Represents an asynchronous operation. The `Task` class is used to handle and control these operations.

## Relation to the Thread Pool

**Thread Pool**

A collection of threads managed by .NET to perform background tasks. Instead of creating a new thread every time an asynchronous task is performed, .NET uses threads from this pool to optimize performance.

When you use `async` and `await`, **the method doesn't block the main thread. Instead, it runs on a thread from the thread pool.** **Once the awaited task completes, it returns to the context it was called from, which is often the main thread.**

In .NET, **synchronous methods typically do not directly interact with the thread pool** unless they explicitly use it, such as via `Task.Run` or `ThreadPool.QueueUserWorkItem`. **By default, synchronous methods run on the current thread that calls them**. However, you can use the thread pool to run synchronous methods in a background thread, thus freeing up the main thread.

## Multi-Threaded Programming

Multi-threaded programming in C# involves **creating and managing multiple threads within a single application.** This allows the application to perform multiple tasks concurrently, improving performance and responsiveness, especially on multi-core processors.

### Key Concepts

1. **Thread:** The smallest unit of a process that can be scheduled for execution. In C#, you can create and manage threads using the `Thread` class.
2. **Thread Pool:** A pool of worker threads managed by the .NET Framework. It handles thread creation and management, which helps improve performance and resource management.
3. **Task:** A higher-level abstraction over threads. Tasks are part of the Task Parallel Library (TPL) and provide a more efficient and easier way to work with asynchronous operations.

**No dependencies**

```csharp
using System;  
using System.Threading;  
  
class Program  
{  
static void Main()  
{  
// Create three threads  
Thread thread1 = new Thread(new ThreadStart(Activity1));  
Thread thread2 = new Thread(new ThreadStart(Activity2));  
Thread thread3 = new Thread(new ThreadStart(Activity3));  
  
// Start the threads  
thread1.Start();  
thread2.Start();  
thread3.Start();  
  
// Wait for threads to complete  
thread1.Join();  
thread2.Join();  
thread3.Join();  
  
Console.WriteLine("All activities completed.");  
}  
  
static void Activity1()  
{  
}  
  
static void Activity2()  
{  
}  
  
static void Activity3()  
{  
}  
}
```

**Dependencies scenario**

```csharp
using System;  
using System.Threading;  
  
class Program  
{  
static ManualResetEvent activity1Completed = new ManualResetEvent(false);  
static string sharedData;  
  
static void Main()  
{  
// Create three threads  
Thread thread1 = new Thread(new ThreadStart(Activity1));  
Thread thread2 = new Thread(new ThreadStart(Activity2));  
Thread thread3 = new Thread(new ThreadStart(Activity3));  
  
// Start the threads  
thread1.Start();  
thread2.Start();  
thread3.Start();  
  
// Wait for threads to complete  
thread1.Join();  
thread2.Join();  
thread3.Join();  
  
Console.WriteLine("All activities completed.");  
}  
  
static void Activity1()  
{  
// Set shared data and signal completion  
sharedData = "Data from Activity 1";  
activity1Completed.Set();  
}  
  
static void Activity2()  
{  
// Wait for Activity 1 to complete  
activity1Completed.WaitOne();  
  
// Implementation  
var Act1Results = sharedData;  
}  
  
static void Activity3()  
{  
}  
}
```

## Handle Exceptions

```csharp
using System;  
using System.Threading;  
using System.Threading.Tasks;  
  
class Program  
{  
static CancellationTokenSource cts = new CancellationTokenSource();  
  
static void Main()  
{  
// Create and start tasks  
Task task1 = Task.Run(() => Activity1(cts.Token), cts.Token);  
Task task2 = Task.Run(() => Activity2(cts.Token), cts.Token);  
Task task3 = Task.Run(() => Activity3(cts.Token), cts.Token);  
  
try  
{  
// Wait for all tasks to complete  
Task.WaitAll(task1, task2, task3);  
}  
catch (AggregateException ex)  
{  
// Handle the exception  
foreach (var innerEx in ex.InnerExceptions)  
{  
Console.WriteLine($"Exception: {innerEx.Message}");  
}  
  
// Revert changes here  
RevertChanges();  
  
// Signal that the tasks were cancelled  
Console.WriteLine("All activities stopped and changes reverted.");  
}  
}  
  
static void Activity1(CancellationToken token)  
{  
try  
{  
throw new Exception("Error in Activity 1");  
}  
catch (Exception ex)  
{  
cts.Cancel(); // Cancel all tasks  
throw; // Re-throw the exception to be caught by Task.WaitAll  
}  
}  
  
static void Activity2(CancellationToken token)  
{  
try  
{  
}  
catch (OperationCanceledException)  
{  
Console.WriteLine("Activity 2 cancelled.");  
}  
}  
  
static void Activity3(CancellationToken token)  
{  
try  
{  
}  
catch (OperationCanceledException)  
{  
Console.WriteLine("Activity 3 cancelled.");  
}  
}  
  
static void RevertChanges()  
{  
// Implement the logic to revert changes here  
Console.WriteLine("Reverting changes...");  
}  
}
```

#csharp #dotnet #async #parallel #thread